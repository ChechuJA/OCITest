#!/usr/bin/env python3
"""
Traductor de Vault (86 preguntas) con batches pequeños para evitar rate limiting.
Traduce en grupos de 3 preguntas con pausa de 5 segundos entre batches.
"""

import json
import time
import random
from pathlib import Path
from deep_translator import GoogleTranslator

def translate_text(text):
    """Traducir texto con reintentos."""
    max_retries = 2
    for attempt in range(max_retries):
        try:
            translator = GoogleTranslator(source_language='en', target_language='es')
            result = translator.translate(text)
            time.sleep(0.5)  # Pequeña pausa entre requests
            return result
        except Exception as e:
            if attempt < max_retries - 1:
                wait = 10 + (attempt * 5)
                print(f"    ⚠️  Error (reintentando en {wait}s)...")
                time.sleep(wait)
            else:
                print(f"    ❌ Fallido - usando original")
                return text
    return text

def main():
    input_file = 'Descargables/Vault/vault-questions.json'
    output_file = 'Descargables/Vault/vault-questions-es.json'
    
    print("=" * 60)
    print("🔐 Traduciendo Vault (86 preguntas)")
    print("=" * 60)
    print("Estrategia: Batches de 3 preguntas + 5seg pausa\n")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    translated = []
    batch_size = 3
    
    for i, q in enumerate(questions, 1):
        print(f"[{i:3d}/86] Pregunta {q['id']:3d}... ", end='', flush=True)
        
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
        
        print("✅")
        
        # Pausa cada batch_size preguntas
        if i % batch_size == 0 and i < len(questions):
            print(f"     ⏱️  Pausa de 5 segundos (batch {i}/{batch_size})")
            time.sleep(5)
    
    # Guardar JSON traducido
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Guardado: {output_file}")
    print(f"📊 {len(translated)} preguntas traducidas")
    print("=" * 60)

if __name__ == '__main__':
    main()
