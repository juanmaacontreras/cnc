#!/usr/bin/env python3
"""Arma la configuración del proyecto (ElegooSlicer) para las medallas en la CC2.

Toma los perfiles oficiales de ElegooSlicer (impresora Centauri Carbon 2 0.4,
proceso 0.20mm Standard, filamento Elegoo PLA), resuelve la herencia de cada uno,
aplica los ajustes de calidad para las medallas y guarda el resultado en
patrullas/cc2_project_settings.json. generar_patrullas.py lo mete en el 3MF.

Uso:  python3 armar_config_cc2.py <ruta a ElegooSlicer/resources/profiles/Elegoo>
"""

import glob
import json
import sys
from pathlib import Path

PRINTER = "Elegoo Centauri Carbon 2 0.4 nozzle"
PROCESS = "0.20mm Standard @Elegoo CC2 0.4 nozzle"
FILAMENT = "Elegoo PLA @ECC2"
COLOURS = ["#000000", "#FFFFFF"]  # filamento 1 negro (base), filamento 2 blanco (relieves)

# Ajustes sobre el perfil 0.20mm Standard
PROCESS_OVERRIDES = {
    # calidad de paredes y superficies
    "wall_generator": "arachne",
    "wall_sequence": "inner-outer-inner wall",
    "wall_loops": "3",
    "top_shell_layers": "5",
    "bottom_shell_layers": "4",
    "top_surface_pattern": "monotonic",
    "seam_position": "aligned",
    "elefant_foot_compensation": "0.15",
    "reduce_crossing_wall": "1",
    # planchado de todas las caras superiores (fondo, letras, huesos, borde)
    "ironing_type": "top",
    "ironing_pattern": "rectilinear",
    "ironing_flow": "10%",
    "ironing_spacing": "0.12",
    "ironing_speed": "30",
    "ironing_inset": "0.15",
    # relleno
    "sparse_infill_pattern": "gyroid",
    "sparse_infill_density": "15%",
    # velocidades más tranquilas en lo que se ve
    "outer_wall_speed": "100",
    "top_surface_speed": "100",
    "initial_layer_speed": "40",
    "outer_wall_acceleration": "3000",
    # sin soportes, brim ni falda (las medallas llegan a 2 mm del borde de la cama)
    "enable_support": "0",
    "brim_type": "no_brim",
    "skirt_loops": "0",
    # la CC2 purga el cambio de filamento por su cuenta (purge_in_prime_tower = 0)
    "enable_prime_tower": "0",
}

SKIP = {"name", "type", "inherits", "from", "setting_id", "instantiation", "renamed_from",
        "compatible_printers", "compatible_printers_condition", "compatible_prints",
        "compatible_prints_condition", "filament_id", "description", "version"}


def load_index(root):
    idx = {}
    for f in glob.glob(str(Path(root) / "**" / "*.json"), recursive=True):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if isinstance(d, dict) and "name" in d and "type" in d:
            idx[d["name"]] = d
    return idx


def flatten(idx, name):
    chain, n = [], name
    while n:
        chain.append(idx[n])
        n = idx[n].get("inherits")
    out = {}
    for d in reversed(chain):
        out.update(d)
    return out


def main(root):
    idx = load_index(root)
    printer, process, filament = (flatten(idx, n) for n in (PRINTER, PROCESS, FILAMENT))
    filament_id = filament.get("filament_id", "")

    cfg = {}
    for d in (printer, process):
        cfg.update({k: v for k, v in d.items() if k not in SKIP})
    for k, v in filament.items():
        if k in SKIP:
            continue
        # los valores de filamento van uno por filamento (negro, blanco)
        cfg[k] = (v * len(COLOURS)) if isinstance(v, list) and len(v) == 1 else v
    cfg.update(PROCESS_OVERRIDES)

    n = len(COLOURS)
    cfg.update({
        "printer_settings_id": PRINTER,
        "print_settings_id": PROCESS,
        "filament_settings_id": [FILAMENT] * n,
        "filament_ids": [filament_id] * n,
        "inherits_group": [""] * (n + 2),
        "different_settings_to_system": [";".join(sorted(PROCESS_OVERRIDES))] + [""] * (n + 1),
        "filament_colour": COLOURS,
        "filament_self_index": [str(i + 1) for i in range(n)],
        "filament_extruder_variant": ["Direct Drive Standard"] * n,
        # purga negro → blanco: el valor que trae ElegooSlicer para la CC2 (900 mm³)
        "flush_volumes_matrix": ["0", "900", "300", "0"],
        "flush_volumes_vector": ["140"] * (2 * n),
        "flush_multiplier": ["1"],
        "curr_bed_type": "Textured PEI Plate",
        "name": "project_settings",
        "from": "project",
        "version": "1.5.3.5",
    })
    out = Path(__file__).resolve().parent / "patrullas" / "cc2_project_settings.json"
    out.write_text(json.dumps(cfg, indent=4, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    print(f"{out.name}: {len(cfg)} claves")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else
         "/home/user/elegoo-3d/elegooslicer/resources/profiles/Elegoo")
