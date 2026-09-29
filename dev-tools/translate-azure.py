#!/usr/bin/env python3
"""
Traductor de preguntas usando Azure Translator API
Más estable que Google Translate para este volumen
"""

import json
import requests
import time
from pathlib import Path

# Configurar credenciales de Azure
AZURE_KEY = ""  # Se pide al usuario
AZURE_REGION = "eastus"
AZURE_ENDPOINT = "https://api.cognitive.microsofttranslator.com"

def get_azure_key():
    """Pide la clave de Azure Translator al usuario"""
    key = input("\n🔑 Ingresa tu clave de Azure Translator API: ").strip()
    if not key:
        print("❌ Clave requerida")
        return None
    return key

def translate_text_azure(text, key, delay=1):
    """Traduce texto usando Azure Translator"""
    if not text or len(text.strip()) == 0:
        return text
    
    time.sleep(delay)
    
    try:
        url = f"{AZURE_ENDPOINT}/translate?api-version=3.0&from=en&to=es"
        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': AZURE_REGION,
            'Content-type': 'application/json'
        }
        
        body = [{'text': text}]
        response = requests.post(url, headers=headers, json=body)
        
        if response.status_code == 200:
            result = response.json()
            return result[0]['translations'][0]['text']
        else:
            print(f"❌ Error Azure: {response.status_code}")
            return text
    except Exception as e:
        print(f"❌ Error: {e}")
        return text

def translate_exam_azure(input_file, output_file, key, delay=1):
    """Traduce un archivo JSON completo"""
    
    print(f"\n📖 Cargando: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f"📝 Total de preguntas: {len(questions)}")
    print(f"⏱️  Delay entre traducciones: {delay}s")
    
    translated = []
    total = len(questions)
    
    for i, question in enumerate(questions, 1):
        print(f"\n[{i}/{total}] Pregunta {question['id']}", end="", flush=True)
        
        # Traducir pregunta
        q_text = translate_text_azure(question['question'], key, delay)
        print(f" ✓", end="", flush=True)
        
        # Traducir respuestas
        translated_answers = []
        for answer in question['answers']:
            a_text = translate_text_azure(answer['text'], key, delay)
            translated_answers.append({
                'key': answer['key'],
                'text': a_text
            })
            print(f".", end="", flush=True)
        
        # Traducir explicación
        exp_text = question['explanation']
        if question.get('explanation') and not question['explanation'].startswith('http'):
            exp_text = translate_text_azure(question['explanation'], key, delay)
        
        translated_q = {
            'id': question['id'],
            'question': q_text,
            'answers': translated_answers,
            'correctKeys': question['correctKeys'],
            'explanation': exp_text
        }
        
        translated.append(translated_q)
    
    # Guardar
    print(f"\n\n💾 Guardando: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Completado: {output_file}")

if __name__ == '__main__':
    key = get_azure_key()
    if not key:
        exit(1)
    
    base_dir = Path(__file__).parent.parent
    
    # Terraform 004
    print("\n" + "=" * 60)
    print("TRADUCIENDO: Terraform 004 (221 preguntas)")
    print("=" * 60)
    terraform_input = base_dir / 'Descargables' / 'Terraform' / '004' / 'terraform-questions.json'
    terraform_output = base_dir / 'Descargables' / 'Terraform' / '004' / 'terraform-questions-es.json'
    translate_exam_azure(str(terraform_input), str(terraform_output), key, delay=1)
    
    print("\n⏳ Esperando 10 segundos...")
    time.sleep(10)
    
    # Vault
    print("\n" + "=" * 60)
    print("TRADUCIENDO: Vault (86 preguntas)")
    print("=" * 60)
    vault_input = base_dir / 'Descargables' / 'Vault' / 'vault-questions.json'
    vault_output = base_dir / 'Descargables' / 'Vault' / 'vault-questions-es.json'
    translate_exam_azure(str(vault_input), str(vault_output), key, delay=1)
    
    print("\n✨ ¡Listo!")
