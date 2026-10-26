# Imágenes y material: catálogo para webs y piezas

Hay dos fuentes de imágenes. Las dos están en
`~/Downloads/03-Proyectos y clientes/Taufic Gashaan/` y **nunca se copian enteras
a un repo**. A un proyecto solo se llevan derivados optimizados en `public/`.

| Fuente | Ruta local | Qué es | Calidad |
|---|---|---|---|
| **Drive (originales)** | `Drive fotos proyectos/` (826 MB, 182 archivos) | Fotos de obra, renders, planos y textos por proyecto. Parece armado para una web anterior (2021-2023; hay una carpeta "FOTOS EMPLEADOS PAGINA", vacía) | Muchas son de cámara pro (5,000-9,600 px). Algunas son de celular (≤1,600 px) |
| **Libro (avance sept.)** | `Libro The Container Home II/imagenes-libro/<sección>/pNNN-MMM.jpg` (194 imágenes) | Las fotos tal como están maquetadas en el libro | **Baja: ~850 px de lado y 100 ppi.** Sirven para tarjetas, thumbs y referencia, no para héroes ni impresión |

- Drive original: https://drive.google.com/drive/folders/10NXHTbFCZiG9c5gTuqXpztqxNf6s0nwv
- Manifiesto por archivo (ruta, id de Drive, px, peso): [fuentes/manifest-drive.json](fuentes/manifest-drive.json)
- Índice del libro (sección, página PDF e impresa, px): [fuentes/indice-imagenes-libro.json](fuentes/indice-imagenes-libro.json).
  Nombre `pNNN-MMM.jpg` = página del PDF (la impresa es NNN−1) y número de imagen.
- Textos que venían en el Drive: [fuentes/drive-descripciones.md](fuentes/drive-descripciones.md)

## Reglas para usarlas en web

1. **Prioridad: Drive original > libro.** El libro solo se usa donde el Drive no
   tiene la obra (ver "Solo en el libro").
2. Hacer derivados: héroe a 2400 px y tarjetas a 1200 px, en JPG o WebP calidad
   ~80. Los originales de 20-36 MB nunca van a la web.
3. Varias fotos traen **HDR fuerte** (Colegio, Bugambilias, Lago, Palenque).
   Cuidarlas al lado de fotos naturales.
4. Las de **Casa Arrayán** tienen marca de agua "pacoG / animatoriumrex.com" (es el
   fotógrafo) y miden 400-800 px. No sirven para un héroe; preguntar el crédito.
5. Los nombres de carpeta del Drive traen espacios al inicio o al final, y hay
   archivos sin extensión. Al bajarlos se normalizaron: se quitaron los espacios,
   se añadió `.jpg` y los duplicados quedaron como `4 (2).jpg`.
6. Para generar thumbnails o collages **no usar ffmpeg con `-reinit_filter 0` y
   `format=rgb24`**: voltea unas imágenes. Los originales están bien orientados.

---

## Equivalencias de nombres: Drive ↔ libro

| Drive | Libro | Certeza |
|---|---|---|
| DEPARTAMENTO BOCA DE TOMATLAN | Departamento Móvil **El Mangle** | Alta: mismas fotos, 2 contenedores sobre pilotes, el río de Boca de Tomatlán |
| DEPARTAMENTO MISMALOYA | Departamento Móvil Mismaloya | Alta (el libro trae fotos distintas: mar, rocas, paneles solares) |
| OFICINAS YOGUI | **Oficina MVA** | Alta: mismas fotos (1 de 40' abajo + 2 de 20' arriba, deck con muro verde) |
| OFICINAS GE + OFICINAS SAYER | Oficinas móviles General Electric y Sayer Lack | Alta |
| HOSPITAL CULIACAN | "Proyecto Hospital con Torre" (Proyectos, sin maquetar) | Media: el render dice "HOSPITAL CENTRAL CULIACÁN" |
| CASA BUGAMBILIAS | "Casa Panorámica Bugambilias" (Proyectos, sin maquetar) | Media: en el Drive se ve terminada, no en render |
| BASIL DEL MAR | "Proyecto Basil del Mar" (Proyectos, sin maquetar) | Alta |
| DEPA MATUTE | Casa-contenedor exhibida **bajo el puente Matute Remus** (la que vieron los dueños de Casa Bosque) | Media: la foto 1 es un contenedor-tráiler bajo el puente |
| DEPARTAMENTO PLAYA BOSQUE (renders "CPM") | ¿"Cabaña Bosque Triángulo"? | Baja: preguntar |
| CASA PILAR | Casa El Pilar | Alta (la obra es de construcción convencional, lo que cuadra con los "0 contenedores" de la ficha) |

