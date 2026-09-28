"""
Procesa Terraform 004 y Vault desde archivos Word
Flexible para procesar múltiples archivos desde cualquier ruta
"""
import json
import re
import os
import glob
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
    print(f"✅ JSON: {output_path.name} ({len(questions)} Q)")
    return len(questions)

def save_as_markdown(questions, output_path, title="Examen"):
    """Guarda las preguntas en formato Markdown"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
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
    
    print(f"✅ MD: {output_path.name} ({len(questions)} Q)")
    return len(questions)

def process_file(docx_path, json_output, md_output, title):
    """Procesa un archivo Word individual"""
    print(f"\n{'='*80}")
    print(f"📖 Procesando: {docx_path.name}")
    print(f"{'='*80}")
    
    if not docx_path.exists():
        print(f"❌ FALTA: {docx_path}")
        return 0
    
    # Extraer
    questions = extract_questions_from_docx(docx_path)
    print(f"📊 Extraídas: {len(questions)} preguntas")
    
    # Limpiar
    questions = clean_questions(questions)
    print(f"✅ Validadas: {len(questions)} preguntas")
    
    # Mostrar estadísticas
    multi_answer = [q for q in questions if len(q['correctKeys']) > 1]
    if multi_answer:
        print(f"📈 Multi-respuesta: {len(multi_answer)}")
    
    # Guardar
    count = save_as_json(questions, json_output)
    save_as_markdown(questions, md_output, title)
    
    # Mostrar primeras Q
    print(f"\n🔍 Primeras 2 preguntas:")
    for q in questions[:2]:
        print(f"  Q{q['id']}: {q['question'][:70]}...")
        print(f"    Respuestas: {len(q['answers'])} | Correcta(s): {', '.join(q['correctKeys'])}")
    
    return count

if __name__ == "__main__":
    
    total_questions = 0
    
    # ============================================================================
    # TERRAFORM 004
    # ============================================================================
    
    docx_path_tf004 = Path(r"c:\Github\OCITest\Descargables\Terraform\004\source\HASHICORP TERRAFORM - 004.docx")
    json_output_tf004 = Path(r"c:\Github\OCITest\Descargables\Terraform\004\terraform-questions.json")
    md_output_tf004 = Path(r"c:\Github\OCITest\Descargables\Terraform\004\terraform-questions.md")
    
    count_tf004 = process_file(
        docx_path_tf004,
        json_output_tf004,
        md_output_tf004,
        "HashiCorp Terraform Associate 004"
    )
    total_questions += count_tf004
    
    # ============================================================================
    # VAULT
    # ============================================================================
    
    docx_path_vault = Path(r"c:\Github\OCITest\Descargables\Vault\source\Vault 002 1.docx")
    json_output_vault = Path(r"c:\Github\OCITest\Descargables\Vault\vault-questions.json")
    md_output_vault = Path(r"c:\Github\OCITest\Descargables\Vault\vault-questions.md")
    
    count_vault = process_file(
        docx_path_vault,
        json_output_vault,
        md_output_vault,
        "HashiCorp Vault Associate"
    )
    total_questions += count_vault
    
    # ============================================================================
    # RESUMEN FINAL
    # ============================================================================
    
    print(f"\n{'='*80}")
    print(f"✅ PROCESAMIENTO COMPLETADO")
    print(f"{'='*80}")
    print(f"Terraform 004: {count_tf004} preguntas")
    print(f"Vault: {count_vault} preguntas")
    print(f"TOTAL: {total_questions} preguntas")
    print(f"{'='*80}\n")
