#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# Leer el archivo
with open('Descargables/Terraform/004/terraform-questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Q042 - Multi-respuesta: terraform apply my.tfplan con error "Saved plan is stale"
for q in data:
    if q['id'] == 42:
        q['question'] = '''You have a saved execution plan containing desired changes for infrastructure managed by Terraform. After running the command terraform apply my.tfplan, you receive the error shown in the Exhibit space on this page.

Error: Saved plan is stale

The given plan file can no longer be applied because the state was changed by another operation after the plan was created.

How can you apply the desired changes? (Choose two.)'''
        q['answers'] = [
            {'key': 'A', 'text': 'Generate a new execution plan file with terraform plan, and apply the new plan.'},
            {'key': 'B', 'text': 'Run terraform apply without the saved execution plan.'},
            {'key': 'C', 'text': 'Refresh the current state data using the -refresh-only flag.'},
            {'key': 'D', 'text': 'Force the apply command by adding the flag -lock=false.'},
            {'key': 'E', 'text': 'Update the current plan file using the terraform state push command.'},
        ]
        q['correctKeys'] = ['A', 'B']
        print("✓ Q42 actualizada (multi-respuesta)")

    # Q064 - Sobre provider con alias para múltiples regiones
    elif q['id'] == 64:
        q['question'] = '''You need to deploy resources into two different regions in the same Terraform configuration using the block in the Exhibit space on this page.

provider "aws"{
  region = "us-east-1"
}

provider "aws"{
  region = "us-west-2"
}

What do you need to add to the provider configuration to deploy the resource to the us-west-2 AWS region?'''
        q['answers'] = [
            {'key': 'A', 'text': 'resource "aws_instance" "example-us-west-2"{\n  ami = data.aws_ami.ubuntu.id\n  instance_type = "t3.micro"\n}'},
            {'key': 'B', 'text': 'provider "aws"{\n  region = "us-east-1"\n}\n\nprovider "aws" "west"{\n  region = "us-west-2"\n}'},
            {'key': 'C', 'text': 'provider "aws_west"{\n  region = "us-west-2"\n}'},
            {'key': 'D', 'text': 'provider "aws"{\n  region = "us-east-1"\n}\n\nprovider "aws"{\n  alias = "west"\n  region = "us-west-2"\n}'},
        ]
        q['correctKeys'] = ['D']
        print("✓ Q64 actualizada")

# Guardar JSON actualizado
with open('Descargables/Terraform/004/terraform-questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Q42 y Q64 actualizadas en JSON")

# ========================================
# Regenerar markdown desde JSON
# ========================================

markdown_content = "# Terraform Associate Certification (004) - Question Bank\n\n"
markdown_content += f"**Total Questions:** {len(data)}\n"
markdown_content += "**Last Updated:** 2025-12-29\n\n"

for q in data:
    markdown_content += f"#### Q{q['id']}. {q['question'].split(chr(10))[0]}\n\n"
    
    # Agregar pregunta completa si tiene múltiples líneas
    lines = q['question'].split('\n')
    if len(lines) > 1:
        markdown_content += f"{q['question']}\n\n"
    
    # Agregar opciones
    for ans in q['answers']:
        is_correct = ans['key'] in q['correctKeys']
        checkbox = "[x]" if is_correct else "[ ]"
        markdown_content += f"- {checkbox} {ans['key']}. {ans['text']}\n"
    
    # Agregar explicación
    if 'explanation' in q and q['explanation']:
        markdown_content += f"\n> **Explanation:** {q['explanation']}\n"
    
    markdown_content += "\n---\n\n"

# Guardar markdown
with open('Descargables/Terraform/004/terraform-questions.md', 'w', encoding='utf-8') as f:
    f.write(markdown_content)

print("✅ Markdown regenerado desde JSON")
print(f"📄 Archivo: Descargables/Terraform/004/terraform-questions.md ({len(data)} preguntas)")