---

## Catálogo por proyecto

El número entre paréntesis es el lado mayor en px. ★ = candidata a héroe.

### Residencial (en el libro)

**Casa Bosque**: Drive `RESIDENCIAL/CASA BOSQUE/` (7 fotos, 5,700-6,700 px, pro).
1 ★ fachada nocturna en hora azul (es la **foto de portada del libro**) · 2 fachada
lateral al atardecer · 3 terraza de noche con jardín · 4 terraza y jardín con árbol ·
5 sala con muro de ladrillo · 6 comedor · 7 sala de TV. Libro: `Casa Bosque/` (12).

**Casa Cantalagua**: Drive (10 fotos, mezcla). `1.jpg` fachada de día con techo
mariposa (4,608 panorámica) ★ · `2.jpg` fachada lateral · `3.jpg` fachada frontal con
estructura en V · `4.jpg`/`4 (2).jpg` (una de 4,608 y otra de 1,024) · `5-8.jpg`
recámaras y cocina en celular (1,024) · `9.jpg` tina frente a un ventanal al campo de
golf. Libro: `Casa Cantalagua/` (12).

**Casa Bunker**: Drive (10 fotos; `3.jpg`, `5.jpg` y `7.jpg` miden ≤1,600 px, el resto
5,600-7,400). `1.jpg` ★ patio nocturno con jardineras y caídas de agua, cielo morado ·
`2.jpg` patio nocturno con pérgola · `4.jpg` patio interior con árbol · `5.jpg` jacuzzi
interior · `6.jpg` sala-comedor · `7.jpg` cocina con barra · `8.jpg` recámara con muro
de madera · `9.jpg` vestidor · `10.jpg` sala con cuadro. Libro: `Casa Bunker/` (14).

**Casa Lago**: Drive (9 fotos, 5,600-7,360). 1 ★ fachada nocturna con alberca · 2
billar y escalera · 3 comedor en doble altura con árbol · 4 sala con muro de piedra ·
5 cocina y bar · 6 cine en casa · 7-8 recámaras · 9 baño. Libro: `Casa Lago/` (16).

**Casa Palenque**: Drive (7 fotos, todas de 7,360). 1 ★ fachada y alberca al
atardecer · 2 alberca · 3 comedor en terraza · 4 doble altura con árbol y escalera ·
5 sala con árbol interior · 6 sala bajo la escalera · 7 cocina. Libro: `Casa Palenque/` (12).

**Casa El Pilar**: Drive `CASA PILAR/` (8 fotos, 3,500-6,000). 1 ★ fachada
nocturna con celosía y ladrillo · 2 fachada y cochera en hora azul · 3 celosía con
ladrillo de noche · 4 sala · 5 sala-comedor · 6 recámara (vertical) · 7 rincón de
lectura · 8 cocina de mármol. Libro: `Casa El Pilar/` (14).

