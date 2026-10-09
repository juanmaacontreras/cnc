#!/usr/bin/env python3
"""Medallón conmemorativo imprimible en 3D – Museo de Cs. Naturales de La Plata.

Genera:
  * medallon_smilodon.stl   – malla cerrada (manifold) lista para el slicer
  * render_frontal.png      – vista frontal estilo "clay render" (PLA gris mate)

Dependencias:  pip install numpy shapely manifold3d trimesh matplotlib pillow scipy

Todas las medidas están en milímetros. El diseño se describe una sola vez como
capas 2D (polígonos de shapely + altura); de esas capas salen tanto la malla
como el mapa de alturas que se usa para el render.
"""

import math
from pathlib import Path

import numpy as np
import trimesh
from manifold3d import CrossSection, FillRule, Manifold
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextPath
from PIL import Image, ImageDraw
from scipy import ndimage
from shapely import affinity, minimum_bounding_circle, minimum_bounding_radius
from shapely.geometry import LineString, MultiPolygon, Point, Polygon
from shapely.ops import unary_union

OUT = Path(__file__).resolve().parent

# ---------------------------------------------------------------- parámetros
DIAM = 80.0           # diámetro total
R = DIAM / 2
BASE = 3.0            # espesor del disco (nivel del campo)
CHAMFER_BOTTOM = 0.6  # chaflán inferior (evita "pata de elefante")

RIM_IN = 35.6         # radio interior del borde exterior
RIM_TOP = BASE + 2.6  # altura del borde exterior
RIM_BEVEL = 0.5

RING_R = 26.6         # anillo interior que separa el texto del campo central
RING_W = 1.3
RING_H = 1.1

TEXT = "MUSEO DE CS. NATURALES DE LA PLATA"
YEAR = "2026"
TEXT_H = 1.2          # relieve de las letras
TEXT_SPAN_DEG = 236   # arco que ocupa la leyenda superior
FONT = FontProperties(family="DejaVu Sans", weight="bold")

SKEL_FIELD_R = 24.6   # el esqueleto debe caber dentro de este radio

# Alturas de relieve (sobre el campo) para dar profundidad de bajorrelieve
H_FAR = 0.8           # patas del lado lejano
H_RIBS = 1.3          # caja torácica / núcleo de la columna
H_SPINE = 1.7         # vértebras, escápula, pelvis
H_NEAR = 2.1          # patas cercanas, cráneo
H_SABER = 2.3         # colmillo


# ---------------------------------------------------------------- utilidades
def bone(p0, p1, w, knob=1.3):
    """Hueso largo estilizado: cápsula gruesa con epífisis redondeadas."""
    shaft = LineString([p0, p1]).buffer(w / 2, cap_style=1)
    ends = [Point(p).buffer(w / 2 * knob) for p in (p0, p1)]
    return unary_union([shaft, *ends])


def stroke(points, w):
    return LineString(points).buffer(w / 2, cap_style=1, join_style=1)


def ellipse(cx, cy, a, b, ang=0.0):
    e = affinity.scale(Point(0, 0).buffer(1, resolution=24), a, b)
    return affinity.translate(affinity.rotate(e, ang), cx, cy)


def bezier(p0, p1, p2, n=24):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2 = map(np.asarray, (p0, p1, p2))
    return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t**2 * p2


def polyline_resample(pts, step):
    """Puntos equiespaciados (y su ángulo) a lo largo de una polilínea."""
    line = LineString(pts)
    out = []
    d = step / 2
    while d < line.length:
        a, b = line.interpolate(d - 0.05), line.interpolate(d + 0.05)
        ang = math.degrees(math.atan2(b.y - a.y, b.x - a.x))
        p = line.interpolate(d)
        out.append((p.x, p.y, ang, d / line.length))
        d += step
    return out


def rounded_rect(cx, cy, length, height, ang, r):
    rect = Polygon([(-length / 2 + r, -height / 2 + r), (length / 2 - r, -height / 2 + r),
                    (length / 2 - r, height / 2 - r), (-length / 2 + r, height / 2 - r)]).buffer(r)
    return affinity.translate(affinity.rotate(rect, ang), cx, cy)


