# Medallas Smilodon 2026: mismo contenido, diseño nuevo

Hola. Necesito que me ayudes a diseñar y generar el modelo 3D de 6 medallas para mi impresora 3D. Abajo tenés todo el contexto.

- El CONTENIDO ya está definido y es obligatorio.
- El DISEÑO visual es libre y quiero que sea distinto del de una versión que ya hice.

Leé todo antes de arrancar. Si falta algo importante, preguntame en vez de suponer. No inventes datos de mi impresora ni de mi configuración.

---

## 1. Tu rol y cómo trabajar conmigo

- Trabajá como diseñador/a de medallas y monedas en bajorrelieve y como experto/a en impresión 3D FDM a dos colores.
- Quiero que queden lo más lindas posible y con el menor riesgo de falla.
- Si una idea estética choca con una restricción de impresión, gana la impresión. Avisame y proponé una alternativa.
- Si algo obligatorio choca con una restricción técnica (por ejemplo, la leyenda no entra con el tamaño mínimo de letra), avisame y dame opciones. No lo resuelvas en silencio.
- Si una restricción te parece equivocada, decímelo y explicá por qué, pero no la ignores.
- Hablame en español rioplatense, claro y sin relleno. Si usás un término técnico, explicalo en una línea.
- No digas que probaste o verificaste algo que no corriste. Tampoco digas que lo probaste en el slicer, porque no tenés cómo.

## 2. Contexto

- Son medallas conmemorativas para 6 patrullas (scouts o similar) del Museo de Ciencias Naturales de La Plata, año 2026.
- Las 6 son iguales salvo el nombre de la patrulla.
- Se imprimen las 6 juntas, en una sola cama, a dos colores (base negra y relieves blancos), con un solo cambio de filamento.

## 3. Contenido OBLIGATORIO

1. Medallón redondo en bajorrelieve, optimizado para FDM: geometría simplificada, superficies elevadas gruesas y limpias, nada fino ni frágil.
2. Borde exterior circular, grueso y elevado.
3. En el centro, una silueta estilizada y con poco detalle del ESQUELETO de un tigre dientes de sable (Smilodon).
   - Tiene que leerse como esqueleto, no como el animal con piel.
   - Sin costillas finas ni huesos delgados.
   - El colmillo de sable se tiene que reconocer a simple vista.
4. Texto en relieve, en tipografía sans-serif bold, a lo largo del borde superior. Tiene que decir exactamente `MUSEO DE CS. NATURALES DE LA PLATA`: en mayúsculas, con punto en "CS.", 34 caracteres contando los espacios.
   - Va centrada arriba y sigue el borde. El ángulo que ocupa es libre (puede bajar por los costados), siempre que deje lugar abajo para "2026" y no choque con el colgado.
   - Una cartela recta o una banda horizontal no cumple.
5. Centrado abajo: `2026`.
6. El nombre de la patrulla en relieve, uno por medalla: `CHITA`, `CÓNDOR`, `TIGRE`, `PANTERA`, `ZORRO`, `LOBO`.
   - CÓNDOR lleva tilde también en mayúscula (Ó).
   - La altura de letra es la misma en las 6.
   - El diseño tiene que funcionar con el nombre más ancho y con el más alto (la tilde suma altura). Medilos con la tipografía que elijas, no cuentes letras.
7. Se tiene que poder colgar. El tipo de colgado está por confirmar (ver §10, paso 0).
8. Dos colores: base NEGRA y relieves BLANCOS. El borde, la leyenda, el año, el nombre y el esqueleto salen blancos. Hay un solo cambio de filamento, por altura (ver §8).
9. Las 6 van juntas en una sola cama, con la torre de purga (ver §9). No me propongas imprimir en tandas (4 + 2, dos impresiones, etc.).
10. No agregues textos, logos ni símbolos con significado (por ejemplo, emblemas scout) sin consultarme. Los ornamentos abstractos sí se pueden usar.

## 4. Lo que es LIBRE (acá quiero que propongas)

