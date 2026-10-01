"""Extract PDF text and OCR pages that have no usable text layer."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import re
import sys


IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp"}


def parse_page_selection(selection: str | None, page_count: int) -> list[int]:
    if not selection:
        return list(range(1, page_count + 1))

    pages = set()
    for part in selection.split(","):
        match = re.fullmatch(r"\s*(\d+)(?:\s*-\s*(\d+))?\s*", part)
        if not match:
            raise ValueError(f"Selección de páginas inválida: {part}")

        start = int(match.group(1))
        end = int(match.group(2) or start)
        if start < 1 or end < start or end > page_count:
            raise ValueError(f"Rango de páginas fuera del archivo: {part}")
        pages.update(range(start, end + 1))

    return sorted(pages)


def format_page_selection(pages: list[int]) -> str:
    ranges = []
    start = previous = pages[0]
    for page_number in pages[1:]:
        if page_number == previous + 1:
            previous = page_number
            continue
        ranges.append(str(start) if start == previous else f"{start}-{previous}")
        start = previous = page_number
    ranges.append(str(start) if start == previous else f"{start}-{previous}")
    return ", ".join(ranges)


def extract(source: Path, ocr_mode: str, dpi: int, page_selection: str | None = None) -> str:
    try:
        import pymupdf as fitz
    except ImportError as exc:
        raise RuntimeError("Falta PyMuPDF. Ejecuta el script local de preparación del entorno OCR.") from exc

    document = fitz.open(source)
    page_count = len(document)
    selected_pages = parse_page_selection(page_selection, page_count)
    engine = None
    sections = []
    for page_number in selected_pages:
        page = document[page_number - 1]
        text = page.get_text("text", sort=True).strip() if source.suffix.lower() == ".pdf" else ""
        should_ocr = ocr_mode == "all" or (ocr_mode == "auto" and not text)
        method = "texto nativo"

        if should_ocr:
            if engine is None:
                try:
                    import numpy as np
                    from rapidocr_onnxruntime import RapidOCR
                except ImportError as exc:
                    raise RuntimeError(
                        "Faltan NumPy o RapidOCR. Ejecuta el script local de preparación del entorno OCR."
                    ) from exc
                engine = RapidOCR()
            pixmap = page.get_pixmap(
                matrix=fitz.Matrix(dpi / 72, dpi / 72),
                colorspace=fitz.csRGB,
                alpha=False,
            )
            image = np.frombuffer(pixmap.samples, dtype=np.uint8).reshape(
                pixmap.height, pixmap.width, pixmap.n
            )
            detections, _ = engine(image)
            text = "\n".join(str(item[1]) for item in (detections or []))
            method = "OCR automático"

        if not text:
            text = "[No se detectó texto legible en esta página]"
        sections.append(f"## Página {page_number} · {method}\n\n{text}")

    document.close()
    extracted_at = datetime.now().astimezone().isoformat(timespec="minutes")
    return (
        f"# Transcripción: {source.name}\n\n"
        f"- Archivo fuente: `{source.name}`\n"
        f"- Páginas del archivo: {page_count}\n"
        f"- Páginas incluidas: `{format_page_selection(selected_pages)}`\n"
        f"- Extracción: {extracted_at}\n"
        "- Aviso: resultado automático; cotejar cifras e identificadores con el original.\n\n"
        + "\n\n---\n\n".join(sections)
        + "\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Transcribe un PDF o imagen a Markdown, aplicando OCR a páginas escaneadas."
    )
    parser.add_argument("source", type=Path, help="PDF o imagen JPG/PNG/TIFF/BMP")
    parser.add_argument("-o", "--output", type=Path, help="Ruta Markdown de salida")
    parser.add_argument("--ocr", choices=("auto", "all", "off"), default="auto")
    parser.add_argument("--pages", help="Páginas 1-based, por ejemplo `1,3-5`")
    parser.add_argument("--dpi", type=int, default=220)
    parser.add_argument("--force", action="store_true", help="Sobrescribe la salida si existe")
    args = parser.parse_args()

    source = args.source.resolve()
    if not source.is_file() or source.suffix.lower() not in IMAGE_SUFFIXES | {".pdf"}:
        parser.error("Indica un PDF o una imagen compatible existente.")
    if not 72 <= args.dpi <= 600:
        parser.error("--dpi debe estar entre 72 y 600.")
    output = args.output.resolve() if args.output else source.with_name(f"{source.stem}.extracted.md")
    if output.exists() and not args.force:
        parser.error(f"La salida ya existe: {output}. Usa --force para reemplazarla explícitamente.")

    try:
        markdown = extract(source, args.ocr, args.dpi, args.pages)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown, encoding="utf-8")
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Transcripción creada: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
