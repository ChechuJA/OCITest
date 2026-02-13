import json

# Cargar el JSON
with open('c:/Github/OCITest/Descargables/GH-300/gh300-questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Crear el contenido para leer en voz alta
output = []
output.append('GH-300 — GitHub Copilot\n')
output.append('Preguntas y Respuestas Correctas para Lectura\n')
output.append('=' * 60 + '\n\n')

for q in questions:
    # Agregar la pregunta
    output.append(f'Q{q["id"]}. {q["question"]}\n')
    
    # Encontrar y agregar solo la(s) respuesta(s) correcta(s)
    correct_keys = q['correctKeys']
    correct_answers = [ans for ans in q['answers'] if ans['key'] in correct_keys]
    
    for ans in correct_answers:
        output.append(f'Respuesta: {ans["key"]}. {ans["text"]}\n')
    
    output.append('\n')

# Guardar el archivo
with open('c:/Github/OCITest/Descargables/GH-300/gh300-lectura.txt', 'w', encoding='utf-8') as f:
    f.writelines(output)

print(f'Archivo creado: gh300-lectura.txt con {len(questions)} preguntas')
