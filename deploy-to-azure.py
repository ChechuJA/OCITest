#!/usr/bin/env python3
"""
Deploy OCITest to Azure Blob Storage Static Website
"""

import os
import subprocess
import json
from pathlib import Path

def run_cmd(cmd):
    """Execute Azure CLI command"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        return None
    return result.stdout.strip()

def main():
    storage_name = "ociquiz6861"
    rg = "ocitest-public-rg"
    container = "$web"
    
    print(f"🚀 Deploying to {storage_name}...")
    
    # Get storage key
    print("🔑 Getting storage key...")
    cmd = f'az storage account keys list --account-name {storage_name} --resource-group {rg} --query "[0].value" -o tsv'
    storage_key = run_cmd(cmd)
    
    if not storage_key:
        print("❌ Failed to get storage key")
        return False
    
    print(f"✅ Got storage key")
    
    # Files to upload
    files_to_upload = [
        "index.html",
        "quiz.js",
        "exam-loader.js",
        "style.css",
        "exams-catalog.json",
        "terraform-lectura.html",
        "vault-lectura.html",
        "lectura-todas.html",
    ]
    
    # Upload files
    print(f"📤 Uploading files...")
    for file in files_to_upload:
        if Path(file).exists():
            cmd = (
                f'az storage blob upload '
                f'--account-name {storage_name} '
                f'--account-key {storage_key} '
                f'--container-name "{container}" '
                f'--name "{file}" '
                f'--file "{file}" '
                f'--overwrite'
            )
            result = run_cmd(cmd)
            if result:
                print(f"  ✅ {file}")
            else:
                print(f"  ⚠️  {file} - skipped")
    
    # Upload Descargables recursively
    print(f"📁 Uploading Descargables/...")
    descargables_path = Path("Descargables")
    if descargables_path.exists():
        for file_path in descargables_path.rglob("*"):
            if file_path.is_file() and file_path.suffix in [".json", ".md"]:
                relative_path = str(file_path.relative_to(".")).replace("\\", "/")
                cmd = (
                    f'az storage blob upload '
                    f'--account-name {storage_name} '
                    f'--account-key {storage_key} '
                    f'--container-name "{container}" '
                    f'--name "{relative_path}" '
                    f'--file "{file_path}" '
                    f'--overwrite'
                )
                result = run_cmd(cmd)
                if result:
                    print(f"  ✅ {relative_path}")
    
    # Get web URL
    print(f"\n🌐 Getting web URL...")
    cmd = f'az storage account show --name {storage_name} --resource-group {rg} --query primaryEndpoints.web -o tsv'
    web_url = run_cmd(cmd)
    
    print(f"\n" + "="*70)
    print(f"✅ DEPLOYMENT COMPLETE!")
    print(f"="*70)
    print(f"📍 Azure URL: {web_url}")
    print(f"="*70)
    
    return True

if __name__ == "__main__":
    main()
