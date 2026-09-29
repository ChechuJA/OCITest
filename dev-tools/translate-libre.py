#!/usr/bin/env python3
"""
Traductor usando LibreTranslate (API pública, sin rate limiting)
"""

import json
import requests
import time
from pathlib import Path

# API LibreTranslate pública
LIBREAPI_URL = "https://libretranslate.de/translate"

def translate_batch(texts, delay=0.5):
    """Traduce un lote de textos"""
    try:
        time.sleep(delay)
        
        data = {
            "q": texts,
            "source": "en",
            "target": "es"
        }
        
        response = requests.post(LIBREAPI_URL, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result.get('translatedText'), list):
                return result['translatedText']
            else:
                return [result['translatedText']]
        else:
            print(f"⚠️  Error: {response.status_code}")
            return texts
    except Exception as e:
        print(f"⚠️  Error: {e}")
        return texts

def translate_exam(input_file, output_file):
    """Traduce un archivo JSON completo"""
    
    print(f"\n📖 Cargando: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f"📝 Total de preguntas: {len(questions)}")
    
    translated = []
    total = len(questions)
    
    for i, question in enumerate(questions, 1):
        print(f"[{i:3d}/{total}] Q{question['id']:3d}", end=" ", flush=True)
        
        # Recolectar todos los textos para traducir
        texts_to_translate = [question['question']]
        for answer in question['answers']:
            texts_to_translate.append(answer['text'])
        if question.get('explanation') and not question['explanation'].startswith('http'):
            texts_to_translate.append(question['explanation'])
        
        # Traducir en lote
        translated_texts = translate_batch(texts_to_translate, delay=0.3)
        
        # Reconstruir
        idx = 0
        q_text = translated_texts[idx] if idx < len(translated_texts) else question['question']
        idx += 1
        
        translated_answers = []
        for answer in question['answers']:
            a_text = translated_texts[idx] if idx < len(translated_texts) else answer['text']
            translated_answers.append({
                'key': answer['key'],
                'text': a_text
            })
            idx += 1
        
        exp_text = question['explanation']
        if question.get('explanation') and not question['explanation'].startswith('http'):
            exp_text = translated_texts[idx] if idx < len(translated_texts) else question['explanation']
        
        translated_q = {
            'id': question['id'],
            'question': q_text,
            'answers': translated_answers,
            'correctKeys': question['correctKeys'],
            'explanation': exp_text
        }
        
        translated.append(translated_q)
        print("✓")
    
    # Guardar
    print(f"\n💾 Guardando: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Completado: {output_file}")

if __name__ == '__main__':
    base_dir = Path(__file__).parent.parent
    
    # Terraform 004
    print("=" * 70)
    print("TRADUCIENDO: Terraform 004 (221 preguntas)")
    print("Usando: LibreTranslate (API pública, sin rate limiting)")
    print("=" * 70)
    terraform_input = base_dir / 'Descargables' / 'Terraform' / '004' / 'terraform-questions.json'
    terraform_output = base_dir / 'Descargables' / 'Terraform' / '004' / 'terraform-questions-es.json'
    translate_exam(str(terraform_input), str(terraform_output))
    
    print("\n⏳ Esperando 5 segundos...")
    time.sleep(5)
    
    # Vault
    print("\n" + "=" * 70)
    print("TRADUCIENDO: Vault (86 preguntas)")
    print("=" * 70)
    vault_input = base_dir / 'Descargables' / 'Vault' / 'vault-questions.json'
    vault_output = base_dir / 'Descargables' / 'Vault' / 'vault-questions-es.json'
    translate_exam(str(vault_input), str(vault_output))
    
    print("\n✨ ¡Traducción completada!")