- **Composición y jerarquía:** el tamaño del esqueleto respecto del resto, dónde y cómo va el nombre, el uso del espacio negativo.
- **Pose, encuadre y estilo del esqueleto:**
  - De perfil vale, porque es donde mejor se ve el sable, pero con otra pose: rugiendo, saltando, sentado, mirando a la izquierda, etc. La única que no va es la de la versión anterior, "caminando hacia la derecha".
  - También puede ir de 3/4 o de frente, siempre que el sable se reconozca.
  - Estilo: geométrico, tipo grabado, art déco, heráldico, de insignia, etc. Siempre simple y robusto.
  - Si proponés solo el cráneo o un busto, marcalo como desvío del pedido.
  - Basate en esqueletos reales de Smilodon: colmillos superiores muy largos y aplanados, mandíbula que abre mucho, cuello y patas delanteras robustos, cola corta. Que no parezca un gato genérico.
- **Tipografía:** la leyenda va en sans-serif bold. Preferí sans-serif bold también para el nombre y el año; si proponés otra, marcala como opción. Tiene que ser libre, fácil de instalar y tener el glifo Ó. El interletrado, los separadores y los ornamentos también los elegís vos.
- **Borde:** perfil y ancho a elección (plano, escalonado, biselado, doble anillo, gráfila tipo moneda, etc.). Por fuera, siempre circular.
- **Forma de colgar:** oreja, agujero dentro del borde, argolla integrada, etc. Si el agujero va arriba, explicá cómo convive con la leyenda (cortarla en dos, correr el colgado, etc.).
- **Medidas:** diámetro, espesores y cantidad de niveles de relieve, dentro de §7 a §9.
- **Recursos de dos colores:** calados, esténcil, etc., para ornamentos y detalles del esqueleto, respetando las reglas de contraste de §8. Los textos obligatorios van en relieve blanco: calarlos es un desvío y solo va como alternativa marcada.

## 5. Versión anterior (para alejarte de ella)

No la repliques ni me hagas "la misma con otra fuente".

**Aspecto (NO copiar):**
- Disco con borde elevado y biselado, y oreja arriba con agujero.
- Leyenda en arco por arriba (236°), anillo interior separador y dos puntos separadores a los costados.
- "2026" recto abajo y nombre recto debajo del esqueleto.
- Esqueleto de perfil caminando hacia la derecha, en 5 niveles de relieve, todo blanco sobre fondo negro.

**Datos técnicos (sirven de escala y de punto de partida, no son requisitos):**
- Ø80 mm. Base de 3,0 mm, toda negra. Cambio de color a Z = 3,0 mm.
- Borde hasta 5,6 mm con bisel. Chaflán inferior de 0,6 mm.
- Oreja de 4,6 mm de alto, 1 mm más baja que el borde (ver §7, "Malla"), con agujero de Ø5 mm y 4 mm de material alrededor. Medida total: 80 × 91,5 mm.
- Niveles del esqueleto: 0,8 / 1,2 / 1,6 / 2,0 / 2,2 mm sobre el fondo. Ojo: el nivel de 0,8 mm no cumple el mínimo de blanco de §8. No lo repitas.
- Placa: 3 columnas × 2 filas, con la fila de abajo girada 180° (orejas hacia afuera), 4 mm entre medallas y 4 mm al borde de la cama. Ocupaba X 4–252, Y 34,5–221,5.
- Torre de purga atrás, con wipe_tower_x = 148 y wipe_tower_y = 229, a 11,8 mm de la medalla más cercana.
- Nada de esta versión está validado en impresión. Lo único probado es el cartel de §6.

## 6. Impresora, slicer y configuración probada (datos reales: no los cambies)

**Impresora**
- Elegoo Centauri Carbon 2 (CC2) con CANVAS: 4 bobinas con cambio automático de filamento.
- **Purga:** la impresora purga por su cuenta, fuera de la torre (en el perfil, purge_in_prime_tower = 0).
  - Al pasar de negro a blanco purga entre 667 y 900 mm³. Por eso conviene un solo cambio para las 6 medallas.
  - La torre de purga viene activada por defecto, pero es chica: 35 mm de ancho, y con su brim ocupa unos 42 mm en X × 16 mm en Y.
  - No la agrandes ni me propongas cambiar la purga.
- Volumen de impresión: 256 × 256 × 256 mm. Boquilla: 0,4 mm. Placa: PEI texturada (Textured PEI Plate).
- Coordenadas de la cama: (0, 0) es la esquina delantera izquierda, X crece hacia la derecha e Y hacia atrás.
- **Zona excluida:** X 246–256, Y 0–20 (esquina delantera derecha). No puede haber nada ahí: ni medallas, ni torre, ni brim.
- Antes de cada impresión, la CC2 mide la cama más o menos en X 10–243 / Y 10–245.

