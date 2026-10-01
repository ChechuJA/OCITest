---
name: extraccion-verificacion-documental
description: 'Convierte PDF a Markdown, extrae texto nativo, aplica OCR local a páginas escaneadas y coteja datos con referencias de página. Úsala para transcribir PDF, extraer texto, OCR, revisar un documento o generar Markdown desde PDF.'
---

# Extracción y verificación documental

Convierte PDFs e imágenes a Markdown localmente, conservando la separación por páginas y dejando claro qué páginas se transcribieron. La extracción no equivale a verificar el contenido.

## Procedimiento

1. Conserva el original y reutiliza primero cualquier extractor ya disponible.
2. Usa el Python del `.venv` y [el conversor](./scripts/pdf_to_markdown.py). El modo `auto` usa texto nativo y aplica OCR a páginas sin texto; `--pages 1,3-5` limita la salida a páginas seleccionadas.
3. El script crea `<nombre>.extracted.md` y no sobrescribe salidas existentes. Usa `--force` solo si el usuario lo pidió explícitamente.
4. No instales paquetes ni descargues modelos sin autorización. Si falta RapidOCR, informa al usuario y señala [la guía del entorno](./references/entorno-ocr.md).
5. Coteja cifras e identificadores materiales contra las páginas originales. Marca dudas; no reconstruyas texto ilegible por contexto.
6. Informa archivo fuente, páginas incluidas, método por página, limitaciones y discrepancias. No describas como verificado algo que solo se transcribió.

## Herramientas

La extracción nativa requiere Python 3.10+ y PyMuPDF. OCR requiere además NumPy y RapidOCR ONNX Runtime. El skill incluye [dependencias](./assets/requirements-ocr.txt), [plantilla](./assets/transcripcion-template.md) y scripts de preparación para Windows y macOS/Linux.
