"""
Identifica las preguntas que no pudieron extraerse del Word
"""
import json
from pathlib import Path

# Cargar preguntas extraídas
json_path = Path(r'c:\Github\OCITest\Descargables\Terraform\terraform-questions.json')
questions = json.loads(json_path.read_text(encoding='utf-8'))

# Obtener IDs extraídos
extracted_ids = sorted([q['id'] for q in questions])

# Rango esperado: 1-379 (380 fue marcada como sin respuesta)
expected_ids = set(range(1, 380))
extracted_set = set(extracted_ids)

# Encontrar faltantes
missing = sorted(expected_ids - extracted_set)

print(f'Total extraídas: {len(extracted_ids)}')
print(f'Total esperadas: 379')
print(f'Faltantes: {len(missing)}')
print(f'\n{"="*80}')
print(f'PREGUNTAS CON PROBLEMAS (IDs faltantes):')
print(f'{"="*80}')
for qid in missing:
    print(f'  Question {qid}')

# Verificar preguntas con formato problemático
print(f'\n{"="*80}')
print(f'PREGUNTAS EXTRAÍDAS CON POSIBLES PROBLEMAS:')
print(f'{"="*80}')

problematic = []
for q in questions:
    issues = []
    if len(q['answers']) < 2:
        issues.append(f"solo {len(q['answers'])} opción(es)")
    if not q['correctKeys']:
        issues.append("sin respuesta correcta")
    if len(q['question']) < 20:
        issues.append(f"pregunta corta ({len(q['question'])} chars)")
    
    if issues:
        problematic.append((q['id'], issues, q['question'][:80]))

if problematic:
    for qid, issues, question_preview in problematic:
        print(f'\nQ{qid}:')
        print(f'  Problemas: {", ".join(issues)}')
        print(f'  Preview: {question_preview}...')
else:
    print('Ninguna pregunta extraída tiene problemas de formato obvios.')

print(f'\n{"="*80}')
print(f'RESUMEN:')
print(f'{"="*80}')
print(f'Preguntas que necesitan revisión manual: {missing}')