**Slicer y material**
- ElegooSlicer 1.3.2.1 (basado en OrcaSlicer).
- Proceso: "0.20mm Standard @Elegoo CC2 0.4 nozzle" (capa de 0,2 mm y primera capa de 0,2 mm).
- Filamento: "Elegoo PLA @ECC2" (boquilla a 210 °C, cama a 60 °C).
- Tengo PLA blanco, gris y negro. Uso negro (ranura 1 del CANVAS) y blanco (ranura 2). No uses el gris sin preguntarme.

**Configuración PROBADA**
Me funcionó con un cartel bicolor negro/blanco de unos 98 × 122 mm y 6 mm de alto:
- capa de 0,2 mm, 2 paredes, generador de paredes **classic** (no Arachne), sin detección de paredes finas, ancho de línea 0,42 mm (paredes internas 0,45);
- brim automático con brim_width = 5 mm y separación de 0,1 mm (en modo automático puede poner menos o nada: tomá 5 mm como peor caso);
- torre de purga activada (35 mm de ancho, con brim de 3 mm);
- primera capa a 50 mm/s (relleno de la primera capa a 105 mm/s), compensación de pata de elefante 0,1 mm;
- cama a 60 °C, sin planchado;
- cancelar objetos sueltos desactivado (exclude_object = 0).

Consecuencia importante del generador classic: lo que mide menos de ≈ 0,42 mm no se imprime, y lo que mide entre ≈ 0,42 y 0,84 mm sale con un solo perímetro y queda empastado. Apuntá a trazos de **≥ 0,85 mm** (dos líneas). Si algo no llega, el único cambio opcional que podés proponer es pasar a Arachne.

La idea es usar ESA configuración y solo sumarle el cambio de color. Opcionalmente, el planchado (ironing) de las caras superiores, que me interesa. No me propongas cambiar otros parámetros salvo que haya un motivo concreto. En ese caso, marcalo como opcional y proponé un cambio por vez.

**Cómo hago el cambio de color en ElegooSlicer (ya lo sé hacer)**
1. Cargo 2 filamentos: 1 = negro y 2 = blanco.
2. Dejo todos los objetos en el filamento 1 y lamino.
3. En la barra vertical de capas voy a la capa que muestra Z_cambio + 0,2. Por ejemplo, para un cambio a 3,0 mm es la que muestra 3.20, o sea la capa 16.
4. Clic derecho o "+" → Cambiar filamento → Filamento 2.
5. Vuelvo a laminar.

**Lo que falló**
En los intentos anteriores, las primeras líneas se despegaban de la cama. Creo que fue porque no había lavado la placa, pero no estoy 100 % seguro.

## 7. Restricciones de geometría

**Orientación y base**
- Se imprime acostada, con la cara de abajo plana en Z = 0 y sin soportes.
- Nada que necesite soporte (voladizos de más de ~45°). Para colgar, lo más simple es un agujero vertical, que atraviese la medalla en Z.
- Se permite un chaflán inferior chico (la anterior tenía 0,6 mm) contra la "pata de elefante", siempre que no achique mucho la superficie de apoyo. Tené en cuenta que el perfil ya compensa 0,1 mm en la primera capa.
- Todas las medidas en mm.

**Alturas**
- TODAS las caras superiores HORIZONTALES (fondo, borde, cada nivel de relieve y el colgado) tienen que estar a alturas múltiplos exactos de 0,2 mm, medidas desde Z = 0. Nada de 0,9 ni de 1,25.
- Los biseles y las curvas (caras inclinadas) no tienen una sola Z: se permiten, salen escalonados cada 0,2 mm, y se controlan aparte con su rango de Z y la regla de color de §8.

**Anchos mínimos (medidos en planta, en cada nivel)**

| Elemento | Mínimo | Objetivo |
|---|---|---|
| Huesos y trazos de relieve (esqueleto, ornamentos, borde) | 0,9 mm | ≥ 1,0 mm |
| Trazo de letra en relieve | 0,7 mm | ≥ 0,85 mm (ver generador classic en §6) |
| Altura de la mayúscula | 4,0 mm | — |
| Punto de "CS." y tilde de la Ó (islas sueltas) | ≈ 0,8 mm de tamaño (agrandarlos a mano si hace falta) | separados ≥ 0,8 mm de la letra (mínimo 0,5) |
| Hueco entre elementos blancos | 0,5 mm (mínimo absoluto) | ≥ 0,8 mm donde se tenga que ver el negro, incluidas las contraformas de A, O, Ó, D, R y P y el 0 y el 6 de "2026" |
| Trazo hundido o calado hasta el negro (esténcil) | 0,8 mm | ≥ 1,0 mm |
| Agujero para colgar | referencia de la anterior: Ø5 mm con 4 mm de material alrededor | depende del colgado |

