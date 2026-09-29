"""
Debugging: Ver qué Q no pasan validación
"""
import json
import re
from pathlib import Path
from docx import Document

docx_path = Path(r"c:\Github\OCITest\Descargables\Terraform\004\source\HASHICORP TERRAFORM - 004.docx")
doc = Document(docx_path)

questions = []
current_question = None
current_id = 0
in_question = False
in_answer = False
in_explanation = False

for i, para in enumerate(doc.paragraphs):
    text = para.text.strip()
    
    if not text:
        continue
    
    if text == "Question.":
        if current_question and current_question.get('question'):
            questions.append(current_question)
            current_id += 1
        
        current_question = {
            'id': current_id + 1,
            'question': '',
            'answers': [],
            'correctKeys': [],
            'explanation': ''
        }
        in_question = True
        in_answer = False
        in_explanation = False
        continue
    
    if not current_question:
        continue
    
    if text == "Answer":
        in_question = False
        in_answer = True
        in_explanation = False
        continue
    
    if text.startswith("Correct Answer:"):
        in_answer = False
        in_explanation = True
        answer_part = text.replace("Correct Answer:", "").strip()
        letters = re.findall(r'([A-Z])', answer_part)
        if letters:
            current_question['correctKeys'] = letters
        continue
    
    if text.startswith("Explanation:") or text.startswith("Discussion:"):
        in_explanation = True
        in_answer = False
        exp_text = text.split(":", 1)[1].strip() if ":" in text else ""
        if exp_text:
            current_question['explanation'] = exp_text
        continue
    
    if in_question:
        if current_question['question']:
            current_question['question'] += " " + text
        else:
            current_question['question'] = text
    
    elif in_answer and not in_explanation:
        if not current_question['answers']:
            key = 'A'
        else:
            last_key = current_question['answers'][-1]['key']
            key = chr(ord(last_key) + 1)
        
        current_question['answers'].append({
            'key': key,
            'text': text
        })
    
    elif in_explanation:
        if current_question['explanation']:
            current_question['explanation'] += " " + text
        else:
            current_question['explanation'] = text

if current_question and current_question.get('question'):
    questions.append(current_question)

print(f"Total extraídas: {len(questions)}")
print()

# Ver qué falla
print("Analizando validación...")
print()

for i, q in enumerate(questions[:10], 1):
    print(f"Q{q['id']}:")
    print(f"  ✓ question: {bool(q.get('question'))} | {len(q.get('question', ''))} chars")
    print(f"  ✓ answers: {len(q.get('answers', []))} opciones")
    print(f"  ✓ correctKeys: {q.get('correctKeys')} | len={len(q.get('correctKeys', []))}")
    print(f"  ✓ explanation: {bool(q.get('explanation'))} | {len(q.get('explanation', ''))} chars")
    
    # Validar
    valid = q.get('question') and q.get('answers') and q.get('correctKeys')
    print(f"  >>> VÁLIDA: {valid}")
    print()
