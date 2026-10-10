# Medallas de patrulla – cómo imprimir

Archivo: **`placa_6_medallas.3mf`**. Tiene las 6 medallas (Chita, Cóndor, Tigre, Pantera,
Zorro, Lobo) ya acomodadas en una cama de 256 × 256 mm. También están los STL sueltos.

## Configuración recomendada – Centauri Carbon 2, PLA, boquilla 0,4 (ElegooSlicer)
Partí del perfil **0.20mm Standard @Elegoo CC2** y cambiá solo esto:

### Calidad
| Parámetro | Valor | Por qué |
|---|---|---|
| Altura de capa / primera capa | 0,20 / 0,20 mm | el cambio de color cae justo en 3,0 mm |
| Generador de paredes | Arachne | letras y huesos más prolijos |
| Orden de paredes | Interior/Exterior/Interior | bordes nítidos sin perder adherencia |
| Costura | Alineada | |
| Compensación pata de elefante | 0,15 mm | |
| Patrón superior | Monotónico | |

### Planchado (ironing)
| Parámetro | Valor |
|---|---|
| Tipo de planchado | **Superficies superiores** (no "solo la superior", porque hay caras a varias alturas) |
| Patrón | Rectilíneo |
| Flujo | 10 % |
| Espaciado | 0,12 mm |
| Velocidad | 30 mm/s |
| Margen (inset) | 0,2 mm (no aplasta los bordes de las letras) |

El fondo negro se plancha en la última capa negra, antes del cambio, y las caras blancas se planchan al final de cada relieve.

### Resistencia
| Parámetro | Valor |
|---|---|
| Paredes | 3 |
| Capas superiores / inferiores | 5 / 4 |
| Relleno | 15 % giroide |
| Soportes | No |
| Brim | No (si una esquina se levanta, brim exterior de 3 mm) |

### Velocidad
| Parámetro | Valor |
|---|---|
| Pared exterior | 100 mm/s |
| Superficie superior | 80 mm/s |
| Primera capa | 40 mm/s |
| El resto | lo que trae el perfil |

### Filamento (PLA, igual para negro y blanco)
| Parámetro | Valor |
|---|---|
| Boquilla | 215 °C (primera capa 220 °C) |
| Cama | 55 °C (primera capa 60 °C) |
| Ventilador de capa | 100 % desde la capa 3 |
| Ratio de flujo | el que tengas calibrado (si no, 0,98) |
| Purga negro → blanco | **subila a ~600 mm³** (en Volúmenes de purga). Es un solo cambio y evita que la primera capa blanca salga grisácea |

### Antes de imprimir
- Limpiá la placa PEI con agua y detergente: es lo que más riesgo saca.
- Con PLA en impresora cerrada, dejá la tapa superior levantada o la puerta entreabierta para que no haya obstrucción por calor.
- Revisá en la vista previa: el fondo negro, desde la capa 3.20 todo blanco, y el planchado en verde/azul sobre las caras superiores.

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