def glyph_geom(ch, size, xscale=1.0):
    """Polígono shapely de un carácter (línea de base en y=0) y su avance."""
    if ch == " ":
        return Polygon(), 0.32 * size * xscale
    tp = TextPath((0, 0), ch, size=size, prop=FONT)
    geom = Polygon()
    for ring in tp.to_polygons():
        if len(ring) >= 3:
            geom = geom.symmetric_difference(Polygon(ring).buffer(0))  # par-impar
    adv = TextPath((0, 0), ch + "|", size=size, prop=FONT).get_extents().x1 - \
        TextPath((0, 0), "|", size=size, prop=FONT).get_extents().x1
    return affinity.scale(geom, xscale, 1, origin=(0, 0)), adv * xscale


# ---------------------------------------------------------------- esqueleto
def smilodon():
    """Silueta estilizada del esqueleto de Smilodon (perfil, mirando a la derecha).

    Devuelve un dict {altura_relieve: geometría} en coordenadas de diseño.
    Todas las piezas son gruesas: sin costillas finas ni partes frágiles.
    """
    L = {H_FAR: [], H_RIBS: [], H_SPINE: [], H_NEAR: [], H_SABER: []}

    # --- cráneo: cresta sagital alta, hocico corto
    cranium = Polygon([(8.4, 6.0), (8.9, 7.3), (10.3, 8.5), (12.3, 9.2), (14.4, 9.1),
                       (16.3, 8.5), (18.0, 7.6), (19.6, 6.9), (20.5, 6.1), (20.4, 5.2),
                       (19.4, 4.9), (18.0, 5.0), (16.0, 5.1), (13.5, 5.3), (11.0, 5.4),
                       (9.2, 5.3)])
    cranium = cranium.buffer(0.3).buffer(-0.3)
    orbit = ellipse(16.4, 7.0, 0.95, 0.85)
    fenestra = ellipse(12.6, 7.1, 1.9, 0.75, 6)
    nasal = ellipse(19.5, 6.0, 0.4, 0.55, -25)
    # mandíbula levemente abierta, con reborde mentoniano
    jaw = Polygon([(11.4, 4.7), (13.0, 4.8), (15.5, 4.5), (18.4, 4.3), (19.8, 4.1),
                   (19.9, 3.4), (19.2, 2.6), (18.6, 3.2), (15.0, 3.5), (13.0, 3.5),
                   (11.6, 3.9)]).buffer(0.25).buffer(-0.25)
    L[H_SPINE].append(cranium)                       # fondo de órbita/fosas
    L[H_NEAR].append(cranium.difference(unary_union([orbit, fenestra, nasal])))
    L[H_NEAR].append(jaw)
    # colmillo de sable: curvo, cónico, con punta roma
    saber = Polygon([(18.75, 5.3), (18.65, 3.8), (18.25, 2.3), (17.6, 0.95), (17.1, 0.6),
                     (16.85, 0.95), (17.05, 2.3), (17.25, 3.8), (17.25, 5.3)]).buffer(0.2)
    L[H_SABER].append(saber)

    # --- columna: cervicales, dorsales, lumbares, sacro y cola corta
    neck = bezier((9.8, 5.0), (7.6, 4.9), (5.4, 3.9), 30)
    back = np.vstack([bezier((5.4, 3.9), (0.5, 5.4), (-5.0, 4.6), 40),
                      bezier((-5.0, 4.6), (-8.5, 4.2), (-10.8, 3.3), 20)[1:]])
    tail = bezier((-10.8, 3.3), (-14.8, 2.3), (-17.4, -1.6), 30)
    core = np.vstack([neck, back[1:], tail[1:]])
    L[H_RIBS].append(stroke(core, 0.9))              # núcleo continuo (sin piezas sueltas)

    for x, y, ang, _ in polyline_resample(neck, 1.45):
        L[H_SPINE].append(rounded_rect(x, y, 1.05, 1.5, ang, 0.35))
    for x, y, ang, t in polyline_resample(back, 1.38):
        L[H_SPINE].append(rounded_rect(x, y, 1.0, 1.45, ang, 0.35))
        if t < 0.55:   # apófisis espinosas dorsales, gruesas y cortas
            h = 1.35 - 0.6 * t
            nx, ny = -math.sin(math.radians(ang)), math.cos(math.radians(ang))
            L[H_SPINE].append(stroke([(x, y), (x + nx * h - 0.35, y + ny * h)], 0.85))
    for x, y, ang, t in polyline_resample(tail, 1.3):
        s = 1.0 - 0.45 * t
        L[H_SPINE].append(rounded_rect(x, y, 0.95 * s + 0.1, 1.35 * s, ang, 0.3))

    # --- caja torácica: pocas costillas, anchas
    ribs = []
    for i in range(6):
        x0 = 4.0 - i * 1.85
        y0 = float(np.interp(-x0, -back[:, 0], back[:, 1])) - 0.2
        depth = 7.9 - 0.55 * i ** 1.25
        p2 = (x0 - 1.2 - 0.25 * i, y0 - depth)
        p1 = (x0 - 0.2, y0 - depth * 0.55)
        ribs.append(stroke(bezier((x0, y0), p1, p2), 1.15 if i < 5 else 1.0))
    L[H_RIBS].append(unary_union(ribs))

    # --- cintura escapular y pelvis
    scapula = Polygon([(6.6, 4.6), (3.6, 4.9), (3.3, 3.9), (4.7, 0.9), (5.6, 0.3),
                       (6.3, 1.0)]).buffer(0.25).buffer(-0.25)
    pelvis = Polygon([(-7.5, 4.3), (-9.0, 4.7), (-10.5, 3.2), (-12.6, 1.3), (-13.0, 0.1),
                      (-11.7, -0.2), (-10.4, 0.9), (-8.6, 2.6)]).buffer(0.25).buffer(-0.25)
    L[H_SPINE] += [scapula, pelvis]

    # --- patas cercanas (paso al frente) y lejanas (más bajas)
    def leg_fore(sh, el, wr, paw, toe, layer, k=1.0):
        L[layer] += [bone(sh, el, 1.45 * k), bone(el, wr, 1.25 * k),
                     bone(wr, paw, 1.05 * k, 1.2), ellipse(*toe, 1.05 * k, 0.62 * k, -8)]

    def leg_hind(hip, knee, ank, paw, toe, layer, k=1.0):
        L[layer] += [bone(hip, knee, 1.5 * k), bone(knee, ank, 1.3 * k),
                     bone(ank, paw, 1.05 * k, 1.2), ellipse(*toe, 1.05 * k, 0.62 * k, -8),
                     ellipse(ank[0] - 0.45, ank[1] + 0.1, 0.75 * k, 0.6 * k)]  # talón

    leg_fore((5.3, 0.7), (6.9, -4.5), (6.0, -10.0), (7.3, -11.6), (8.3, -12.0), H_NEAR)
    leg_fore((3.7, 0.3), (2.9, -4.7), (1.6, -10.0), (2.9, -11.6), (3.9, -12.0), H_FAR, 0.95)
    leg_hind((-10.9, 1.1), (-8.2, -4.5), (-11.5, -9.0), (-10.7, -11.6), (-9.6, -12.0), H_NEAR)
    leg_hind((-11.8, 0.6), (-10.4, -4.9), (-14.2, -8.7), (-13.8, -11.6), (-12.7, -12.0),
             H_FAR, 0.95)

    return {h: unary_union(g) for h, g in L.items()}


