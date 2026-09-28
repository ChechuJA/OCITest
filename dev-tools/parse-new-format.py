"""
Parser mejorado para Terraform 004 y Vault
Maneja el formato: Question. | opciones | Answer | Correct Answer: X
"""
import json
import re
from pathlib import Path
from docx import Document

def extract_questions_from_docx(docx_path):
    """Extrae preguntas del formato actual"""
    doc = Document(docx_path)
    questions = []
    current_question = None
    current_id = 0
    in_question = False
    in_answer = False
    in_explanation = False
    
    for i, para in enumerate(doc.paragraphs):
        text = para.text.strip()
        
        # Saltar párrafos vacíos
        if not text:
            continue
        
        # Detectar inicio de pregunta
        if text == "Question.":
            # Guardar pregunta anterior si existe
            if current_question and current_question.get('question'):
                questions.append(current_question)
                current_id += 1
            
            # Nueva pregunta
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
        
        # Si no estamos en una pregunta, ignorar
        if not current_question:
            continue
        
        # Detectar "Answer"
        if text == "Answer":
            in_question = False
            in_answer = True
            in_explanation = False
            continue
        
        # Detectar "Correct Answer"
        if text.startswith("Correct Answer:"):
            in_answer = False
            in_explanation = True
            answer_part = text.replace("Correct Answer:", "").strip()
            # Extraer letras
            letters = re.findall(r'([A-Z])', answer_part)
            if letters:
                current_question['correctKeys'] = letters
            continue
        
        # Detectar "Explanation:" o "Discussion:"
        if text.startswith("Explanation:") or text.startswith("Discussion:"):
            in_explanation = True
            in_answer = False
            # Agregar el texto si tiene contenido después de ":"
            exp_text = text.split(":", 1)[1].strip() if ":" in text else ""
            if exp_text:
                current_question['explanation'] = exp_text
            continue
        
        # Procesar según sección
        if in_question:
            if current_question['question']:
                current_question['question'] += " " + text
            else:
                current_question['question'] = text
        
        elif in_answer and not in_explanation:
            # Esto es una opción de respuesta
            # Asignar letra automáticamente
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
    
    # Agregar última pregunta
    if current_question and current_question.get('question'):
        questions.append(current_question)
    
    return questions

def clean_questions(questions):
    """Limpia y valida preguntas"""
    cleaned = []
    for q in questions:
        if not q.get('question') or not q.get('answers'):
            continue
        
        # Limpiar espacios
        q['question'] = ' '.join(q['question'].split())
        for ans in q['answers']:
            ans['text'] = ' '.join(ans['text'].split())
        q['explanation'] = ' '.join(q['explanation'].split()) if q['explanation'] else ''
        
        # Validar respuesta correcta
        if not q.get('correctKeys'):
            continue
        
        cleaned.append(q)
    
    return cleaned

def save_as_json(questions, output_path):
    """Guarda JSON"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"✅ JSON: {len(questions)} Q")
    return len(questions)

def save_as_markdown(questions, output_path, title):
    """Guarda Markdown"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"Total: {len(questions)} preguntas\n\n")
        
        for q in questions:
            f.write(f"#### Q{q['id']}. {q['question']}\n\n")
            sorted_ans = sorted(q['answers'], key=lambda a: a['key'])
            for ans in sorted_ans:
                is_correct = ans['key'] in q['correctKeys']
                checkbox = '[x]' if is_correct else '[ ]'
                f.write(f"- {checkbox} {ans['key']}. {ans['text']}\n")
            f.write(f"\n> {q['explanation']}\n\n")
    
    print(f"✅ MD: {len(questions)} Q")
    return len(questions)

def process_file(docx_path, json_output, md_output, title):
    """Procesa un archivo"""
    print(f"\n{'='*70}")
    print(f"📖 {docx_path.name}")
    print(f"{'='*70}")
    
    if not docx_path.exists():
        print(f"❌ FALTA")
        return 0
    
    # Extraer
    questions = extract_questions_from_docx(docx_path)
    print(f"Extraídas: {len(questions)} Q")
    
    # Limpiar
    questions = clean_questions(questions)
    print(f"Validadas: {len(questions)} Q")
    
    # Stats
    multi = [q for q in questions if len(q['correctKeys']) > 1]
    if multi:
        print(f"Multi-respuesta: {len(multi)} Q")
    
    # Guardar
    save_as_json(questions, json_output)
    save_as_markdown(questions, md_output, title)
    
    # Show sample
    if questions:
        q = questions[0]
        print(f"\n🔍 Primera pregunta:")
        print(f"   {q['question'][:70]}...")
        print(f"   {len(q['answers'])} opciones, correcta(s): {', '.join(q['correctKeys'])}")
    
    return len(questions)

if __name__ == "__main__":
    
    total = 0
    
    # Terraform 004
    count_tf = process_file(
        Path(r"c:\Github\OCITest\Descargables\Terraform\004\source\HASHICORP TERRAFORM - 004.docx"),
        Path(r"c:\Github\OCITest\Descargables\Terraform\004\terraform-questions.json"),
        Path(r"c:\Github\OCITest\Descargables\Terraform\004\terraform-questions.md"),
        "HashiCorp Terraform Associate 004"
    )
    total += count_tf
    
    # Vault
    count_vault = process_file(
        Path(r"c:\Github\OCITest\Descargables\Vault\source\Vault 002 1.docx"),
        Path(r"c:\Github\OCITest\Descargables\Vault\vault-questions.json"),
        Path(r"c:\Github\OCITest\Descargables\Vault\vault-questions.md"),
        "HashiCorp Vault Associate"
    )
    total += count_vault
    
    # Resumen
    print(f"\n{'='*70}")
    print(f"✅ COMPLETADO")
    print(f"{'='*70}")
    print(f"Terraform 004: {count_tf} Q")
    print(f"Vault: {count_vault} Q")
    print(f"TOTAL: {total} Q")
    print(f"{'='*70}\n")
