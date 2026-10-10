# Medallas de patrulla – cómo imprimir (Elegoo Centauri Carbon 2 + CANVAS)

Abrí **`medallas_CC2_listo.3mf`** con ElegooSlicer (Archivo → Abrir proyecto). Trae:

- **La misma configuración de tu cartel Elegoo que salió bien** (impresora, proceso y
  filamentos, las 533 opciones tal cual, guardadas en `config_cartel_elegoo.json`).
  Lo único que cambia es la posición de la torre de purga, para que no choque con las medallas.
- **Torre de purga** activada, como en el cartel, atrás al centro (a 11,8 mm de la medalla más cercana).
- Dos filamentos Elegoo PLA: 1 = negro, 2 = blanco.
- Las 6 medallas (Chita, Cóndor, Tigre, Pantera, Zorro, Lobo) en la cama.
- **Cambio a blanco en la capa 3,20 mm**: todo lo que está por encima de 3 mm sale blanco.

## Antes de mandar
1. Si pregunta si cargar la configuración del proyecto, respondé que sí.
2. Filamento 1 = negro y 2 = blanco, igual que las ranuras del CANVAS.
3. Laminar y revisar la vista previa: negro hasta 3,20, blanco desde ahí, y la torre atrás.
   Si el cambio de color no aparece: clic derecho en la capa 3.20 → Cambiar filamento → 2.

Archivos sin configuración: `medallas_solo_modelo.3mf`, `placa_6_medallas.stl` y los STL sueltos.
