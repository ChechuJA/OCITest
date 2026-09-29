#!/usr/bin/env python3
"""
Traductor de preguntas de examen a español con rate limiting agresivo.
Usa delays de 2-3 segundos entre requests para respetar límites de Google Translate.
"""

import json
import time
import random
from pathlib import Path
from deep_translator import GoogleTranslator

def translate_text(text, retry_count=0, max_retries=3):
    """Traducir texto con reintentos exponenciales."""
    try:
        # Delay exponencial: 2-3 segundos + jitter aleatorio
        delay = 2 + random.uniform(0.5, 1.5)
        time.sleep(delay)
        
        translator = GoogleTranslator(source_language='en', target_language='es')
        return translator.translate(text)
    except Exception as e:
        if retry_count < max_retries:
            wait_time = (retry_count + 1) * 5  # 5, 10, 15 segundos
            print(f"⚠️  Reintentando en {wait_time}s... (error: {str(e)[:50]})")
            time.sleep(wait_time)
            return translate_text(text, retry_count + 1, max_retries)
        else:
            print(f"❌ No se pudo traducir después de {max_retries} intentos: {text[:50]}...")
            return text  # Retornar texto original si falla

def translate_exam(input_file, output_file):
    """Traducir preguntas de un examen."""
    print(f"\n📖 Leyendo: {input_file}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f"🔄 Traduciendo {len(questions)} preguntas...")
    
    translated = []
    for i, q in enumerate(questions, 1):
        print(f"  [{i}/{len(questions)}] ", end='', flush=True)
        
        # Traducir pregunta
        translated_question = translate_text(q['question'])
        
        # Traducir opciones
        translated_answers = []
        for ans in q['answers']:
            translated_text = translate_text(ans['text'])
            translated_answers.append({
                'key': ans['key'],
                'text': translated_text
            })
        
        # Traducir explicación
        translated_explanation = ''
        if q.get('explanation'):
            translated_explanation = translate_text(q['explanation'])
        
        translated.append({
            'id': q['id'],
            'question': translated_question,
            'answers': translated_answers,
            'correctKeys': q['correctKeys'],
            'explanation': translated_explanation
        })
        
        print(f"✅ (Q{q['id']})")
    
    # Guardar JSON traducido
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Guardado: {output_file}\n")

def main():
    exams = [
        (
            'Descargables/Terraform/004/terraform-questions.json',
            'Descargables/Terraform/004/terraform-questions-es.json'
        ),
        (
            'Descargables/Vault/vault-questions.json',
            'Descargables/Vault/vault-questions-es.json'
        )
    ]
    
    print("=" * 60)
    print("🌐 Traductor de Exámenes a Español (Google Translate)")
    print("=" * 60)
    print(f"⏱️  Delays: 2-3 segundos + exponencial en errores")
    
    for input_file, output_file in exams:
        try:
            translate_exam(input_file, output_file)
        except Exception as e:
            print(f"❌ Error procesando {input_file}: {e}")
    
    print("\n" + "=" * 60)
    print("✅ Traducción completada")
    print("=" * 60)

if __name__ == '__main__':
    main()
