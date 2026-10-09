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

## Cambio de color (un solo cambio para las 6)
- PLA **negro** desde el inicio.
- Cambio a PLA **blanco** al terminar la capa que llega a **3,0 mm**: en la barra de capas
  del slicer elegí la capa que muestra **3,20 mm** (la primera capa por encima de 3,0)
  y agregá ahí el cambio de filamento o la pausa.
  - Con AMS: "Cambiar filamento" → blanco. Desactivá la torre de purga si no hace falta.
  - Sin AMS: "Agregar pausa" / "Color change (M600)" y cambiá el filamento a mano.
- Todo lo que queda por encima (esqueleto, textos, anillo, borde y oreja) sale blanco.

Material aproximado: unos 85 g en total (~70 g negro, ~15 g blanco). El slicer da el valor exacto.