Las puntas (colmillo, garras, cola) tienen que terminar redondeadas o truncadas, sin bajar del mínimo. El sable tiene que ser grueso desde el diseño.

**Ojo con la tipografía**
Estos datos son orientativos, medidos con Liberation Sans Bold. Si usás otra fuente, medí la tuya.
- **Trazos:** con mayúsculas de 4,0 mm, las barras horizontales (de la E o la H) miden ≈ 0,65–0,69 mm y no llegan a 0,7. Hacen falta mayúsculas de ≈ 4,4–4,5 mm o engrosar el texto (offset de ≈ +0,03 a +0,05 mm).
- **Largo de la leyenda:** mide ≈ 30 veces la altura de la mayúscula, sobre la línea de base. Da ≈ 120 mm con mayúsculas de 4,0 mm y ≈ 135 mm con 4,5 mm.
  - Con 4,5 mm, un borde de 3 mm y 0,8 mm de separación, la leyenda ocupa ≈ 245° con Ø80, ≈ 265° con Ø75 y ≈ 280° con Ø72: forzosamente baja por los costados.
  - Probablemente sea la restricción más ajustada del diseño. Calculala desde el primer concepto, sobre todo si achicás el diámetro.
  - Si no entra, considerá una sans bold condensada (verificando sus trazos) o un arco más largo.
- **Punto de "CS.":** mide ≈ 0,21 veces la altura de la mayúscula (≈ 0,82 mm con 4 mm, ≈ 0,92 mm con 4,5 mm). Si querés que llegue a 1 mm, agrandalo o engrosalo a mano.
- **Tilde de la Ó:** queda a ≈ 0,07 veces la altura de la mayúscula por encima de la O (≈ 0,28 mm con mayúsculas de 4 mm). En su parte más gruesa mide ≈ 0,13 veces esa altura (≈ 0,5 mm con 4 mm) y en las puntas, menos.
  - Para que CÓNDOR cumpla hueco ≥ 0,5 y trazo ≥ 0,7 con la fuente tal como viene, el nombre necesita mayúsculas de ≈ 7 mm o más. Si no, dibujá o separá la tilde a mano.
  - Reservá también su altura: la tilde suma ≈ 29 % a la altura del nombre.
- **OpenSCAD:** el parámetro `size` de `text()` no es la altura de la mayúscula. Medila.

**Malla**
- Cada medalla tiene que ser un solo sólido cerrado (watertight y manifold): sin aristas no-manifold, sin autointersecciones, sin caras internas, con normales consistentes y volumen positivo.
- Usá operaciones booleanas reales (OpenSCAD, manifold3d, CadQuery, etc.), no juntes mallas sueltas.
- Evitá que dos sólidos se toquen solo por una cara o una arista coplanar: que se superpongan con volumen o que queden a alturas distintas.
  - En la versión anterior, la unión entre la oreja y el borde generó aristas no-manifold. Se resolvió dejando la oreja 1 mm más baja que el borde.
- En las restas, el cuerpo que corta tiene que sobresalir un poco de las caras que atraviesa.

## 8. Color por altura (un solo cambio)

**Reglas**
- Todo lo que está por debajo de Z_cambio sale negro (filamento 1) y todo lo que está por encima sale blanco (filamento 2).
- Z_cambio lo elegís vos. Tiene que ser múltiplo de 0,2 y el mismo para las 6 medallas.
- Nada de pintar colores por zona ni de asignar filamento por objeto o por parte: eso multiplica los cambios de filamento y la purga.
- Lo más prolijo es que la cara superior del fondo coincida con Z_cambio. En la anterior era 3,0 mm.
- **Blanco suficiente:** toda cara hacia arriba que esté por encima de Z_cambio tiene que estar a Z_cambio + 1,0 mm o más (5 capas), y mejor a + 1,2 mm (6 capas). Con menos, el blanco no tapa al negro y se ve grisáceo.
- **Superficies inclinadas:** ninguna superficie visible (bisel, redondeo) debería quedar entre Z_cambio y Z_cambio + 1,0. Ahí aparece una banda gris o se ve la línea del cambio. Si lo hacés a propósito, mostrámelo.
- **Costados:** el canto exterior de la medalla queda negro abajo y blanco arriba. Diseñá contando con eso y mostralo en la previsualización.

