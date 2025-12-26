"""
Regenera el archivo markdown desde el JSON corregido
"""
import json
from pathlib import Path

# Cargar JSON
json_path = Path('Descargables/Terraform/terraform-questions.json')
questions = json.loads(json_path.read_text(encoding='utf-8'))

# Generar Markdown
md_path = Path('Descargables/Terraform/terraform-questions.md')
with open(md_path, 'w', encoding='utf-8') as f:
    f.write('# HashiCorp Terraform Associate\n\n')
    f.write(f'Total de preguntas: {len(questions)}\n\n')
    
    for q in questions:
        f.write(f'#### Q{q["id"]}. {q["question"]}\n\n')
        
        # Ordenar respuestas por key
        sorted_answers = sorted(q['answers'], key=lambda a: a['key'])
        
        for ans in sorted_answers:
            is_correct = ans['key'] in q['correctKeys']
            checkbox = '[x]' if is_correct else '[ ]'
            f.write(f'- {checkbox} {ans["key"]}. {ans["text"]}\n')
        
        f.write(f'\n> {q.get("explanation", "Sin explicación")}\n\n')

print(f'✅ Markdown regenerado: {md_path}')
print(f'Total preguntas: {len(questions)}')
