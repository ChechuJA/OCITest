"""
Extrae preguntas del documento Word de Terraform y las convierte al formato JSON
"""
import json
import re
from pathlib import Path
from docx import Document

def extract_questions_from_docx(docx_path):
    """Extrae todas las preguntas del documento Word"""
    doc = Document(docx_path)
    questions = []
    current_question = None
    current_section = None
    collecting_options = False
    
    for i, para in enumerate(doc.paragraphs):
        text = para.text.strip()
        
        # Detectar inicio de pregunta
        if re.match(r'^Question\s+(\d+)', text, re.IGNORECASE):
            # Guardar pregunta anterior si existe
            if current_question and current_question.get('question'):
                questions.append(current_question)
            
            # Nueva pregunta
            match = re.match(r'^Question\s+(\d+)', text, re.IGNORECASE)
            current_question = {
                'id': int(match.group(1)),
                'question': '',
                'answers': [],
                'correctKeys': [],
                'explanation': ''
            }
            current_section = 'question'
            collecting_options = False
            continue
        
        if not current_question:
            continue
        
        # Detectar sección de respuesta
        if re.match(r'^Answer\s+\d+', text, re.IGNORECASE):
            current_section = 'answer'
            collecting_options = False
            continue
        
        # Extraer respuesta correcta
        if text.startswith('Correct Answer:'):
            answer_part = text.replace('Correct Answer:', '').strip()
            # Extraer letras: puede ser "A", "BC", "A, B", "A (B)"
            letters = re.findall(r'([A-Z])', answer_part)
            current_question['correctKeys'] = letters
            current_section = 'reference'
            continue
        
        # Extraer referencia y explicación
        if current_section == 'reference' or current_section == 'answer':
            if text and not re.match(r'^Question\s+\d+', text):
                if current_question['explanation']:
                    current_question['explanation'] += ' ' + text
                else:
                    current_question['explanation'] = text
            continue
        
        # Procesar sección de pregunta
        if current_section == 'question' and text:
            # Si ya tenemos pregunta y no hay opciones, empezar a colectar opciones
            if current_question['question'] and not collecting_options:
                # Buscar indicadores de opciones múltiples
                if re.search(r'\(choose\s+(two|three|four)\)', text, re.IGNORECASE):
                    current_question['question'] += ' ' + text
                    collecting_options = True
                    continue
                else:
                    collecting_options = True
            
            # Agregar opciones
            if collecting_options:
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
            else:
                # Todavía estamos en la pregunta
                if current_question['question']:
                    current_question['question'] += ' ' + text
                else:
                    current_question['question'] = text
    
    # Agregar última pregunta
    if current_question and current_question.get('question'):
        questions.append(current_question)
    
    return questions

def clean_questions(questions):
    """Limpia y valida las preguntas extraídas"""
    cleaned = []
    for q in questions:
        # Validar que tenga los campos mínimos
        if not q.get('question') or not q.get('answers'):
            continue
        
        # Limpiar espacios
        q['question'] = ' '.join(q['question'].split())
        for ans in q['answers']:
            ans['text'] = ' '.join(ans['text'].split())
        
        # Validar que tenga respuesta correcta
        if not q.get('correctKeys'):
            print(f"⚠️ Pregunta {q['id']} sin respuesta correcta")
            continue
        
        cleaned.append(q)
    
    return cleaned

def save_as_json(questions, output_path):
    """Guarda las preguntas en formato JSON"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"✅ Guardado: {output_path} ({len(questions)} preguntas)")

def save_as_markdown(questions, output_path):
    """Guarda las preguntas en formato Markdown"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# HashiCorp Terraform Associate\n\n")
        f.write(f"Total de preguntas: {len(questions)}\n\n")
        
        for q in questions:
            f.write(f"#### Q{q['id']}. {q['question']}\n\n")
            
            # Ordenar respuestas por key
            sorted_answers = sorted(q['answers'], key=lambda a: a['key'])
            
            for ans in sorted_answers:
                is_correct = ans['key'] in q['correctKeys']
                checkbox = '[x]' if is_correct else '[ ]'
                f.write(f"- {checkbox} {ans['key']}. {ans['text']}\n")
            
            f.write(f"\n> {q.get('explanation', 'Sin explicación')}\n\n")
    
    print(f"✅ Guardado: {output_path} ({len(questions)} preguntas)")

if __name__ == "__main__":
    docx_path = Path(r"c:\Github\OCITest\Descargables\Terraform\HASHICORP TERRAFORM.docx")
    json_output = Path(r"c:\Github\OCITest\Descargables\Terraform\terraform-questions.json")
    md_output = Path(r"c:\Github\OCITest\Descargables\Terraform\terraform-questions.md")
    
    if not docx_path.exists():
        print(f"❌ Error: No se encuentra {docx_path}")
        exit(1)
    
    print(f"📖 Extrayendo preguntas de: {docx_path.name}")
    questions = extract_questions_from_docx(docx_path)
    print(f"📊 Extraídas: {len(questions)} preguntas")
    
    # Limpiar y validar
    questions = clean_questions(questions)
    print(f"✅ Validadas: {len(questions)} preguntas")
    
    # Mostrar estadísticas
    multi_answer = [q for q in questions if len(q['correctKeys']) > 1]
    print(f"📈 Preguntas multi-respuesta: {len(multi_answer)}")
    
    # Mostrar algunas preguntas de ejemplo
    print("\n" + "="*80)
    print("PRIMERAS 3 PREGUNTAS:")
    print("="*80)
    for q in questions[:3]:
        print(f"\nQ{q['id']}: {q['question'][:100]}...")
        print(f"Opciones: {len(q['answers'])}")
        print(f"Correcta(s): {', '.join(q['correctKeys'])}")
    
    # Guardar
    save_as_json(questions, json_output)
    save_as_markdown(questions, md_output)
    
    print(f"\n✅ Proceso completado")
