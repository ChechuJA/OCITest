# Deploy the site and exam materials to Azure Blob Storage static website.
$ErrorActionPreference = "Stop"
$storageName = "ociquiz6861"
$rg = "ocitest-public-rg"
$container = "`$web"

Write-Host "Getting storage key..." -ForegroundColor Cyan
$storageKey = az storage account keys list --account-name $storageName --resource-group $rg --query "[0].value" -o tsv
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($storageKey)) {
    throw "Could not retrieve the storage account key."
}

$previousStorageKey = $env:AZURE_STORAGE_KEY
$env:AZURE_STORAGE_KEY = $storageKey
$uploadedCount = 0

try {
    function Upload-SiteFile($filePath, $blobName) {
        Write-Host "  Uploading $blobName" -ForegroundColor Yellow
        az storage blob upload --account-name $storageName --auth-mode key --container-name $container --name $blobName --file $filePath --overwrite --only-show-errors -o none
        if ($LASTEXITCODE -ne 0) {
            throw "Upload failed for $blobName."
        }
        $script:uploadedCount++
    }

    $coreFiles = @(
        "index.html",
        "quiz.js",
        "exam-loader.js",
        "style.css",
        "exams-catalog.json",
        "terraform-lectura.html",
        "lectura-todas.html"
    )

    foreach ($file in $coreFiles) {
        if (-not (Test-Path $file -PathType Leaf)) {
            throw "Required site file not found: $file"
        }
        Upload-SiteFile $file $file
    }

    Write-Host "Uploading Descargables/" -ForegroundColor Green
    $downloadFiles = Get-ChildItem -Recurse -File -Path "Descargables" -Include "*.json", "*.md", "*.html", "*.txt"
    foreach ($file in $downloadFiles) {
        $relativePath = $file.FullName.Replace((Get-Location).Path + "\", "").Replace("\", "/")
        Upload-SiteFile $file.FullName $relativePath
    }
}
finally {
    if ($null -eq $previousStorageKey) {
        Remove-Item Env:AZURE_STORAGE_KEY -ErrorAction SilentlyContinue
    }
    else {
        $env:AZURE_STORAGE_KEY = $previousStorageKey
    }
}

$webUrl = az storage account show --name $storageName --resource-group $rg --query primaryEndpoints.web -o tsv
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($webUrl)) {
    throw "Upload finished, but the website endpoint could not be verified."
}

Write-Host "Uploaded $uploadedCount files." -ForegroundColor Green
Write-Host "Azure URL: $webUrl" -ForegroundColor Green
