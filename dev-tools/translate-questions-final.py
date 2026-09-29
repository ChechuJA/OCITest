#!/usr/bin/env python3
"""
Traductor de preguntas de examen a español con manejo de rate limiting
Usa Google Translate con delays configurables
"""

import json
import time
import sys
from pathlib import Path
from deep_translator import GoogleTranslator

def translate_text(text, delay=3):
    """Traduce un texto con delay para evitar rate limiting"""
    if not text or len(text.strip()) == 0:
        return text
    
    try:
        print(f"  Traduciendo: {text[:50]}...", end=" ", flush=True)
        time.sleep(delay)  # Delay antes de traducir
        translator = GoogleTranslator(source_language='en', target_language='es')
        result = translator.translate(text)
        print(f"✓")
        return result
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"  Reintentando en 10 segundos...")
        time.sleep(10)
        try:
            translator = GoogleTranslator(source_language='en', target_language='es')
            result = translator.translate(text)
            print(f"  ✓ Reintento exitoso")
            return result
        except Exception as e2:
            print(f"  ✗ Falló de nuevo: {e2}")
            return text  # Devuelve el original si falla

def translate_exam(input_file, output_file, delay=3):
    """Traduce un archivo JSON de examen completo"""
    
    print(f"\n📖 Cargando: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f"📝 Total de preguntas: {len(questions)}")
    print(f"⏱️  Delay entre traducciones: {delay}s")
    print(f"\n🔄 Iniciando traducción...")
    
    translated = []
    total = len(questions)
    
    for i, question in enumerate(questions, 1):
        print(f"\n[{i}/{total}] Pregunta {question['id']}")
        
        # Traducir pregunta
        translated_question = question['question']
        translated_question = translate_text(question['question'], delay)
        
        # Traducir respuestas
        translated_answers = []
        for answer in question['answers']:
            translated_text = translate_text(answer['text'], delay)
            translated_answers.append({
                'key': answer['key'],
                'text': translated_text
            })
        
        # Traducir explicación
        translated_explanation = question['explanation']
        if question.get('explanation') and not question['explanation'].startswith('http'):
            translated_explanation = translate_text(question['explanation'], delay)
        
        # Construir objeto traducido
        translated_q = {
            'id': question['id'],
            'question': translated_question,
            'answers': translated_answers,
            'correctKeys': question['correctKeys'],
            'explanation': translated_explanation
        }
        
        translated.append(translated_q)
    
    # Guardar archivo traducido
    print(f"\n💾 Guardando: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Traducción completada: {output_file}")

if __name__ == '__main__':
    # Configurar delays
    # Cambiar a 5+ segundos para evitar rate limiting
    DELAY_BETWEEN_TRANSLATIONS = 5
    
    base_dir = Path(__file__).parent.parent
    
    # Terraform 004
    print("=" * 60)
    print("TRADUCIENDO: Terraform 004")
    print("=" * 60)
    terraform_input = base_dir / 'Descargables' / 'Terraform' / '004' / 'terraform-questions.json'
    terraform_output = base_dir / 'Descargables' / 'Terraform' / '004' / 'terraform-questions-es.json'
    translate_exam(str(terraform_input), str(terraform_output), DELAY_BETWEEN_TRANSLATIONS)
    
    print("\n" + "=" * 60)
    print("Esperando 30 segundos antes de siguiente examen...")
    print("=" * 60)
    time.sleep(30)
    
    # Vault
    print("\n" + "=" * 60)
    print("TRADUCIENDO: Vault")
    print("=" * 60)
    vault_input = base_dir / 'Descargables' / 'Vault' / 'vault-questions.json'
    vault_output = base_dir / 'Descargables' / 'Vault' / 'vault-questions-es.json'
    translate_exam(str(vault_input), str(vault_output), DELAY_BETWEEN_TRANSLATIONS)
    
    print("\n" + "=" * 60)
    print("✨ ¡Todas las traducciones completadas!")
    print("=" * 60)
