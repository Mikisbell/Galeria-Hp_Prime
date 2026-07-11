#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
preparar_imagenes.py — Herramienta de la Edición Español de Gallery (HP Prime).

Redimensiona y optimiza imágenes para que quepan en la memoria de la HP Prime.

¿Por qué existe esto?
    La HP Prime NO se queda sin memoria por el PESO del archivo (los MB en disco),
    sino por la RESOLUCIÓN: al mostrar una imagen, la calculadora la descomprime a
    píxeles crudos en la RAM. Una foto de 12 megapíxeles (4000x3000) ocupa ~24 MB
    descomprimida y revienta la memoria. La pantalla es de solo 320x240, así que
    no tiene sentido cargar más. Esta herramienta reduce la imagen a un tamaño
    razonable ANTES de subirla, resolviendo el problema de raíz.

Uso básico (deja las imágenes listas en la carpeta "listas/"):
    python tools/preparar_imagenes.py <carpeta_con_fotos>

Ejemplos:
    python tools/preparar_imagenes.py mis_fotos
    python tools/preparar_imagenes.py mis_fotos --salida galeria --max 320x240
    python tools/preparar_imagenes.py mis_fotos --calidad 90

Autor de la herramienta: Miguel Ángel Rivera Ospina ("Belico"), 2026.
Parte de la Edición Español de Gallery. Licencia GPL-3.0.
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Falta Pillow. Instálalo con:  pip install Pillow")

EXTENSIONES = {".jpg", ".jpeg", ".png"}
# Fondo negro: es el que usa la Galería detrás de las imágenes.
FONDO = (0, 0, 0)


def parse_tamano(texto):
    """Convierte '640x480' en (640, 480)."""
    try:
        w, h = texto.lower().split("x")
        return (int(w), int(h))
    except Exception:
        raise argparse.ArgumentTypeError("El tamaño debe ser AnchoxAlto, ej: 640x480")


def humano(n_bytes):
    """Formatea bytes a KB/MB legibles."""
    for unidad in ("B", "KB", "MB"):
        if n_bytes < 1024:
            return f"{n_bytes:.0f} {unidad}"
        n_bytes /= 1024
    return f"{n_bytes:.1f} GB"


def preparar(entrada, salida, tam_max, calidad):
    carpeta_in = Path(entrada)
    if not carpeta_in.is_dir():
        sys.exit(f"No existe la carpeta: {carpeta_in}")

    carpeta_out = Path(salida)
    carpeta_out.mkdir(parents=True, exist_ok=True)

    imagenes = sorted(
        p for p in carpeta_in.iterdir()
        if p.suffix.lower() in EXTENSIONES and p.name.lower() != "icon.png"
    )

    if not imagenes:
        sys.exit(f"No encontré imágenes (.jpg/.png) en: {carpeta_in}")

    print(f"\nPreparando {len(imagenes)} imagen(es) -> máx {tam_max[0]}x{tam_max[1]}\n")
    print(f"{'Archivo':<28}{'Antes':>10}{'Después':>10}   Reducción")
    print("-" * 62)

    total_antes = total_despues = 0

    for img_path in imagenes:
        try:
            with Image.open(img_path) as im:
                # Respeta la orientación EXIF (fotos de celular giradas).
                im = ImageOps.exif_transpose(im)

                # Si tiene transparencia, la aplanamos sobre fondo negro
                # (la Prime no maneja bien el canal alfa en este visor).
                if im.mode in ("RGBA", "LA", "P"):
                    im = im.convert("RGBA")
                    fondo = Image.new("RGB", im.size, FONDO)
                    fondo.paste(im, mask=im.split()[-1])
                    im = fondo
                else:
                    im = im.convert("RGB")

                # Reduce preservando proporción; solo achica, nunca agranda.
                im.thumbnail(tam_max, Image.LANCZOS)

                # Salida siempre como JPG baseline (no progresivo) optimizado:
                # mejor calidad/peso que PNG 8-bit para fotos y compatible con la Prime.
                destino = carpeta_out / (img_path.stem + ".jpg")
                im.save(
                    destino,
                    format="JPEG",
                    quality=calidad,
                    optimize=True,
                    progressive=False,
                )

            antes = img_path.stat().st_size
            despues = destino.stat().st_size
            total_antes += antes
            total_despues += despues
            pct = (1 - despues / antes) * 100 if antes else 0
            print(f"{img_path.name[:27]:<28}{humano(antes):>10}{humano(despues):>10}   -{pct:4.0f}%")

        except Exception as e:
            print(f"{img_path.name[:27]:<28}  ERROR: {e}")

    print("-" * 62)
    if total_antes:
        pct_total = (1 - total_despues / total_antes) * 100
        print(f"{'TOTAL':<28}{humano(total_antes):>10}{humano(total_despues):>10}   -{pct_total:4.0f}%")
    print(f"\nListo. Imágenes preparadas en: {carpeta_out.resolve()}")
    print("Ahora copia esas imágenes dentro de la carpeta Gallery.hpappdir y transfiérela.\n")


def main():
    ap = argparse.ArgumentParser(
        description="Redimensiona y optimiza imágenes para la Galería de la HP Prime."
    )
    ap.add_argument("entrada", help="Carpeta con las imágenes originales.")
    ap.add_argument("--salida", default="listas", help="Carpeta de salida (por defecto: listas).")
    ap.add_argument("--max", type=parse_tamano, default=(640, 480),
                    help="Tamaño máximo AnchoxAlto (por defecto 640x480; usa 320x240 para máximo ahorro).")
    ap.add_argument("--calidad", type=int, default=85,
                    help="Calidad JPG 1-100 (por defecto 85).")
    args = ap.parse_args()

    preparar(args.entrada, args.salida, args.max, args.calidad)


if __name__ == "__main__":
    main()
