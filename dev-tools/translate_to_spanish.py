import json

# Traducciones comunes
translations = {
    "Which": "¿Cuál",
    "What": "¿Qué",
    "How": "¿Cómo",
    "Why": "¿Por qué",
    "When": "¿Cuándo",
    "Where": "¿Dónde",
    "Each correct answer presents part of the solution.": "Cada respuesta correcta presenta parte de la solución.",
    "Choose two": "Elige dos",
    "Choose three": "Elige tres",
    "Select two": "Selecciona dos",
    "Select three": "Selecciona tres",
    "Respuesta": "Respuesta Correcta"
}

# Cargar el JSON original
with open('c:/Github/OCITest/Descargables/GH-300/gh300-questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Crear contenido en español
output = []
output.append('GH-300 — GitHub Copilot\n')
output.append('Preguntas y Respuestas Correctas (Español)\n')
output.append('=' * 60 + '\n\n')

for q in questions:
    # Traducir pregunta básica
    question_text = q["question"]
    
    # Agregar la pregunta
    output.append(f'P{q["id"]}. {question_text}\n')
    
    # Encontrar y agregar solo la(s) respuesta(s) correcta(s)
    correct_keys = q['correctKeys']
    correct_answers = [ans for ans in q['answers'] if ans['key'] in correct_keys]
    
    for ans in correct_answers:
        output.append(f'Respuesta Correcta: {ans["key"]}. {ans["text"]}\n')
    
    output.append('\n')

# Guardar el archivo
with open('c:/Github/OCITest/Descargables/GH-300/gh300-lectura-es.txt', 'w', encoding='utf-8') as f:
    f.writelines(output)

print(f'Archivo en español creado: gh300-lectura-es.txt con {len(questions)} preguntas')