# ---------------------------------------------------------------- leyendas
def arc_text(text, r_base, span_deg, cap_target, xscale):
    size = cap_target / 0.73  # altura de mayúsculas ≈ 0.73 em en DejaVu Sans Bold
    glyphs = [glyph_geom(c, size, xscale) for c in text]
    r_mid = r_base + cap_target / 2
    tracking = 0.18 * size
    total = sum(a for _, a in glyphs) + tracking * (len(text) - 1)
    # el tracking se ajusta para que el texto ocupe exactamente span_deg
    tracking += (math.radians(span_deg) * r_mid - total) / (len(text) - 1)
    s = 0.0
    theta0 = math.radians(90 + span_deg / 2)
    parts = []
    for (g, adv) in glyphs:
        if not g.is_empty:
            c = s + adv / 2
            th = theta0 - c / r_mid
            g = affinity.translate(g, -adv / 2, 0)
            g = affinity.rotate(g, math.degrees(th) - 90, origin=(0, 0))
            g = affinity.translate(g, r_base * math.cos(th), r_base * math.sin(th))
            parts.append(g)
        s += adv + tracking
    return unary_union(parts), tracking


def straight_text(text, cap, cy, xscale=1.0, tracking=0.0):
    size = cap / 0.73
    parts, x = [], 0.0
    for ch in text:
        g, adv = glyph_geom(ch, size, xscale)
        parts.append(affinity.translate(g, x, 0))
        x += adv + tracking
    geom = unary_union(parts)
    b = geom.bounds
    return affinity.translate(geom, -(b[0] + b[2]) / 2, cy - (b[1] + b[3]) / 2)


