#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# Leer el archivo
with open('Descargables/Terraform/004/terraform-questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Q26 - Agregar recuadro en pregunta y reducir a 4 opciones
for q in data:
    if q['id'] == 26:
        q['question'] = '''A variable block is shown in the Exhibit space of this page.

variable "tags"{
  description = "Metadata tags for resources"
  type = _____________
}

You will use this variable as the value for the tags argument in several resources. The data format must be a set of key value pairs. Which type argument would you use?'''
        q['answers'] = q['answers'][:4]
        print(f"✓ Q26 actualizada")

    # Q53 - Reformatear: mover pregunta y quitar opción E
    elif q['id'] == 53:
        q['question'] = '''The Exhibit section of this page shows part of a configuration you've been asked to update.

data "azurerm_resource_group" "example"{
  name = var.resource_group_name
}

resource "azurerm_virtual_network" "example"{
  name = ____________
}

The name of the Azure Virtual Network should be set to the name of the resource group followed by a dash and the word "vnet". Which expression fulfils this requirement?'''
        q['answers'] = [q['answers'][i] for i in [1, 2, 3, 4]]  # B, C, D, E -> A, B, C, D
        q['answers'][0]['key'] = 'A'
        q['answers'][1]['key'] = 'B'
        q['answers'][2]['key'] = 'C'
        q['answers'][3]['key'] = 'D'
        q['correctKeys'] = ['D']  # La E pasa a ser D
        print(f"✓ Q53 actualizada")

    # Q55 - Reformatear: mover pregunta y reducir a 4 opciones
    elif q['id'] == 55:
        q['question'] = '''A resource block is shown in the Exhibit space of this page.

resource "aws_instance" "web"{
  count = 2
  name = "terraform-${count.index}"
}

How do you reference the name value of the second instance of this resource?'''
        q['answers'] = q['answers'][:4]  # Solo A, B, C, D (ignorar E, F)
        q['correctKeys'] = ['D']  # aws_instance.web[1].name es index 1 (segundo)
        print(f"✓ Q55 actualizada")

    # Q59 - Agregar recuadro en pregunta
    elif q['id'] == 59:
        q['question'] = '''The Terraform configuration shown in the Exhibit space on this page will create a new AWS instance.

data "aws_instance" "web"{
  filter{
    name = "tag:Name"
    values = ["web"]
  }
}'''
        print(f"✓ Q59 actualizada")

    # Q62 - Reformatear: mover pregunta y reducir a 4 opciones
    elif q['id'] == 62:
        q['question'] = '''A data source is shown in the Exhibit space of this page.

data "aws_ami" "web"{
  most_recent = true
  owners = ["self"]
  tags = {
    Name = "web-server"
  }
}

How do you reference the id attribute of this data source?'''
        q['answers'] = q['answers'][:4]  # A, B, C, D (ignorar E)
        q['correctKeys'] = ['A']  # data.aws_ami.web.id es la correcta
        print(f"✓ Q62 actualizada")

    # Q63 - Reformatear: mover pregunta y reducir a 4 opciones
    elif q['id'] == 63:
        q['question'] = '''A resource block is shown in the Exhibit space of this page.

resource "kubernetes_namespace" "example"{
  name = "test"
}

How would you reference the attribute name of this resource in HCL?'''
        q['answers'] = q['answers'][:4]  # A, B, C, D (ignorar E)
        q['correctKeys'] = ['C']  # kubernetes_namespace.example.name
        print(f"✓ Q63 actualizada")

    # Q65 - Reformatear: mover pregunta y quitar opciones E, F
    elif q['id'] == 65:
        q['question'] = '''Two resources blocks are shown in the Exhibit space on this page: azurerm_linux_web_app, and azurerm_role_assignment.

When provisioned, the web app will use the role assignment during creation, so the role assignment must be created first.

How do you ensure the azurerm_role_assignment resource is created first?'''
        # Reordenar: C->A, D->B, E->C, F->D
        q['answers'] = [
            {'key': 'A', 'text': q['answers'][2]['text']},  # C -> A
            {'key': 'B', 'text': q['answers'][3]['text']},  # D -> B
            {'key': 'C', 'text': q['answers'][4]['text']},  # E -> C
            {'key': 'D', 'text': q['answers'][5]['text']},  # F -> D
        ]
        q['correctKeys'] = ['A']  # "Add a depends_on argument to the azurerm_linux_web_app"
        print(f"✓ Q65 actualizada")

# Guardar
with open('Descargables/Terraform/004/terraform-questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n✅ Todas las preguntas actualizadas")
