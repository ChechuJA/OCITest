#!/usr/bin/env python3
"""
Traducir exámenes con delays para respetar límites de Google Translate
5 requests por segundo máximo
"""

import json
import time
from pathlib import Path

try:
    from deep_translator import GoogleTranslator
except ImportError:
    print("Instalando deep-translator...")
    import os
    os.system('pip install deep-translator -q')
    from deep_translator import GoogleTranslator

def translate_with_delay(text, delay=0.3):
    """Traducir con delay para respetar límites"""
    if not text or len(text) < 2:
        return text
    
    try:
        translator = GoogleTranslator(source='en', target='es')
        time.sleep(delay)  # Delay de 0.3 segundos
        return translator.translate(text)
    except Exception as e:
        print(f"⚠️  Error: {str(e)[:50]}... usando texto original")
        return text

def translate_questions(input_file, output_file):
    """Traducir preguntas de un JSON"""
    
    print(f"📖 Leyendo: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f"📝 Traduciendo {len(questions)} preguntas (esto toma ~{len(questions) * 0.3 / 60:.1f} minutos)...")
    print()
    
    translated_questions = []
    
    for i, q in enumerate(questions, 1):
        # Mostrar progreso cada 10
        if i % 10 == 0:
            print(f"   Progreso: {i}/{len(questions)} ({int(i*100/len(questions))}%)")
        
        try:
            # Traducir pregunta (más importante)
            question_es = translate_with_delay(q['question'], 0.25)
            
            # Traducir opciones
            answers_es = []
            for answer in q['answers']:
                text_es = translate_with_delay(answer['text'], 0.15)
                answers_es.append({
                    'key': answer['key'],
                    'text': text_es
                })
            
            # Traducir explicación
            explanation_es = translate_with_delay(q.get('explanation', ''), 0.2) if q.get('explanation') else ''
            
            translated_questions.append({
                'id': q['id'],
                'question': question_es,
                'answers': answers_es,
                'correctKeys': q['correctKeys'],
                'explanation': explanation_es
            })
        except Exception as e:
            print(f"❌ Error en pregunta {i}: {str(e)[:40]}")
            # Usar original si hay error
            translated_questions.append(q)
    
    print(f"\n💾 Guardando: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated_questions, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Completado: {len(translated_questions)} preguntas")
    return True

# Traducir Terraform 004
print("="*70)
print("TRADUCIENDO TERRAFORM 004 (221 preguntas)")
print("="*70)
if translate_questions(
    'Descargables/Terraform/004/terraform-questions.json',
    'Descargables/Terraform/004/terraform-questions-es.json'
):
    print("\n✅ Terraform 004 LISTO\n")

# Pequeña pausa entre traducciones
time.sleep(2)

# Traducir Vault
print("="*70)
print("TRADUCIENDO VAULT (86 preguntas)")
print("="*70)
if translate_questions(
    'Descargables/Vault/vault-questions.json',
    'Descargables/Vault/vault-questions-es.json'
):
    print("\n✅ Vault LISTO\n")

print("="*70)
print("✅ TODAS LAS TRADUCCIONES COMPLETADAS")
print("="*70)