# ---------------------------------------------------------------- composición
def build_layers():
    """Lista de (geometría 2D, altura superior absoluta)."""
    layers = []
    ring = Point(0, 0).buffer(RING_R + RING_W / 2, 256).difference(
        Point(0, 0).buffer(RING_R - RING_W / 2, 256))
    layers.append((ring, BASE + RING_H))

    band_in, band_out = RING_R + RING_W / 2, RIM_IN
    cap = 4.0
    r_base = (band_in + band_out) / 2 - cap / 2
    legend, trk = arc_text(TEXT, r_base, TEXT_SPAN_DEG, cap, 0.86)
    year = straight_text(YEAR, 5.2, -(band_in + band_out) / 2, 1.0, 0.5)
    layers += [(legend, BASE + TEXT_H), (year, BASE + TEXT_H)]
    # pequeños puntos de separación entre leyenda y año
    for sgn in (-1, 1):
        th = math.radians(90 + sgn * (TEXT_SPAN_DEG / 2 + 11))
        rm = (band_in + band_out) / 2
        layers.append((Point(rm * math.cos(th), rm * math.sin(th)).buffer(1.0, 32),
                       BASE + TEXT_H))

    skel = smilodon()
    allg = unary_union(list(skel.values()))
    circ = minimum_bounding_circle(allg)
    cx, cy = circ.centroid.x, circ.centroid.y
    scale = SKEL_FIELD_R / minimum_bounding_radius(allg)
    for h, g in sorted(skel.items()):
        g = affinity.translate(g, -cx, -cy)
        g = affinity.scale(g, scale, scale, origin=(0, 0))
        layers.append((g, BASE + h))
    info = dict(skeleton_scale=scale, legend_tracking=trk, legend_cap=cap)
    return layers, info


def rim_profile():
    """Perfil (r, z) del disco + borde, para revolucionar."""
    return [(0, 0), (R - CHAMFER_BOTTOM, 0), (R, CHAMFER_BOTTOM), (R, RIM_TOP - RIM_BEVEL),
            (R - RIM_BEVEL, RIM_TOP), (RIM_IN + RIM_BEVEL, RIM_TOP), (RIM_IN, RIM_TOP - RIM_BEVEL),
            (RIM_IN, BASE), (0, BASE)]


# ---------------------------------------------------------------- malla
def to_cross_section(geom):
    rings = []
    for p in getattr(geom, "geoms", [geom]):
        if p.is_empty:
            continue
        rings.append(np.asarray(p.exterior.coords)[:-1])
        rings += [np.asarray(i.coords)[:-1] for i in p.interiors]
    return CrossSection(rings, FillRule.EvenOdd)


def build_mesh(layers):
    body = Manifold.revolve(CrossSection([np.array(rim_profile(), float)]), 360)
    eps = 0.05
    for geom, ztop in layers:
        geom = geom.simplify(0.01)
        solid = to_cross_section(geom).extrude(ztop - BASE + eps).translate((0, 0, BASE - eps))
        body = body + solid
    m = body.to_mesh()
    tm = trimesh.Trimesh(vertices=m.vert_properties[:, :3], faces=m.tri_verts, process=True)
    return tm


# ---------------------------------------------------------------- render
def heightmap(layers, px=0.04, margin=6.0):
    n = int(round((DIAM + 2 * margin) / px))
    off = n / 2

    def to_px(coords):
        c = np.asarray(coords)
        return [(off + x / px, off - y / px) for x, y in c]

    yy, xx = np.mgrid[0:n, 0:n]
    rr = np.hypot((xx + 0.5 - off) * px, (yy + 0.5 - off) * px)
    prof = np.array(rim_profile())
    h = np.interp(rr, prof[1:-1, 0][::-1] if False else [0, RIM_IN - 1e-6, RIM_IN, RIM_IN + RIM_BEVEL,
                                                          R - RIM_BEVEL, R],
                  [BASE, BASE, RIM_TOP - RIM_BEVEL, RIM_TOP, RIM_TOP, RIM_TOP - RIM_BEVEL])
    inside = rr <= R
    h = np.where(inside, h, 0.0)

    for geom, ztop in sorted(layers, key=lambda t: t[1]):
        img = Image.new("L", (n, n), 0)
        d = ImageDraw.Draw(img)
        for p in getattr(geom, "geoms", [geom]):
            d.polygon(to_px(p.exterior.coords), fill=255)
            for i in p.interiors:
                d.polygon(to_px(i.coords), fill=0)
        mask = np.asarray(img) > 127
        h = np.where(mask, np.maximum(h, ztop), h)
    return h, inside, px


