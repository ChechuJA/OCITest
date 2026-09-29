"""
Ver estructura detallada de Q1
"""
from pathlib import Path
from docx import Document

docx_path = Path(r"c:\Github\OCITest\Descargables\Terraform\004\source\HASHICORP TERRAFORM - 004.docx")
doc = Document(docx_path)

print("Párrafos 1-40 (primeras 3 preguntas):")
print("="*80)

for i, para in enumerate(doc.paragraphs[:40], 1):
    text = para.text.strip()
    prefix = ""
    if text == "Question.":
        prefix = "[QUESTION]"
    elif text == "Answer":
        prefix = "[ANSWER]"
    elif text.startswith("Correct"):
        prefix = "[CORRECT]"
    elif text.startswith("Explanation"):
        prefix = "[EXPLAIN]"
    elif text.startswith("Discussion"):
        prefix = "[DISCUSS]"
    else:
        prefix = "[TEXT]"
    
    print(f"{i:3} {prefix:12} {text[:70]}")
