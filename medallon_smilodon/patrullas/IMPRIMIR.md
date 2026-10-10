# Medallas de patrulla – cómo imprimir (Elegoo Centauri Carbon 2 + CANVAS)

Primero imprimí **`prueba_1_medalla_CC2.3mf`** (una sola medalla, misma configuración). Si sale bien,
abrí **`medallas_CC2_listo.3mf`** con ElegooSlicer (Archivo → Abrir proyecto). Ya trae:

- Impresora **Centauri Carbon 2 0.4** y proceso **0.20mm Standard** con los ajustes de abajo.
- Dos filamentos **Elegoo PLA**: 1 = negro, 2 = blanco.
- Las 6 medallas (Chita, Cóndor, Tigre, Pantera, Zorro, Lobo) acomodadas en la cama.
- El **cambio a blanco en la capa 3.20 mm**: todo lo que está por encima de 3 mm
  (esqueleto, textos, anillo, borde y oreja) sale blanco; el fondo y la base, negros.

## Antes de mandar (1 minuto)
1. Si pregunta si cargar la configuración del proyecto, respondé que **sí**.
2. En los filamentos, que el 1 sea el negro y el 2 el blanco, igual que las ranuras del CANVAS.
3. Elegí el tipo de placa que tengas puesta (PEI texturada o lisa; la temperatura es la misma).
4. **Laminar** y mirar la vista previa: barra de capas abajo de 3.20 todo negro, desde 3.20
   todo blanco, y el planchado sobre las caras superiores.
   Si el cambio de color no aparece, agregalo a mano: clic derecho en la capa 3.20 de la
   barra de capas → Cambiar filamento → Filamento 2.

## Ajustes cargados (sobre 0.20mm Standard @Elegoo CC2)
| | Valor |
|---|---|
| Capa / primera capa | 0,20 / 0,20 mm (todas las alturas del diseño son múltiplos de 0,2) |
| Paredes | 3, generador Arachne, orden interior-exterior-interior |
| Capas superiores / inferiores | 5 / 4 |
| Relleno | 15 % giroide |
| Superficie superior | monotónico, 100 mm/s |
| **Planchado** | todas las caras superiores, flujo 10 %, separación 0,12 mm, 30 mm/s, margen 0,15 mm |
| Pared exterior | 100 mm/s, aceleración 3000 |
| Primera capa | paredes 35 mm/s, relleno 45 mm/s, cama 65 °C |
| Pata de elefante | 0 (la base ya tiene chaflán de 0,6 mm) |
| Evitar cruzar paredes | sí |
| Soportes / brim / falda | no / **brim de 3 mm** (sale con la uña) / no |
| Torre de purga | no (la CC2 purga el cambio de filamento por su cuenta) |
| Purga negro → blanco | 900 mm³ (valor de Elegoo para la CC2) |

## Filamento (perfil Elegoo PLA @ECC2, sin cambios)
Boquilla 210 °C, cama 65 °C en la primera capa y 60 °C después, ventilador 50–100 %, ratio de flujo 0,98, presión avance 0,04.

## Para que no falle
- Limpiá la placa con agua y detergente antes de imprimir.
- Tapa y puerta **cerradas**: la CC2 maneja su propio ventilador de cámara para PLA, y así no hay corrientes que levanten los bordes.
- Limpiá la punta de la boquilla si le quedó plástico de la impresión anterior.
- Material aproximado: unos 85 g (~70 g negro, ~15 g blanco). El slicer da el valor exacto.

## Regenerar
`armar_config_cc2.py` arma `cc2_project_settings.json` a partir de los perfiles oficiales de
ElegooSlicer; `generar_patrullas.py` genera las medallas y el proyecto.
