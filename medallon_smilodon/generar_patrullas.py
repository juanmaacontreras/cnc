#!/usr/bin/env python3
"""Genera las 6 medallas de patrulla y una placa lista para el slicer.

Salida en ./patrullas/:
  * medalla_<patrulla>.stl         – una malla por medalla
  * medallas_CC2_listo.3mf         – proyecto de ElegooSlicer para la Centauri Carbon 2:
                                     las 6 medallas en la cama, configuración y cambio de color
  * render_<patrulla>.png          – vista frontal en dos colores
  * render_placa.png               – vista superior de la placa completa

Usa la geometría de generar_medallon.py; el nombre va en el campo central.
"""

import json
import zipfile
from pathlib import Path

import numpy as np
from PIL import Image

import generar_medallon as gm

PATRULLAS = ["Chita", "Cóndor", "Tigre", "Pantera", "Zorro", "Lobo"]
BED = 256.0     # cama de 256×256 (Bambu Lab A1 / P1 / X1, Orca, etc.)
GAP = 4.0       # separación entre medallas (deja 4 mm a cada lado de la cama)
OUT = gm.OUT / "patrullas"


def slug(name):
    return name.lower().replace("ó", "o")


def layout(meshes):
    """3 columnas × 2 filas; la fila de arriba con la oreja hacia arriba y la de
    abajo girada 180° (oreja hacia abajo), así los discos quedan enfrentados."""
    placed = []
    w = max(m.extents[0] for m in meshes)
    for i, m in enumerate(meshes):
        m = m.copy()
        row, col = divmod(i, 3)
        if row == 1:
            m.apply_transform(np.diag([-1, -1, 1, 1]))  # giro de 180° en Z
        b = m.bounds
        x = BED / 2 + (col - 1) * (w + GAP) - (b[0][0] + b[1][0]) / 2
        # los centros de los discos quedan a (DIAM + GAP)/2 del centro de la cama
        y = BED / 2 + (1 if row == 0 else -1) * (gm.DIAM + GAP) / 2
        m.apply_translation([x, y, -b[0][2]])
        placed.append(m)
    return placed