**Contraste (importante para el diseño)**
- El blanco solo se lee contra el negro que queda a la vista, o sea, en zonas a la altura de Z_cambio o más abajo.
- Un hueco o grabado dentro de un elemento blanco que no baje hasta Z_cambio sigue saliendo blanco: es blanco sobre blanco y casi no se lee. Por ejemplo, letras grabadas en un borde blanco.
- Un hueco que baja hasta Z_cambio o más (calado tipo esténcil) deja ver el negro y sí da contraste.
- El texto en relieve sobre una banda blanca es blanco sobre blanco: solo se lee por la sombra. La leyenda, el año, el nombre y el esqueleto tienen que tener fondo negro a la vista alrededor.
- Los detalles hundidos en la base negra, o los relieves negros por debajo de Z_cambio, son negro sobre negro: casi no tienen contraste. Usalos solo como textura o decoración secundaria, nunca para el contenido obligatorio.

## 9. Placa con las 6 medallas y la torre

**Qué tiene que entrar**
- Las 6 medallas en la cama de 256 × 256, sin pisar la zona excluida, más la torre de purga (≈ 42 × 16 mm con brim).
- En el código de la placa, modelá la torre como un rectángulo reservado que no se exporta. Así podés medir distancias contra él.

**Separaciones**
- La torre y las medallas no se pueden tocar, contando el brim de las dos. Medí y reportá la distancia geométrica real, no la distancia entre cajas envolventes. Como referencia, en la anterior quedó a 11,8 mm.
- **Brim automático:** el perfil tiene brim_width = 5 mm. Tomalo como peor caso por lado. Si una medalla queda pegada al borde, el brim se puede salir de la cama.
- La separación entre medallas es libre (en la anterior era de 4 mm).

**Compromiso de tamaño (cuantificalo)**
- Con Ø80 en 3 columnas, el ancho es 3 × 80 + 2 × 4 = 248 mm.
  - Entra en la cama, pero queda a 4 mm del borde y fuera de la zona que mide la impresora en X (X 10–243 son 233 mm).
  - En Y sobra lugar: la anterior ocupaba Y 34,5–221,5.
- Para entrar en la zona medida con 3 columnas y 4 mm entre medallas hace falta un diámetro de ≈ 75 mm sin brim, o ≈ 71 mm o menos con el brim de 5 mm. Eso aprieta la leyenda (ver §7).
- Otra opción es cambiar la distribución: 2 columnas × 3 filas, filas desfasadas, medallas rotadas, torre al costado, etc.
- No sé si quedar fuera de la zona medida influyó en el despegue; yo creo que fue la cama sucia. Evaluá el compromiso con números y recomendame una opción.
- La distribución es libre. Podés rotar medallas para acomodar el colgado.

**Coordenadas**
ElegooSlicer puede re-centrar en la cama lo que importás, así que no des por sentado que respeta tus coordenadas. Si se puede, que la caja envolvente de las 6 quede centrada en (128, 128). Dame una tabla con:
- el centro de la caja envolvente de cada medalla y del conjunto de las 6. Es lo que muestra el panel de posición del objeto. Si hay oreja, no coincide con el centro del disco.
- la posición de la torre como valores wipe_tower_x / wipe_tower_y del slicer, y su huella. Ojo: (x, y) NO es la esquina de la huella con brim. En mi cartel, con (x, y) la torre con brim ocupó aprox. X x−3,5…x+38,5 e Y y−6…y+9,5. En la versión anterior, (148, 229) daba X 144,5–186,5 / Y 223–238,5, y de ahí salen los 11,8 mm. Modelá el rectángulo reservado así. Igual lo verifico en la vista previa del slicer.

## 10. Cómo vamos a trabajar

**Paso 0. Capacidades y preguntas (es lo único de tu primera respuesta)**
- En una o dos líneas, contame:
  - si podés ejecutar código y con qué librerías (manifold3d, trimesh, shapely, CadQuery, build123d, OpenSCAD);
  - si tenés internet para instalar cosas;
  - si podés entregar archivos descargables y generar imágenes.

  Según eso, seguí el camino A o el B de §11.