**Casa Cataluña**: Drive (8 fotos; `1.jpg` y `3.jpg` miden 1,280, el resto ~7,000).
`2.jpg` ★ fachada con volúmenes grises al atardecer · `1.jpg`/`3.jpg` fachada ·
`4.jpg` escalera metálica y ladrillo · `5.jpg` sala-comedor · `6.jpg` cocina · `7.jpg`
y `8.jpg` recámaras. Libro: `Casa Cataluna/` (8). La cerámica es de Héctor Montero
"Pachanga" (hay que darle crédito).

**Depto. Móvil El Mangle**: Drive `DEPARTAMENTO BOCA DE TOMATLAN/` (10 fotos de
celular, ≤1,280). Contenedor sobre pilotes con cochera abajo, terraza con
sombrillas sobre la selva, asador, sala, recámara, escritorio. Libro:
`Depto Movil El Mangle/` (12, las mismas tomas). **Para un héroe falta foto pro.**

**Depto. Móvil Mismaloya**: Drive (6 fotos). `1.jpg` grúa izando el contenedor
(1,040; sirve para contar el proceso) · `2.heic` vista entre árboles (convertir) ·
`3-6.JPG` interiores (3,680, celular gran angular). Libro: `Depto Movil Mismaloya/`
(8: mar y rocas, vista desde arriba con paneles solares, terraza, cocina, sala).

### Residencial: solo en el libro (no están en el Drive)

- **Studio Manhattan** (11): sala con TV y sillón de piel, bar con botellas, cocina
  negra, recámara, baño, terraza con horno. Archivos `p084-099` a `p092-108`.
- **Casa Pompeya** (9; la carpeta del Drive está vacía): cochera con un Porsche
  clásico, salas con arte, comedor, cocina con isla, recámara. Archivos `p150-160` a `p157-167`.
- **Casa Xulha**: **solo la portada** (puerta pintada y título). No hay ninguna foto de
  la obra, ni en el libro ni en el Drive.

### Residencial: solo en el Drive (no están en el libro)

- **Casa Arenal** (5, ≤1,600, celular): casa en un lomerío con vista a las montañas,
  terraza y cocina con isla de mármol.
- **Casa Arrayán** (12, 400-800 px, con marca de agua): interiores oscuros, escalera
  de vidrio, árbol interior, sala de cine en el sótano. Hay 2 duplicados "Copia de".
- **Casa Fierro** (5, 3,000-4,900): `1.jpg` fachada vertical con celosía negra ★, sala
  con escalera, recámara con ladrillo, sala-cocina, baño.
- **Casa Olivo** (6, 3,600-3,900): `1.jpg` ★ fachada nocturna con un pino y un volado,
  sala roja, cocina, comedor, recámara, baño.
- **Casita Ajijic** (7, panorámicas de 4,608): `1.jpg` ★ contenedores negros en volado
  sobre la ladera, fachada, sala-comedor, terraza, cocina, 2 recámaras.
- **Depa Matute** (6, hasta 9,594): `1.jpg` contenedor-tráiler exhibido bajo el
  puente Matute Remus (1,831) ★ por su historia · recámaras, cocina-sala panorámica,
  sala, baño.
- **Departamento Playa Bosque** (5 renders, 2,000-2,250): la misma cabaña de
  contenedor en dos versiones, playa (con una vela tensada) y bosque. Exterior e interiores.
- **Casa Joco**: carpeta vacía.

### Institucional

- **Colegio Inglés Hidalgo**: Drive (6 fotos, 7,378, HDR). 1 ★ contenedor en volado
  · 2 pasillo con la placa "Oxford" · 3 aula · 4 patio-cafetería con canasta · 5
  escalera · 6 recepción. Libro: `Colegio Ingles Hidalgo/` (11).
- **Oficina MVA (Drive: OFICINAS YOGUI)**: 7 fotos de 1,280. Fachada nocturna, escalera,
  deck con muro verde y oficinas. Libro: `Oficina MVA/` (9).
- **Oficina móvil GE**: Drive (5, ≤1,280). Exterior junto a una planta industrial,
  contenedor gris de 40', coworking, oficina privada, cafetera.
