#!/usr/bin/env python3
"""
Script para procesar y numerar preguntas en archivos de exámenes markdown.
Convierte "#### Q." a "#### Q1.", "#### Q2.", etc.
"""

import re
import sys
from pathlib import Path

def process_exam_file(filepath):
    """Procesa un archivo de examen, numerando las preguntas secuencialmente."""
    print(f"\n📄 Procesando: {filepath.name}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Contar preguntas antes
    questions_before = content.count('#### Q.')
    print(f"   Preguntas encontradas: {questions_before}")
    
    if questions_before == 0:
        print("   ⚠️  No se encontraron preguntas con formato '#### Q.'")
        return False
    
    # Numerar preguntas secuencialmente
    question_num = 1
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        if line.startswith('#### Q.'):
            # Reemplazar "#### Q." por "#### Q[num]."
            new_line = line.replace('#### Q.', f'#### Q{question_num}.', 1)
            new_lines.append(new_line)
            question_num += 1
        else:
            new_lines.append(line)
    
    new_content = '\n'.join(new_lines)
    
    # Guardar archivo procesado
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"   ✅ Archivo actualizado con {question_num - 1} preguntas numeradas")
    return True

def main():
    """Procesa todos los archivos .md en la carpeta Nuevos."""
    nuevos_dir = Path(r'c:\Github\Nuevos')
    
    if not nuevos_dir.exists():
        print(f"❌ Error: La carpeta {nuevos_dir} no existe")
        return 1
    
    # Buscar todos los archivos .md
    md_files = list(nuevos_dir.glob('*.md'))
    
    if not md_files:
        print(f"❌ No se encontraron archivos .md en {nuevos_dir}")
        return 1
    
    print(f"🔍 Encontrados {len(md_files)} archivos markdown")
    print("=" * 60)
    
    processed = 0
    for md_file in sorted(md_files):
        if process_exam_file(md_file):
            processed += 1
    
    print("\n" + "=" * 60)
    print(f"✨ Procesamiento completado: {processed}/{len(md_files)} archivos actualizados")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
