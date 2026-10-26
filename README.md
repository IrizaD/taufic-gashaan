# Arq. Taufic Gashaan · Exclusive Design

Todo el material del cliente en un solo lugar: su libro, las fotos de su obra, los
testimonios de sus clientes y las notas de marca. Sirve para hacer webs, presentaciones,
anuncios, contenido o cualquier pieza sin tener que pedir acceso a nada más.

**Quién es:** arquitecto de Guadalajara. Diseña casas, oficinas, escuelas y espacios
comerciales; varios de sus proyectos usan contenedores marinos como estructura.
**La marca es la firma de diseño, Taufic Gashaan · Exclusive Design.** Con
Contenedores (Colima) es la empresa que construye y fabrica; aparece como
constructora, no como protagonista.

## Por dónde empezar

| Si necesitas… | Abre |
|---|---|
| Entender al cliente, su mensaje y qué falta confirmar | [CLAUDE.md](CLAUDE.md), secciones "Marca", "Quién es" y "Cómo se cuenta Taufic" |
| Datos de una obra (m², contenedores, ubicación) o una cita textual | [LIBRO.md](LIBRO.md) |
| Ver todas las fotos con miniaturas | [fotos/README.md](fotos/README.md) |
| Saber qué foto sirve para qué y cuál tiene buena resolución | [ASSETS.md](ASSETS.md) |
| El libro completo (PDF, 212 pp.) | [libro/AVANCE-SEPTIEMBRE2.pdf](libro/AVANCE-SEPTIEMBRE2.pdf) |
| Planos, documentos y video originales del Drive | [fuentes/drive/](fuentes/drive/) |
| El texto completo del libro para buscar o copiar | [fuentes/libro-avance-septiembre2-texto.txt](fuentes/libro-avance-septiembre2-texto.txt) |

## Qué hay en las fotos

- `fotos/obras/` — **174 fotos** del Drive del estudio, en 23 proyectos (residencial,
  institucional y en desarrollo), a **2000 px**. Sirven para web, presentaciones y redes.
- `fotos/libro/` — **194 imágenes** sacadas del libro, ordenadas por sección. Son de baja
  resolución (~850 px). Úsalas solo para las obras que no están en el Drive (Studio
  Manhattan, Casa Pompeya, oficinas de Guadalajara) o como referencia de diseño.
- **Para impresión**, pide los originales (hasta 9,600 px) en el Drive del estudio:
  https://drive.google.com/drive/folders/10NXHTbFCZiG9c5gTuqXpztqxNf6s0nwv

## Cómo copiarlo

- **Todo de una vez:** en GitHub, botón verde **Code → Download ZIP** (unos 160 MB),
  o `git clone https://github.com/IrizaD/taufic-gashaan.git`.
- **Una foto o un archivo:** ábrelo en GitHub y usa el botón de descarga.
- **Texto:** todo está en Markdown y se copia directo desde GitHub.

## Reglas para trabajar con este material

1. **Datos solo de la fuente.** Cifras, citas, nombres y años salen del libro, del Drive o
   de lo que el cliente confirme. No inventes premios, años de trayectoria ni números.
2. **Los testimonios se citan tal cual** (están textuales en `LIBRO.md`), firmados con el
   nombre de pila, como en el libro.
3. **La firma va primero.** No vistas el diseño de "contenedor" ni centres el mensaje en
   cajas de metal: el contenedor es un material de su obra, no su identidad.
4. **No todo su portafolio es de contenedores.** Casa El Pilar y el Hospital Culiacán son
   construcción convencional.
5. **Créditos pendientes:** las fotos de Casa Arrayán tienen marca de agua de un fotógrafo
   (pacoG / animatoriumrex.com), las cerámicas de Casa Cataluña son de Héctor Montero
   "Pachanga", y las puertas pintadas del libro son de artistas sin nombre todavía.
   Antes de publicar, confirma créditos y permisos.

## Qué falta confirmar con el cliente

Su nombre completo y el nombre exacto de la firma, retratos (de él, de su hijo y del
equipo), WhatsApp y correo de contacto, logo, fotos en alta de las obras que solo están en
el libro, y si se pueden publicar las obras que solo están en el Drive. La lista completa
está al final de [CLAUDE.md](CLAUDE.md).

## Trabajo hecho

- **Sitio web** (borrador para revisión, sin indexar): https://taufic-gashaan-web.vercel.app
  · repo `IrizaD/taufic-gashaan-web`.

## Mantenimiento

`herramientas/preparar_material.py` vuelve a armar `fotos/`, `libro/` y `fuentes/drive/`
desde los originales (macOS, usa `sips` y `ffmpeg`). Si llegan fotos nuevas, súmalas a la
carpeta original y corre `python3 herramientas/preparar_material.py`.
