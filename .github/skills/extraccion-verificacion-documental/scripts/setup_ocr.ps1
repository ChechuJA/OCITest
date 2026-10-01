 [CmdletBinding()]
param([switch]$SkipInstall)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..')).Path
$venv = Join-Path $repoRoot '.venv'
$python = Join-Path $venv 'Scripts\python.exe'
$requirements = Join-Path $PSScriptRoot '..\assets\requirements-ocr.txt'

if (-not (Test-Path $python)) {
	if (Get-Command py -ErrorAction SilentlyContinue) {
		& py -3 -m venv $venv
	} elseif (Get-Command python -ErrorAction SilentlyContinue) {
		& python -m venv $venv
	} else {
		throw 'Instala Python 3.10 o superior y vuelve a ejecutar este script.'
	}
	if ($LASTEXITCODE -ne 0) { throw 'No se pudo crear .venv. Comprueba permisos y que Python esté instalado.' }
}

if (-not $SkipInstall) {
	& $python -m pip install --upgrade pip
	if ($LASTEXITCODE -ne 0) { throw 'No se pudo preparar pip en .venv.' }
	& $python -m pip install -r $requirements
	if ($LASTEXITCODE -ne 0) { throw 'No se pudieron instalar los paquetes OCR en .venv.' }
}

& $python -c "import pymupdf, numpy; from rapidocr_onnxruntime import RapidOCR; print('Entorno OCR listo:', pymupdf.VersionBind, '| NumPy', numpy.__version__, '| RapidOCR OK')"
if ($LASTEXITCODE -ne 0) { throw 'El entorno está incompleto. Ejecuta de nuevo sin -SkipInstall.' }
Write-Host "Python: $python"
