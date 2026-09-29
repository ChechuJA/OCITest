# Deploy to Azure Blob Storage
$storageName = "ociquiz6861"
$rg = "ocitest-public-rg"
$container = "`$web"

Write-Host "🚀 Getting storage key..." -ForegroundColor Cyan
$storageKey = az storage account keys list --account-name $storageName --resource-group $rg --query "[0].value" -o tsv

Write-Host "📤 Uploading files..." -ForegroundColor Green

# Core files
$coreFiles = @(
    "index.html",
    "quiz.js",
    "exam-loader.js",
    "style.css",
    "exams-catalog.json",
    "terraform-lectura.html",
    "vault-lectura.html",
    "lectura-todas.html"
)

foreach ($file in $coreFiles) {
    if (Test-Path $file) {
        Write-Host "  ↳ $file" -ForegroundColor Yellow
        az storage blob upload --account-name $storageName --account-key $storageKey --container-name $container --name $file --file $file --overwrite 2>&1 | Out-Null
    }
}

# Descargables
Write-Host "📁 Uploading Descargables/" -ForegroundColor Green
Get-ChildItem -Recurse -Path "Descargables" -Include "*.json", "*.md", "*.html" 2>/dev/null | ForEach-Object {
    $relativePath = $_.FullName.Replace((Get-Location).Path + "\", "").Replace("\", "/")
    Write-Host "  ↳ $relativePath" -ForegroundColor Yellow
    az storage blob upload --account-name $storageName --account-key $storageKey --container-name $container --name $relativePath --file $_.FullName --overwrite 2>&1 | Out-Null
}

Write-Host ""
Write-Host "="*70 -ForegroundColor Cyan
Write-Host "✅ DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "="*70 -ForegroundColor Cyan

$webUrl = az storage account show --name $storageName --resource-group $rg --query primaryEndpoints.web -o tsv
Write-Host "📍 Azure URL: $webUrl" -ForegroundColor Green
Write-Host "="*70 -ForegroundColor Cyan