- **Oficinas Sayer**: Drive (6, ≤1,280). Exterior frente a la nave naranja de Sayer,
  estaciones de trabajo y **montaje con grúa** (6).
- **Oficinas corporativas GDL**: **solo en el libro** (10). Puertas de contenedor
  pintadas en la portada, terraza con fachada de vidrio, sala, oficina de Taufic con
  muro de ladrillo y libreros, silla de barbero antigua.
- **Fábrica Colima**: **solo la portada** en el libro. No hay fotos de la fábrica.

### Proyectos en desarrollo (renders)

- **Basil del Mar**: Drive (9 renders + la subcarpeta `RENDERS/` con copias de 1-5, 2
  planos `.dwg` topográficos, el plano `CUYUTLAN RTK`, `PLANO TERRENO ARMERIA.pdf` y un
  video de WhatsApp del 2-jun-2023). **Está en Cuyutlán/Armería, Colima.** ★ `R3.beach
  final.jpg` (aérea con playa, 3,500) y `R3.R2 final (1).jpg` (aérea con alberca,
  3,500); también fachada de casa de 2 niveles, alberca del club y accesos nocturnos
  con palmeras.
- **Hospital Central Culiacán**: Drive (8 renders; 1-3 de 6,000 px). Torre y basamento,
  lobby, pasillo, recepción y habitación. **No se ven contenedores**: es
  arquitectura convencional del despacho.

### Comercial: solo portadas en el libro

**Bar La Obra** (colibrí pintado sobre una puerta de vidrio) y **Sigoo** (puertas con
estética de circo y fotos antiguas). No hay fotos de los locales.

### Personas

- `00 Portada y preliminares/p005-002.jpg`: hombre de pie en una sala con comedor.
  **Probablemente Taufic. Confirmar antes de usarla.**
- `01 Introduccion y prologos/p015-022.jpg`: retrato en blanco y negro en la página
  "Trabajar con Taufic". **Probablemente el Arq. Gashaan Basil.**
- No hay retrato en alta de Taufic ni fotos del equipo (la carpeta "FOTOS EMPLEADOS
  PAGINA" está vacía). **Hay que pedirlas.**

---

## Lenguaje visual (para diseñar en su línea)

- **Portada:** "THE CONTAINER HOME II · El arte de los contenedores en la vida
  diaria · TAUFIC GASHAAN Exclusive Design", con la foto nocturna de Casa Bosque.
  "II" en rojo.
- **Fondo de las aperturas:** textura de lámina corrugada de contenedor en
  café-morado muy oscuro (`02 Apertura Residencial/`, `01…/p009-007.jpg` y otras).
- **Cada sección abre con una puerta de contenedor pintada por un artista**
  (probablemente del *Container Door Art Festival*) y con el título en **caligrafía
  script blanca** sobre una franja de color. La franja es roja en casi todo,
  **naranja** en Oficinas GDL y Mismaloya, y vino en Bar La Obra.
- Las fotos de obra son casi siempre **nocturnas o de hora azul**, con luz cálida
  interior y cielo morado. Materiales: ladrillo aparente, piedra, madera, acero negro
  y concreto.
- Fichas técnicas en una franja inferior gris oscuro y folio sobre una pestaña roja.

## Lo que falta pedir

- Fotos en alta de Studio Manhattan, Pompeya, Xulha, oficinas GDL, la fábrica de
  Colima, Bar La Obra, Sigoo y OV Road (o la carpeta de Links del InDesign).
- Retrato profesional de Taufic, de su hijo y del equipo.
- Fotos pro de El Mangle y Mismaloya (hoy son de celular).
- Logo de Con Contenedores y la tipografía script del libro.
- Crédito y permiso de los fotógrafos (pacoG / animatoriumrex en Arrayán) y de los
  artistas de las puertas.
