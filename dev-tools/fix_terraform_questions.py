"""
Corrige preguntas donde la primera opción es parte de la pregunta
"""
import json
from pathlib import Path

def should_move_to_question(option_text):
    """Determina si una opción debe moverse a la pregunta"""
    if len(option_text) < 10:
        return False
    
    # Palabras interrogativas
    question_words = ['What ', 'How ', 'Which ', 'Where ', 'When ', 'Why ']
    if not any(word in option_text for word in question_words):
        return False
    
    # Indicadores de que es una pregunta
    indicators = ['?', 'should', 'would', 'can', 'could', 'must', 'do you']
    if any(ind in option_text.lower() for ind in indicators):
        return True
    
    return False

def fix_questions(questions):
    """Corrige las preguntas problemáticas"""
    fixed_count = 0
    
    for q in questions:
        if not q['answers'] or len(q['answers']) == 0:
            continue
        
        first_option = q['answers'][0]
        
        if should_move_to_question(first_option['text']):
            # Mover texto de la primera opción a la pregunta
            q['question'] = q['question'].strip() + ' ' + first_option['text'].strip()
            
            # Eliminar la primera opción
            q['answers'] = q['answers'][1:]
            
            # Re-asignar las letras (A, B, C, D...)
            for idx, ans in enumerate(q['answers']):
                ans['key'] = chr(ord('A') + idx)
            
            # Ajustar las respuestas correctas si es necesario
            # Si las correctas eran B, C ahora son A, B
            old_to_new = {}
            for idx in range(26):  # A-Z
                old_key = chr(ord('B') + idx)  # Era B, C, D...
                new_key = chr(ord('A') + idx)  # Ahora A, B, C...
                old_to_new[old_key] = new_key
            
            # Actualizar correctKeys
            new_correct = []
            for key in q['correctKeys']:
                if key in old_to_new:
                    new_correct.append(old_to_new[key])
                elif key == 'A':
                    # Si la respuesta correcta era A (la que movimos), ignorarla
                    pass
                else:
                    new_correct.append(key)
            
            q['correctKeys'] = new_correct
            fixed_count += 1
            print(f"✓ Q{q['id']}: Movido '{first_option['text'][:50]}...' a la pregunta")
    
    return fixed_count

if __name__ == "__main__":
    json_path = Path(r'c:\Github\OCITest\Descargables\Terraform\terraform-questions.json')
    
    # Cargar preguntas
    questions = json.loads(json_path.read_text(encoding='utf-8'))
    print(f"Total preguntas: {len(questions)}")
    
    # Corregir
    fixed = fix_questions(questions)
    
    if fixed > 0:
        # Guardar
        json_path.write_text(json.dumps(questions, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"\n✅ Corregidas {fixed} preguntas")
        print(f"💾 Guardado en {json_path}")
    else:
        print("\n✅ No se encontraron preguntas que corregir")