- Hacé solo las preguntas imprescindibles, todas juntas. Las que sé que faltan:
  - ¿Se cuelga con cordón, cadenita o argolla, o con cinta ancha? Si es cinta, preguntame el ancho, porque en vez de agujero va una ranura.
  - Solo si me vas a dar código OpenSCAD para que lo corra yo: mi sistema operativo, si tengo OpenSCAD instalado y qué versión.
- No me preguntes lo que ya está definido acá. Si no te contesto algo, usá un valor razonable y decime cuál.

**Paso 1. Conceptos (todavía sin el modelo final)**
Proponé 2 o 3 conceptos bien distintos entre sí y distintos de la versión anterior. Para cada uno, en pocas líneas:
- nombre, la idea en 2 o 3 líneas y por qué funciona visualmente;
- un boceto: imagen o SVG si podés; si no, un croquis ASCII o una descripción precisa;
- tipografía concreta, pose y estilo del esqueleto, borde y forma de colgar;
- diámetro aproximado y cómo entran las 6 más la torre, en una línea;
- el principal riesgo de impresión y cómo lo evitás.

Para el que recomiendes, sumá:
- una tabla de alturas: elemento → Z de la cara superior → color;
- la cuenta de la leyenda: su largo contra el arco disponible;
- la distribución de la placa, con números.

Recomendame uno y ESPERÁ a que elija. Puede que te pida mezclar conceptos.

**Paso 2. Una medalla primero**
Con el concepto elegido, hacé primero CÓNDOR, que es la más difícil por la tilde. Comprobá también que entre el nombre más ancho. Mostrámela con la verificación de §13. En el camino B podés entregar directamente el archivo completo, pero decime qué revisar primero en CÓNDOR.

**Paso 3. Las 6 y la placa**
Recién ahí generá todo lo de §11.

**Cambios**
Si te pido cambios:
- en el camino A, aplicalos en el código y regenerá todo;
- en el camino B, mandame el archivo completo actualizado o las líneas exactas que tengo que reemplazar.

## 11. Entregables

**En los dos caminos**
1. **Código fuente paramétrico COMPLETO**, sin "..." ni partes omitidas.
   - Arriba de todo, todos los parámetros con comentarios: nombres, leyenda, año, diámetro, alturas, Z_cambio, anchos mínimos, colgado, tipografía y distribución de la placa.
   - Cambiar un nombre tiene que ser editar una sola línea.
   - Un selector para generar una medalla (por nombre o por índice) o la placa completa.
   - El esqueleto va dibujado dentro del código (polígonos, hull de círculos, etc.) o en archivos que me entregues vos. No me pidas que dibuje ni que consiga nada.
   - Decime qué tipografía usaste, su licencia y cómo instalarla.
   - Textos en UTF-8, con la Ó como un único carácter (U+00D3, forma NFC), no como una "O" más una tilde combinante. Comprobá que la fuente tenga ese glifo.
2. **Un STL por medalla**, en mm y con un solo sólido cada uno: `medalla_CHITA.stl`, `medalla_CONDOR.stl`, `medalla_TIGRE.stl`, `medalla_PANTERA.stl`, `medalla_ZORRO.stl` y `medalla_LOBO.stl`. El nombre del archivo va sin tilde, pero el texto del modelo lleva la Ó.
3. **La placa con las 6 acomodadas**, en coordenadas de cama (0–256):
   - un 3MF con 6 objetos separados y SOLO geometría;
   - un STL único con las 6, como respaldo;
   - la tabla de posiciones de §9.
4. **Previsualización:**
   - una bicolor, coloreada por altura tal como va a salir (negro por debajo de Z_cambio, blanco por encima);
   - una "CAD clay render" (gris mate, luz suave) en vista 3/4, un estilo que me gusta para previsualizar;
   - la placa vista desde arriba, con la torre marcada.
5. **Opcional:** un visor 3D (un HTML con three.js) para girar la medalla. Si no podés, decime cómo verla en 3D (por ejemplo, abriendo el STL en ElegooSlicer).
6. **Opcional:** una probeta chica (un pedazo de borde con texto y parte del esqueleto) para probar el cambio de color antes. La impresión final igual es la placa de 6.
7. Las instrucciones para el slicer (§12) y el informe de verificación (§13).