def write_3mf(path, meshes, names, settings=None, color_change_z=None):
    """Escribe la placa como 3MF.

    Con `settings` (la configuración de cc2_project_settings.json) el archivo se guarda
    como proyecto de ElegooSlicer: abre con impresora, proceso y filamentos cargados
    y, con `color_change_z`, el cambio al filamento 2 en la capa que termina a esa altura.
    Sin `settings` es un 3MF común que abre en cualquier slicer.
    """
    objs, items = [], []
    for i, (m, n) in enumerate(zip(meshes, names), start=1):
        lo, hi = m.bounds
        c = np.array([(lo[0] + hi[0]) / 2, (lo[1] + hi[1]) / 2, lo[2]])
        verts = m.vertices - c  # malla local; la posición en la cama va en la transformación
        v = "".join(f'<vertex x="{x:.4f}" y="{y:.4f}" z="{z:.4f}"/>' for x, y, z in verts)
        t = "".join(f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in m.faces)
        objs.append(f'<object id="{i}" name="Medalla {n}" type="model"><mesh>'
                    f'<vertices>{v}</vertices><triangles>{t}</triangles></mesh></object>')
        items.append(f'<item objectid="{i}" transform="1 0 0 0 1 0 0 0 1 '
                     f'{c[0]:.4f} {c[1]:.4f} {c[2]:.4f}" printable="1"/>')
    meta = '<metadata name="Title">Medallas patrullas - Museo de Cs. Naturales de La Plata 2026</metadata>'
    if settings is not None:
        meta += ('<metadata name="Application">ElegooSlicer-1.5.3.5</metadata>'
                 '<metadata name="BambuStudio:3mfVersion">1</metadata>')
    model = ('<?xml version="1.0" encoding="UTF-8"?>\n'
             '<model unit="millimeter" xml:lang="es-AR" '
             'xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
             'xmlns:BambuStudio="http://schemas.bambulab.com/package/2021">'
             f'{meta}<resources>{"".join(objs)}</resources><build>{"".join(items)}</build></model>')
    types = ('<?xml version="1.0" encoding="UTF-8"?>\n'
             '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
             '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
             '<Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>'
             '<Default Extension="config" ContentType="text/plain"/>'
             '<Default Extension="xml" ContentType="application/xml"/>'
             '</Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Target="/3D/3dmodel.model" Id="rel0" '
            'Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", types)
        z.writestr("_rels/.rels", rels)
        z.writestr("3D/3dmodel.model", model)
        if settings is not None:
            z.writestr("Metadata/project_settings.config",
                       json.dumps(settings, indent=4, ensure_ascii=False))
        if settings is not None and color_change_z is not None:
            # mismo formato que guarda ElegooSlicer (bbs_3mf.cpp): type 2 = cambio de filamento
            colour = settings["filament_colour"][1]
            z.writestr("Metadata/custom_gcode_per_layer.xml",
                       '<?xml version="1.0" encoding="utf-8"?>\n<custom_gcodes_per_layer><plate>'
                       '<plate_info id="1"/>'
                       f'<layer top_z="{color_change_z:g}" type="2" extruder="2" color="{colour}" '
                       'extra="" gcode="tool_change"/>'
                       '<mode value="MultiAsSingle"/></plate></custom_gcodes_per_layer>\n')


def main():
    OUT.mkdir(exist_ok=True)
    meshes, renders, masks = [], [], []
    for n in PATRULLAS:
        layers, _ = gm.build_layers(n)
        mesh = gm.build_mesh(layers)
        assert mesh.is_watertight, n
        mesh.export(OUT / f"medalla_{slug(n)}.stl")
        meshes.append(mesh)
        h, inside, px = gm.heightmap(layers)
        png = OUT / f"render_{slug(n)}.png"
        gm.render(h, inside, px, png, out_px=1000, two_color=True)
        renders.append(png)
        masks.append(Image.fromarray((inside * 255).astype(np.uint8)).resize((1000, 1000)))
        print(f"{n:8s} vol={mesh.volume / 1000:.1f} cm³  bbox={np.round(mesh.extents, 1)}")

    placed = layout(meshes)
    lo = np.min([m.bounds[0] for m in placed], axis=0)
    hi = np.max([m.bounds[1] for m in placed], axis=0)
    assert lo[0] >= 0 and lo[1] >= 0 and hi[0] <= BED and hi[1] <= BED, (lo, hi)
    settings_file = OUT / "cc2_project_settings.json"
    settings = json.loads(settings_file.read_text(encoding="utf-8")) if settings_file.exists() else None
    # cambio a blanco al empezar la capa que termina en BASE + 0,2 mm (capas de 0,2)
    write_3mf(OUT / "medallas_CC2_listo.3mf", placed, PATRULLAS, settings, gm.COLOR_CHANGE_Z + 0.2)
    print(f"placa: x {lo[0]:.1f}–{hi[0]:.1f}  y {lo[1]:.1f}–{hi[1]:.1f} mm (cama {BED:.0f})")

    # mosaico de la placa (vista superior) a partir de los renders individuales
    tile = 1000
    s = tile / (gm.DIAM + 2 * 14.0)  # mismo encuadre que heightmap()
    cw, ch = int(BED * s), int(BED * s)
    sheet = Image.new("RGB", (cw, ch), (214, 213, 209))
    for i, png in enumerate(renders):
        im, mk = Image.open(png), masks[i]
        row, col = divmod(i, 3)
        if row == 1:
            im, mk = im.rotate(180), mk.rotate(180)
        cx = BED / 2 + (col - 1) * (gm.DIAM + GAP)
        cy = BED / 2 - (1 if row == 0 else -1) * (gm.DIAM + GAP) / 2
        sheet.paste(im, (int(cx * s - tile / 2), int(cy * s - tile / 2)), mk)
    sheet.resize((1400, 1400), Image.LANCZOS).save(OUT / "render_placa.png")


if __name__ == "__main__":
    main()
