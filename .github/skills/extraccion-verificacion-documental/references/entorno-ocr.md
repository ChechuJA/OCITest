# Entorno OCR local

Requisito: Python 3.10 o superior y conexión para instalar dependencias la primera vez.

- Windows PowerShell: `& .\.github\skills\extraccion-verificacion-documental\scripts\setup_ocr.ps1`
- macOS/Linux: `sh ./.github/skills/extraccion-verificacion-documental/scripts/setup_ocr.sh`
- El entorno queda en `.venv/`, excluido del control de versiones.
- Paquetes: PyMuPDF para texto/render, NumPy para imágenes y RapidOCR ONNX Runtime para OCR. No requiere Tesseract.
- Ejecución: `.venv/Scripts/python.exe .github/skills/extraccion-verificacion-documental/scripts/pdf_to_markdown.py <archivo.pdf>` en Windows; en macOS/Linux sustituye por `.venv/bin/python`.
- Admite `--ocr auto` (OCR solo si falta texto nativo), `--ocr all`, `--ocr off`, `--pages 1,3-5`, `--dpi 220`, `-o salida.md` y `--force` explícito.

La primera preparación puede descargar ruedas Python y modelos OCR de RapidOCR. No se ejecuta automáticamente: hazla bajo petición y en una sesión con permisos de escritura/red.
