#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# Leer el archivo
with open('Descargables/Terraform/004/terraform-questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Q084 - Sobre module "production" y acceso a output "hostnames"
for q in data:
    if q['id'] == 84:
        q['question'] = '''Your configuration defines the module block shown in the Exhibit space of this page.

module "production"{
  source = "./modules/web_stack"
}

This module declares an output named hostnames.
How do you access the value of this output?'''
        q['answers'] = [
            {'key': 'A', 'text': 'production.hostnames'},
            {'key': 'B', 'text': 'module.production.hostnames'},
            {'key': 'C', 'text': 'web_stack.hostnames'},
            {'key': 'D', 'text': 'module.web_stack.hostnames'},
        ]
        q['correctKeys'] = ['B']
        print("✓ Q84 actualizada")

    # Q085 - Sobre argument en module block para prevenir actualizaciones
    elif q['id'] == 85:
        q['question'] = '''Which argument can you set on a module block to prevent Terraform from updating the module's configuration during an init or get operation?'''
        q['answers'] = [
            {'key': 'A', 'text': 'count'},
            {'key': 'B', 'text': 'lifecycle'},
            {'key': 'C', 'text': 'source'},
            {'key': 'D', 'text': 'version'},
        ]
        q['correctKeys'] = ['C']
        # Mantener la explicación original que está completa en las fotos
        print("✓ Q85 actualizada")

    # Q137 - Sobre module "vpc" con version "~>4.0"
    elif q['id'] == 137:
        q['question'] = '''A module block is shown in the Exhibit space on this page.

module "vpc"{
  source = "terraform-awsmodules/vpc/aws"
  version = "~>4.0"
}

That module block limits the module version to major version 4.
True or False?'''
        q['answers'] = [
            {'key': 'A', 'text': 'True'},
            {'key': 'B', 'text': 'False'},
        ]
        q['correctKeys'] = ['A']
        print("✓ Q137 actualizada")

    # Q144 - Sobre "terraform apply" failing con AccessDenied error
    elif q['id'] == 144:
        q['question'] = '''terraform apply is failing with the following error.

Error loading state: AccessDenied: Access Denied status code: 403, request id: 288766CE5CCA2440, host id: web.example.com

What next step should you take to determine the root cause of the problem?'''
        q['answers'] = [
            {'key': 'A', 'text': 'Run terraform login to reauthenticate with the provider.'},
            {'key': 'B', 'text': 'Review /var/log/terraform.log for error messages.'},
            {'key': 'C', 'text': 'Review syslog for Terraform error messages.'},
            {'key': 'D', 'text': 'Set TF_LOG=DEBUG.'},
        ]
        q['correctKeys'] = ['D']
        print("✓ Q144 actualizada")

    # Q159 - Sobre module block con version 1.0.0 del Terraform Registry
    elif q['id'] == 159:
        q['question'] = '''A module block is shown in the Exhibit space on this page.

module "consul"{
  source = "hashicorp/consul/aws"
}

When you use a module block to reference a module from the Terraform Registry such as the one in the example, how do you specify version 1.0.0 of the module?'''
        q['answers'] = [
            {'key': 'A', 'text': 'You cannot. Modules stored on the public Terraform Registry do not support versioning.'},
            {'key': 'B', 'text': 'Append ?ref=v1.0.0 argument to the source path.'},
            {'key': 'C', 'text': 'Add a version = "1.0.0" attribute to the module block.'},
            {'key': 'D', 'text': 'Nothing. Modules stored on the public Terraform module Registry always default to version 1.0.0.'},
        ]
        q['correctKeys'] = ['C']
        print("✓ Q159 actualizada")

    # Q166 - Sobre module "my_network" y acceso a "vnet_id"
    elif q['id'] == 166:
        q['question'] = '''You are using a networking module in your Terraform configuration with the name "my_network". In your main configuration, you are trying to access the "vnet_id" attribute from this module with the following code:

resource "aws_instance" "example"{
  ami = "ami-0c55b2a94c9b82a81"
  instance_type = "t2.micro"
  subnet_id = module.my_network.vnet_id
}

output "net_id"{
  value = module.my_network.vnet_id
}

When you run "terraform validate", you encounter the following error:

Error: Reference to undeclared output value on main.tf line 12, in output "net_id":
12: value = module.my_network.vnet_id

What must you do to successfully retrieve the "vnet_id" value from your networking module?'''
        q['answers'] = [
            {'key': 'A', 'text': 'Define the attribute "vnet_id" as a variable in the networking module.'},
            {'key': 'B', 'text': 'Change the referenced value to "module.my_network.outputs.vnet_id".'},
            {'key': 'C', 'text': 'Define the attribute "vnet_id" as an output in the networking module.'},
            {'key': 'D', 'text': 'Change the referenced value to "my_network.outputs.vnet_id".'},
        ]
        q['correctKeys'] = ['C']
        print("✓ Q166 actualizada")

    # Q169 - Sobre terraform init para migrar state a S3 backend
    elif q['id'] == 169:
        q['question'] = '''You decide to move a Terraform state file to Amazon S3 from another location. You write the code shown in the Exhibit space into a file called backend.tf.

terraform{
  backend "s3"{
    bucket = "my-tf-bucket"
    region = "us-east-1"
  }
}

Which command will migrate your current state file to the new S3 backend?'''
        q['answers'] = [
            {'key': 'A', 'text': 'terraform refresh'},
            {'key': 'B', 'text': 'terraform init'},
            {'key': 'C', 'text': 'terraform push'},
            {'key': 'D', 'text': 'terraform state'},
        ]
        q['correctKeys'] = ['B']
        print("✓ Q169 actualizada")

# Guardar
with open('Descargables/Terraform/004/terraform-questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n✅ Las 7 preguntas actualizadas")
