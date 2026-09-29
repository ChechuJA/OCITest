#!/usr/bin/env python3
"""
Translate exam questions from English to Spanish
Uses Google Translate API (free via googletrans library)
"""

import json
import os
from pathlib import Path

try:
    from deep_translator import GoogleTranslator
    translator = GoogleTranslator(source='en', target='es')
    print("✅ Usando Deep Translator")
except ImportError:
    print("⚠️  Instalando dependencias...")
    os.system('pip install deep-translator')
    from deep_translator import GoogleTranslator
    translator = GoogleTranslator(source='en', target='es')

def translate_text(text, max_length=5000):
    """Traducir texto con límite de caracteres"""
    if not text or len(text) < 3:
        return text
    
    try:
        # Dividir en fragmentos si es necesario
        if len(text) > max_length:
            chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
            translated = ' '.join([translator.translate(chunk) for chunk in chunks])
        else:
            translated = translator.translate(text)
        return translated
    except Exception as e:
        print(f"⚠️  Error en traducción: {e}")
        return text

def translate_questions(input_file, output_file):
    """Traducir preguntas de un JSON"""
    
    print(f"\n📖 Leyendo: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f"📝 Traduciendo {len(questions)} preguntas...")
    
    translated_questions = []
    for i, q in enumerate(questions, 1):
        # Mostrar progreso
        if i % 20 == 0:
            print(f"   {i}/{len(questions)}... ")
        
        # Traducir pregunta
        question_es = translate_text(q['question'])
        
        # Traducir opciones
        answers_es = []
        for answer in q['answers']:
            answers_es.append({
                'key': answer['key'],
                'text': translate_text(answer['text'])
            })
        
        # Traducir explicación
        explanation_es = translate_text(q.get('explanation', ''))
        
        translated_questions.append({
            'id': q['id'],
            'question': question_es,
            'answers': answers_es,
            'correctKeys': q['correctKeys'],
            'explanation': explanation_es
        })
    
    print(f"💾 Guardando: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated_questions, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Traducción completada: {len(translated_questions)} preguntas")

# Traducir Terraform 004
print("="*70)
print("TRADUCIENDO TERRAFORM 004")
print("="*70)
translate_questions(
    'Descargables/Terraform/004/terraform-questions.json',
    'Descargables/Terraform/004/terraform-questions-es.json'
)

# Traducir Vault
print("\n" + "="*70)
print("TRADUCIENDO VAULT")
print("="*70)
translate_questions(
    'Descargables/Vault/vault-questions.json',
    'Descargables/Vault/vault-questions-es.json'
)

print("\n" + "="*70)
print("✅ PROCESO COMPLETADO")
print("="*70)
print("\nArchivos generados:")
print("  • Descargables/Terraform/004/terraform-questions-es.json")
print("  • Descargables/Vault/vault-questions-es.json")
