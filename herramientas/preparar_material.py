#!/usr/bin/env python3
"""Arma la carpeta de material del repo a partir de las fuentes originales.

- fotos/obras/<categoria>/<proyecto>/   fotos del Drive a 2000 px (JPG)
- fotos/libro/<seccion>/                imágenes extraídas del libro (tal cual, ~850 px)
- fotos/_miniaturas/...                 miniaturas de 480 px para la galería
- fotos/README.md                       galería navegable en GitHub
- fuentes/drive/...                     documentos, planos y video del Drive
- libro/AVANCE-SEPTIEMBRE2.pdf          el avance del libro

Uso (desde la raíz del repo):
    python3 herramientas/preparar_material.py [--drive RUTA] [--libro RUTA]

Por defecto lee de ~/Downloads/03-Proyectos y clientes/Taufic Gashaan/.
Requiere macOS (usa `sips`). Es idempotente: no rehace lo que ya existe.
"""

import argparse
import re
import shutil
import struct
import subprocess
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BASE = Path.home() / "Downloads/03-Proyectos y clientes/Taufic Gashaan"
FOTO = {".jpg", ".jpeg", ".heic", ".png"}
LADO_FOTO = 2000
LADO_MINI = 480


def slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto.strip()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def lado_mayor(ruta: Path) -> int:
    out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(ruta)], capture_output=True, text=True).stdout
    nums = [int(n) for n in re.findall(r"pixel(?:Width|Height): (\d+)", out)]
    return max(nums) if nums else 0


def orientacion(ruta: Path) -> int:
    """Marca EXIF 0x0112. Algunas fotos guardan los píxeles girados y dependen de ella."""
    d = ruta.read_bytes()[:300000]
    i = d.find(b"Exif\x00\x00")
    if i < 0:
        return 1
    t = d[i + 6 :]
    e = "<" if t[:2] == b"II" else ">"
    ifd = struct.unpack(e + "I", t[4:8])[0]
    for k in range(struct.unpack(e + "H", t[ifd : ifd + 2])[0]):
        ent = t[ifd + 2 + 12 * k : ifd + 14 + 12 * k]
        if struct.unpack(e + "H", ent[:2])[0] == 0x112:
            return struct.unpack(e + "H", ent[8:10])[0]
    return 1


# filtro de ffmpeg que endereza los píxeles según la marca EXIF
GIRO = {3: "hflip,vflip", 6: "transpose=1", 8: "transpose=2"}


def a_jpg(origen: Path, destino: Path, lado: int, calidad: int) -> None:
    if destino.exists():
        return
    destino.parent.mkdir(parents=True, exist_ok=True)
    giro = GIRO.get(orientacion(origen)) if origen.suffix.lower() in {".jpg", ".jpeg"} else None
    if giro:
        # sips conserva la marca EXIF; ffmpeg lee los píxeles crudos, los gira y
        # escribe un JPG sin metadatos, que se ve igual en cualquier programa.
        escala = f"scale='if(gt(iw,ih),min({lado},iw),-2)':'if(gt(iw,ih),-2,min({lado},ih))'"
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-noautorotate", "-i", str(origen), "-vf", f"{giro},{escala}",
             "-q:v", "3", "-map_metadata", "-1", str(destino)],
            check=True,
        )
        return
    cmd = ["sips", "-s", "format", "jpeg", "-s", "formatOptions", str(calidad)]
    if lado_mayor(origen) > lado:
        cmd += ["-Z", str(lado)]
    subprocess.run(cmd + [str(origen), "--out", str(destino)], check=True, capture_output=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--drive", type=Path, default=BASE / "Drive fotos proyectos")
    ap.add_argument("--libro", type=Path, default=BASE / "Libro The Container Home II")
    args = ap.parse_args()

    fotos = RAIZ / "fotos"
    galeria: dict[str, list[tuple[str, str]]] = {}

    # Fotos del Drive
    for f in sorted(args.drive.rglob("*")):
        if not f.is_file() or f.name.startswith("_"):
            continue
        rel = f.relative_to(args.drive)
        partes = [slug(p) for p in rel.parts[:-1]]
        if f.suffix.lower() in FOTO:
            nombre = slug(f.stem) + ".jpg"
            destino = fotos / "obras" / Path(*partes) / nombre
            mini = fotos / "_miniaturas" / "obras" / Path(*partes) / nombre
            a_jpg(f, destino, LADO_FOTO, 82)
            a_jpg(destino, mini, LADO_MINI, 70)
            clave = "obras/" + "/".join(partes)
            galeria.setdefault(clave, []).append((destino.relative_to(fotos).as_posix(), mini.relative_to(fotos).as_posix()))
        else:
            destino = RAIZ / "fuentes" / "drive" / Path(*partes) / f.name
            if not destino.exists():
                destino.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, destino)

    # Imágenes del libro
    for f in sorted((args.libro / "imagenes-libro").rglob("*.jpg")):
        seccion = slug(f.parent.name)
        destino = fotos / "libro" / seccion / f.name
        mini = fotos / "_miniaturas" / "libro" / seccion / f.name
        if not destino.exists():
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, destino)
        a_jpg(destino, mini, LADO_MINI, 70)
        galeria.setdefault(f"libro/{seccion}", []).append((destino.relative_to(fotos).as_posix(), mini.relative_to(fotos).as_posix()))

    # PDF del libro
    pdf = args.libro / "AVANCE-SEPTIEMBRE2.pdf"
    if pdf.exists() and not (RAIZ / "libro" / pdf.name).exists():
        (RAIZ / "libro").mkdir(exist_ok=True)
        shutil.copy2(pdf, RAIZ / "libro" / pdf.name)

    # Galería
    lineas = [
        "# Galería de fotos",
        "",
        "Toca una miniatura para abrir la foto (2000 px, lista para copiar o descargar).",
        "Qué muestra cada foto y cuál sirve para qué: [../ASSETS.md](../ASSETS.md).",
        "Originales en resolución completa: carpeta de Drive del estudio (ver README principal).",
        "",
    ]
    for titulo, grupo in [("Obras (Drive del estudio)", "obras/"), ("Imágenes del libro (baja resolución, ~850 px)", "libro/")]:
        lineas += [f"## {titulo}", ""]
        for clave in sorted(k for k in galeria if k.startswith(grupo)):
            nombre = clave.split("/", 1)[1].replace("/", " / ").replace("-", " ").upper()
            lineas += [f"### {nombre}", "", f"`fotos/{clave}/` · {len(galeria[clave])} archivos", "", "<p>"]
            for full, mini in galeria[clave]:
                lineas.append(f'<a href="{full}"><img src="{mini}" width="180" alt=""></a>')
            lineas += ["</p>", ""]
    (fotos / "README.md").write_text("\n".join(lineas), encoding="utf-8")
    total = sum(len(v) for v in galeria.values())
    print(f"{total} imágenes en {len(galeria)} carpetas → {fotos}")


if __name__ == "__main__":
    main()
