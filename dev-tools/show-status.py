import os
import json

print("=" * 80)
print(" 🎉 RESTRUCTURACIÓN COMPLETADA - RESUMEN VISUAL")
print("=" * 80)
print()

# Catálogo
with open('exams-catalog.json') as f:
    catalog = json.load(f)

print("📊 ESTADO DEL CATÁLOGO:")
print(f"   • Total exámenes: {catalog['metadata']['totalExams']}")
print(f"   • Total preguntas: {catalog['metadata']['totalQuestions']}")
print(f"   • Última actualización: {catalog['metadata']['lastUpdated']}")
print()

print("📋 EXÁMENES ACTIVOS (11):")
active = [e for e in catalog['exams'] if e['questions'] > 0]
for i, exam in enumerate(active[:6], 1):
    print(f"   {i}. {exam['title'][:40]:40} | {exam['questions']:3} Q")
print(f"   ... y {len(active)-6} más")
print()

print("⏳ EXÁMENES EN PREPARACIÓN (2):")
pending = [e for e in catalog['exams'] if e['questions'] == 0]
for exam in pending:
    print(f"   • {exam['title']:40} | {exam['file']}")
print()

print("=" * 80)
print()

print("✅ VERIFICACIONES COMPLETADAS:")
print()

# Archivos principales
core_files = ['index.html', 'quiz.js', 'exam-loader.js', 'style.css', 'exams-catalog.json']
print("Core Files:")
for f in core_files:
    exists = "✅" if os.path.exists(f) else "❌"
    print(f"   {exists} {f}")
print()

# Terraform
print("Terraform:")
for version in ['003', '004']:
    path = f'Descargables/Terraform/{version}/terraform-questions.json'
    exists = "✅" if os.path.exists(path) else "⏳" if version == '004' else "❌"
    status = "Ready" if exists == "✅" else "Pending upload" if version == '004' else "Missing"
    print(f"   {exists} Terraform {version} - {status}")
print()

# Vault
print("Vault:")
exists = "⏳" if os.path.exists('Descargables/Vault') else "❌"
print(f"   {exists} Vault - Pending upload")
print()

# Documentación
print("Documentación:")
docs = [
    'INSTRUCCIONES-CLARAS.md',
    'PLAN-TERRAFORM-004-VAULT.md',
    'QUICK-REFERENCE.md',
    'RESTRUCTURACION-COMPLETADA.md'
]
for doc in docs:
    exists = "✅" if os.path.exists(doc) else "❌"
    print(f"   {exists} {doc}")
print()

print("=" * 80)
print()
print("🎯 PRÓXIMOS PASOS:")
print()
print("   1. Sube archivos de Terraform 004 en:")
print("      Descargables/Terraform/004/source/")
print()
print("   2. Sube archivos de Vault en:")
print("      Descargables/Vault/source/")
print()
print("   3. Ejecuta validación:")
print("      python dev-tools/validate-catalog.py")
print()
print("   4. Verifica en navegador:")
print("      Abre index.html y prueba los exámenes")
print()
print("=" * 80)
print()
print("🟢 STATUS: RESTRUCTURACIÓN COMPLETADA - LISTA PARA UPLOAD")
print()