NO generes archivos de proyecto de ElegooSlicer/OrcaSlicer, ni 3MF con configuración adentro, ni perfiles, ni G-code. Ya se intentó: no se pudo verificar en el slicer y me generó desconfianza. Vos me das la geometría; la configuración la pongo yo con mi perfil probado.

**Camino A: si podés ejecutar código**
- Generá vos los archivos y las imágenes, desde el mismo código que me entregás.
- Si el código que me das (por ejemplo, un .scad) no es el que generó los STL, decilo. Explicá si son equivalentes y cómo lo comprobaste.
- Corré la verificación de §13 sobre los archivos finales exportados, no sobre el modelo intermedio.
- Si te faltan librerías y no las podés instalar, adaptá el método y decime qué chequeos no pudiste correr.
- Si podés, entregame todo en un ZIP.

**Camino B: si no podés ejecutar código**
Dame el código OpenSCAD completo. OpenSCAD es gratis (openscad.org). Que sea compatible con la versión que yo tenga; si usás funciones de versiones nuevas, avisame.

Sugerencias técnicas (si te parece mejor otra técnica, usala):
- **Vista previa bicolor (F5):** con `color()` y un corte en Z_cambio, solo dentro de `if ($preview)`. El STL exportado tiene que ser un único sólido. Si el corte queda en el camino de exportación, salen dos cuerpos pegados por una cara coplanar, justo lo que prohíbe §7.
- **Leyenda en arco:** ubicá las letras de a una y rotalas según el ancho aproximado de cada una (OpenSCAD 2021 no mide texto). Revisá el espaciado en la vista previa.
- **Partes demasiado finas del esqueleto:** podés limpiarlas con una "apertura" 2D: `offset(r=-a)` y después `offset(r=+a)`, con a = la mitad del ancho mínimo.
  - Ojo: redondea todas las puntas con radio a y puede acortar o borrar la punta del colmillo. Diseñá el sable grueso desde el principio o dejalo fuera de la apertura.
  - Para cerrar huecos de menos de 0,5 mm se usa el "cierre": `offset(r=+b)` y después `offset(r=-b)`.
- **Fuente:** Liberation Sans Bold viene con OpenSCAD y tiene la Ó. Si usás otra, decime cómo instalarla y el nombre exacto que va en `font=`. Guardá el archivo en UTF-8.

Instrucciones de exportación:
- F5 para la vista previa, F6 para renderizar y F7 (o Archivo → Exportar → STL) para exportar. Si uso Mac, decime los atajos equivalentes.
- Cómo sacar las 6 sin exportar a mano 6 veces: por línea de comandos, por ejemplo `openscad -o medalla_CONDOR.stl -D 'indice=1' medallas.scad`, con las comillas que correspondan a mi sistema.
- Cómo exportar la placa: como STL único. El 3MF con varios objetos depende de la versión.
- Si el render tarda demasiado (con el motor CGAL viejo puede tardar muchísimo con tanto texto), cómo activar el motor Manifold en una versión de desarrollo reciente.

En lugar de los renders y de la verificación automática:
- qué tengo que ver en la vista previa para saber que salió bien;
- qué tengo que revisar yo en OpenSCAD y en la vista previa del slicer.

## 12. Instrucciones para ElegooSlicer (cortas, con tu Z_cambio concreto)

1. **Antes de imprimir:** lavar la placa PEI con agua y detergente, secarla y no tocarla con los dedos. La boquilla tiene que estar limpia.
2. **Perfil:** usar el perfil probado de §6 y revisar que el tipo de placa sea Textured PEI.
3. **Importar:**
   - Importar el 3MF. Si pregunta si cargarlo como un solo objeto con varias partes, responder que no.
   - Si se usa el STL único, entra como un solo objeto. Hay que separarlo en objetos (decime el nombre exacto del menú si lo sabés).
   - No usar el acomodo automático. Comparar las posiciones con la tabla.
