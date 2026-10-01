#!/usr/bin/env sh
set -eu

repo_root="$(CDPATH= cd -- "$(dirname -- "$0")/../../../../" && pwd)"
venv="$repo_root/.venv"
python="$venv/bin/python"
requirements="$(dirname -- "$0")/../assets/requirements-ocr.txt"

if [ ! -x "$python" ]; then
	python3 -m venv "$venv"
fi
"$python" -m pip install --upgrade pip
"$python" -m pip install -r "$requirements"
"$python" -c 'import pymupdf, numpy; from rapidocr_onnxruntime import RapidOCR; print("OCR environment ready:", pymupdf.VersionBind, "NumPy", numpy.__version__)'