def render(h, inside, px, path, out_px=1600):
    n = h.shape[0]
    hs = ndimage.gaussian_filter(h, 1.2)  # micro-bisel: aristas nítidas pero no aliased
    gy, gx = np.gradient(hs, px)
    nrm = np.dstack([-gx, gy, np.ones_like(h)])  # y de imagen hacia abajo
    nrm /= np.linalg.norm(nrm, axis=2, keepdims=True)

    def light(az, el):
        a, e = math.radians(az), math.radians(el)
        return np.array([math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])

    key = light(135, 38)   # luz principal arriba-izquierda
    fill = light(-30, 55)
    diff_k = np.clip(nrm @ key, 0, 1)
    diff_f = np.clip(nrm @ fill, 0, 1)

    # sombras proyectadas por marcha de rayos sobre el mapa de alturas
    step = 1  # píxel en diagonal
    tan_e = math.tan(math.radians(38))
    lit = np.ones_like(h)
    rise = step * math.sqrt(2) * px * tan_e
    shifted = h.copy()
    for k in range(1, int(4.0 / rise) + 2):
        shifted = np.roll(np.roll(h, k, axis=0), k, axis=1)  # muestra hacia arriba-izquierda
        lit = np.minimum(lit, np.clip(1 - (shifted - h - k * rise) / 0.08, 0, 1))
    lit = ndimage.gaussian_filter(lit, 3.0)  # sombras suaves

    # oclusión ambiental aproximada
    ao = np.clip(1 - 0.55 * np.clip(ndimage.gaussian_filter(h, 18) - h, 0, None), 0.35, 1)
    ao *= np.clip(1 - 0.35 * np.clip(ndimage.gaussian_filter(h, 5) - h, 0, None), 0.5, 1)

    albedo = 0.60  # PLA gris
    spec = np.clip(nrm @ ((key + np.array([0, 0, 1])) / np.linalg.norm(key + [0, 0, 1])), 0, 1) ** 24
    shade = albedo * (0.80 * diff_k * lit + 0.22 * diff_f + 0.20 * ao) + 0.04 * spec * lit
    shade *= 0.85 + 0.15 * ao
    col = np.dstack([shade * 1.00, shade * 1.00, shade * 1.02])

    # fondo neutro con degradé y sombra de contacto del medallón
    yy, xx = np.mgrid[0:n, 0:n] / n
    bg = 0.90 - 0.10 * np.hypot(xx - 0.4, yy - 0.35)
    m = inside.astype(float)
    drop = ndimage.gaussian_filter(np.roll(np.roll(m, 22, 0), 26, 1), 28)
    bg = bg * (1 - 0.40 * drop)
    bgc = np.dstack([bg, bg * 0.995, bg * 0.985])
    alpha = ndimage.gaussian_filter(m, 0.8)[..., None]
    img = np.clip(col * alpha + bgc * (1 - alpha), 0, 1) ** (1 / 1.15)
    Image.fromarray((img * 255).astype(np.uint8)).resize((out_px, out_px), Image.LANCZOS).save(path)


# ---------------------------------------------------------------- main
def main():
    layers, info = build_layers()
    mesh = build_mesh(layers)
    stl = OUT / "medallon_smilodon.stl"
    mesh.export(stl)
    print(f"STL: {stl.name}  watertight={mesh.is_watertight}  tris={len(mesh.faces)}  "
          f"bbox={np.round(mesh.extents, 2)} mm  vol={mesh.volume / 1000:.1f} cm³")
    print(info)
    h, inside, px = heightmap(layers)
    render(h, inside, px, OUT / "render_frontal.png")
    print("render: render_frontal.png")


if __name__ == "__main__":
    main()