4. **Filamentos:** todos los objetos en el filamento 1.
5. **Torre:** dónde ubicarla y cómo (arrastrándola o con sus parámetros de posición).
6. **Cambio de color:** el procedimiento de §6, con la capa exacta: su número y la Z que muestra el slicer.
7. **Vista previa:** revisar que haya un solo cambio y que el blanco empiece donde corresponde. Que el brim quede dentro de la cama, no toque la torre y no tape el agujero de colgar. Si lo tapa, decime qué tipo de brim usar.
8. **Planchado:** decime si conviene para este diseño y en qué caras. Es opcional y no forma parte de la configuración probada.
9. **Si se despega:** si las primeras líneas se siguen despegando con la placa limpia, proponé UN solo cambio por vez, en orden de prioridad (por ejemplo, bajar el relleno de la primera capa, que hoy va a 105 mm/s). El resto de la configuración probada se mantiene.
10. **Excluir un objeto:** con mi perfil tal como está (exclude_object = 0) no se puede cancelar una sola medalla durante la impresión. No lo prometas; si te parece útil activarlo, proponelo como cambio opcional.

## 13. Verificación antes de entregar

Reportá cada punto como OK, FALLA o NO VERIFICADO, con el valor medido.
- **Camino A:** verificá con código sobre los archivos finales. Si algo falla, corregilo y volvé a correr todo.
- **Camino B:** decime cómo lo comprobaste o qué tengo que revisar yo.

**Contenido**
- [ ] Textos exactos en el código: `MUSEO DE CS. NATURALES DE LA PLATA`, `2026` y los 6 nombres. La Ó es U+00D3 y está en la fuente (no sale vacía ni como un cuadradito). Está el punto de "CS.". El STL no se puede leer como texto: esto se verifica en el código y mirando el render.
- [ ] Hay 6 archivos, cada uno con su nombre.
- [ ] Ancho y alto reales de los 6 nombres, medidos con la fuente elegida. El peor caso (el más ancho, y CÓNDOR con su tilde) entra sin tocar otros elementos, con la misma altura de letra en las 6.
- [ ] La leyenda sigue el borde superior y "2026" está centrado abajo.
- [ ] El colgado no choca con la leyenda.
- [ ] El colmillo de sable se reconoce en el render.

**Alturas y color**
- [ ] Lista de alturas de todas las caras HORIZONTALES hacia arriba: todas múltiplos de 0,2 (tolerancia 0,001). Z mínima = 0. Las caras inclinadas o curvas, aparte, con su rango de Z.
- [ ] Z_cambio es múltiplo de 0,2. Indicá la capa a marcar: número y Z que muestra el slicer.
- [ ] Toda cara hacia arriba que esté por encima de Z_cambio está a Z_cambio + 1,0 o más (ideal + 1,2).
- [ ] Ninguna superficie inclinada visible queda entre Z_cambio y Z_cambio + 1,0 (o está justificada).
- [ ] Borde, leyenda, nombre, año y esqueleto salen blancos y tienen negro a la vista alrededor (contraste de §8).

**Anchos (§7)**
- [ ] Medidos en cortes de la malla final justo debajo de cada altura de cara (Z = altura − 0,1), con el umbral que corresponde a cada tipo de elemento. Informá:
  - el hueso más fino;
  - el trazo de letra más fino;
  - la altura de mayúscula medida (no el `size`);
  - el punto de "CS." y la tilde;
  - el hueco más chico y las contraformas;
  - los trazos hundidos.
- [ ] Si usás tests morfológicos (apertura y cierre), declarás la tolerancia para no contar como falla el redondeo de las esquinas vivas (por ejemplo, ignorar restos de menos de 0,05 mm²). Si algo falla, decime dónde.

**Colgado e impresión**
- [ ] Agujero: su medida, el material alrededor y que atraviesa la medalla de lado a lado.
- [ ] Base plana en Z = 0, con chaflán chico si lo hay. No hay caras hacia abajo por encima de Z = 0, salvo las de ese chaflán. No hacen falta soportes.

**Malla**
- [ ] Cada medalla es un solo cuerpo: watertight, manifold, con normales consistentes, volumen > 0 y sin autointersecciones.

**Placa**
- [ ] Están las 6 medallas y la torre reservada (42 × 16 mm). Informá la caja de cada una y las distancias mínimas reales (con el brim asumido):
  - entre medallas;
  - entre cada medalla y la torre;
  - al borde de la cama;
  - a la zona excluida, que tiene que quedar vacía;
  - y si quedan dentro o fuera de la zona medida.
- [ ] Tabla de coordenadas de §9, con el aviso de que el slicer puede moverlas al importar.

**Entrega**
- [ ] Los renders salen de los archivos que entregás, no de una versión anterior.
- [ ] El código está completo. Si no lo pudiste ejecutar, decilo.
- [ ] Lista de lo que NO pudiste verificar y de lo que tengo que revisar yo.