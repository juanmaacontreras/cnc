# Medallas de patrulla – cómo imprimir

Archivo: **`placa_6_medallas.3mf`**. Tiene las 6 medallas (Chita, Cóndor, Tigre, Pantera,
Zorro, Lobo) ya acomodadas en una cama de 256 × 256 mm. También están los STL sueltos.

## Configuración recomendada (PLA, boquilla 0,4)
| Parámetro | Valor |
|---|---|
| Altura de capa | **0,20 mm** (primera capa también 0,20) |
| Paredes | 3 |
| Capas superiores / inferiores | 5 / 4 |
| Relleno | 15 % giroide |
| Soportes | No |
| Brim | No (si se levanta una esquina, brim de 3 mm) |
| Velocidad | perfil "Standard" del slicer |
| Orientación | cara plana sobre la cama, tal como viene |

## Cambio de color en Elegoo Centauri Carbon 2 + CANVAS (ElegooSlicer)
Un solo cambio de filamento para las 6 medallas:
1. Abrí `placa_6_medallas.3mf`, elegí la impresora **Centauri Carbon 2** y cargá dos
   filamentos: **1 = negro** y **2 = blanco**, que coincidan con las ranuras del CANVAS.
2. Dejá todas las medallas en el filamento 1 (negro) y laminá.
3. En la barra vertical de capas, a la derecha, subí hasta la capa que dice **3.20**
   (la primera por encima de 3,0 mm). Hacé clic derecho o tocá el **+** y elegí
   **Cambiar filamento → Filamento 2 (blanco)**.
4. Volvé a laminar y revisá en la vista previa que el esqueleto, los textos y el borde
   salgan blancos y el fondo negro.
5. Si el slicer agrega una torre de purga, movela adelante o atrás de las medallas.
   Hay unos 33 mm libres en cada lado.

Sin CANVAS: en el paso 3 elegí **Agregar pausa** y cambiá el filamento a mano.

Material aproximado: unos 85 g en total (~70 g negro, ~15 g blanco). El slicer da el valor exacto.
