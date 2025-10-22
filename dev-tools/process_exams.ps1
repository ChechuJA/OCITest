# Script PowerShell para numerar preguntas en archivos de examen
$nuevosDir = "c:\Github\Nuevos"
$files = Get-ChildItem -Path $nuevosDir -Filter "*.md"

Write-Host ""
Write-Host "Encontrados $($files.Count) archivos markdown" -ForegroundColor Cyan
Write-Host "============================================================"

$totalProcessed = 0

foreach ($file in $files | Sort-Object Name) {
    Write-Host ""
    Write-Host "Procesando: $($file.Name)" -ForegroundColor Yellow
    
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    $questionsBefore = ([regex]::Matches($content, "^#### Q\.", [System.Text.RegularExpressions.RegexOptions]::Multiline)).Count
    
    if ($questionsBefore -eq 0) {
        Write-Host "   No se encontraron preguntas" -ForegroundColor Yellow
        continue
    }
    
    Write-Host "   Preguntas encontradas: $questionsBefore"
    
    $questionNum = 1
    $newContent = $content -split "`n" | ForEach-Object {
        if ($_ -match "^#### Q\.") {
            $_ -replace "^#### Q\.", "#### Q$questionNum."
            $questionNum++
        } else {
            $_
        }
    }
    
    $newContent -join "`n" | Set-Content $file.FullName -Encoding UTF8 -NoNewline
    
    Write-Host "   Actualizado con $($questionNum - 1) preguntas numeradas" -ForegroundColor Green
    $totalProcessed++
}

Write-Host ""
Write-Host "============================================================"
Write-Host "Completado: $totalProcessed de $($files.Count) archivos" -ForegroundColor Green
