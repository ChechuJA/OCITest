import json
import os

# Validar catálogo
with open('exams-catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('✅ exams-catalog.json es válido')
print()
print(f'📊 Total exámenes: {data["metadata"]["totalExams"]}')
print(f'📊 Total preguntas: {data["metadata"]["totalQuestions"]}')
print(f'📅 Última actualización: {data["metadata"]["lastUpdated"]}')
print()
print('📋 Exámenes:')
for i, exam in enumerate(data['exams'], 1):
    status = '⏳' if exam['questions'] == 0 else '✅'
    print(f'{i:2}. {status} {exam["id"]:30} | {exam["questions"]:3} Q | {exam["file"]}')

print()
print('📁 Verificando rutas de archivos:')
missing = []
for exam in data['exams']:
    if not exam['file'].startswith('builtin:'):
        if not os.path.exists(exam['file']):
            missing.append(exam['file'])
            print(f'  ❌ FALTA: {exam["file"]}')
        else:
            print(f'  ✅ OK: {exam["file"]}')

if missing:
    print()
    print(f'⚠️  Archivos faltantes: {len(missing)}')
else:
    print()
    print('✅ Todos los archivos existen')
