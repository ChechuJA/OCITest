#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# Leer el archivo
with open('Descargables/Terraform/004/terraform-questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Diccionario de correcciones para preguntas con recuadros
# Basado en las fotos que pasó el usuario
corrections = {
    18: {
        "question": '''A resource block is shown in the Exhibit space of this page.

```
resource "aws_vpc" "main" {
  name = "test"
}
```

What is the provider for this resource?''',
        "answers": [
            {'key': 'A', 'text': 'main'},
            {'key': 'B', 'text': 'vpc'},
            {'key': 'C', 'text': 'aws'},
            {'key': 'D', 'text': 'test'},
        ],
        "correctKeys": ['C']
    },
    26: {
        "question": '''A variable block is shown in the Exhibit space of this page.

```
variable "tags"{
  description = "Metadata tags for resources"
  type = _____________
}
```

You will use this variable as the value for the tags argument in several resources. The data format must be a set of key value pairs. Which type argument would you use?'''
    },
    42: {
        "question": '''You have a saved execution plan containing desired changes for infrastructure managed by Terraform. After running the command terraform apply my.tfplan, you receive the error shown in the Exhibit space on this page.

```
Error: Saved plan is stale

The given plan file can no longer be applied because the state was changed by another operation after the plan was created.
```

How can you apply the desired changes? (Choose two.)'''
    },
    53: {
        "question": '''The Exhibit section of this page shows part of a configuration you've been asked to update.

```
data "azurerm_resource_group" "example"{
  name = var.resource_group_name
}

resource "azurerm_virtual_network" "example"{
  name = ____________
}
```

The name of the Azure Virtual Network should be set to the name of the resource group followed by a dash and the word "vnet". Which expression fulfils this requirement?'''
    },
    55: {
        "question": '''A resource block is shown in the Exhibit space of this page.

```
resource "aws_instance" "web"{
  count = 2
  name = "terraform-${count.index}"
}
```

How do you reference the name value of the second instance of this resource?'''
    },
    59: {
        "question": '''The Terraform configuration shown in the Exhibit space on this page will create a new AWS instance.

```
data "aws_instance" "web"{
  filter{
    name = "tag:Name"
    values = ["web"]
  }
}
```'''
    },
    62: {
        "question": '''A data source is shown in the Exhibit space of this page.

```
data "aws_ami" "web"{
  most_recent = true
  owners = ["self"]
  tags = {
    Name = "web-server"
  }
}
```

How do you reference the id attribute of this data source?'''
    },
    63: {
        "question": '''A resource block is shown in the Exhibit space of this page.

```
resource "kubernetes_namespace" "example"{
  name = "test"
}
```

How would you reference the attribute name of this resource in HCL?'''
    },
    64: {
        "question": '''You need to deploy resources into two different regions in the same Terraform configuration using the block in the Exhibit space on this page.

```
provider "aws"{
  region = "us-east-1"
}

provider "aws"{
  region = "us-west-2"
}
```

What do you need to add to the provider configuration to deploy the resource to the us-west-2 AWS region?'''
    },
    65: {
        "question": '''Two resources blocks are shown in the Exhibit space on this page: azurerm_linux_web_app, and azurerm_role_assignment.

```
resource "azurerm_linux_web_app" "app"{
  name = "example-app"
  resource_group_name = azurerm_resource_group.rg.name
  location = azurerm_resource_group.rg.location
  service_plan_id = azurerm_service_plan.plan.id

  identity{
    type = "UserAssigned"
    identity_ids = [azurerm_user_assigned_identity.app.id]
  }
}

resource "azurerm_role_assignment" "kv_access"{
  scope = azurerm_key_vault.kv.id
  role_definition_name = "Key Vault Secrets User"
  principal_id = azurerm_user_assigned_identity.identity.app.principal_id
}
```

When provisioned, the web app will use the role assignment during creation, so the role assignment must be created first.

How do you ensure the azurerm_role_assignment resource is created first?'''
    },
    84: {
        "question": '''Your configuration defines the module block shown in the Exhibit space of this page.

```
module "production"{
  source = "./modules/web_stack"
}
```

This module declares an output named hostnames.
How do you access the value of this output?'''
    },
    85: {
        "question": '''Which argument can you set on a module block to prevent Terraform from updating the module's configuration during an init or get operation?'''
    },
    137: {
        "question": '''A module block is shown in the Exhibit space of this page.

```
module "vpc"{
  source = "terraform-awsmodules/vpc/aws"
  version = "~>4.0"
}
```

That module block limits the module version to major version 4.
True or False?'''
    },
    144: {
        "question": '''terraform apply is failing with the following error.

```
Error loading state: AccessDenied: Access Denied status code: 403, request id: 288766CE5CCA2440, host id: web.example.com
```

What next step should you take to determine the root cause of the problem?'''
    },
    159: {
        "question": '''A module block is shown in the Exhibit space of this page.

```
module "consul"{
  source = "hashicorp/consul/aws"
}
```

When you use a module block to reference a module from the Terraform Registry such as the one in the example, how do you specify version 1.0.0 of the module?'''
    },
    166: {
        "question": '''You are using a networking module in your Terraform configuration with the name "my_network". In your main configuration, you are trying to access the "vnet_id" attribute from this module with the following code:

```
resource "aws_instance" "example"{
  ami = "ami-0c55b2a94c9b82a81"
  instance_type = "t2.micro"
  subnet_id = module.my_network.vnet_id
}

output "net_id"{
  value = module.my_network.vnet_id
}
```

When you run "terraform validate", you encounter the following error:

```
Error: Reference to undeclared output value on main.tf line 12, in output "net_id":
12: value = module.my_network.vnet_id
```

What must you do to successfully retrieve the "vnet_id" value from your networking module?'''
    },
    169: {
        "question": '''You decide to move a Terraform state file to Amazon S3 from another location. You write the code shown in the Exhibit space into a file called backend.tf.

```
terraform{
  backend "s3"{
    bucket = "my-tf-bucket"
    region = "us-east-1"
  }
}
```

Which command will migrate your current state file to the new S3 backend?'''
    }
}

# Aplicar correcciones
updated_count = 0
for q in data:
    if q['id'] in corrections:
        old_q = q['question']
        new_q = corrections[q['id']].get('question', old_q)
        q['question'] = new_q
        
        if 'answers' in corrections[q['id']]:
            q['answers'] = corrections[q['id']]['answers']
        
        if 'correctKeys' in corrections[q['id']]:
            q['correctKeys'] = corrections[q['id']]['correctKeys']
        
        print(f"✓ Q{q['id']} actualizada con recuadro en formato código")
        updated_count += 1

# Guardar
with open('Descargables/Terraform/004/terraform-questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ {updated_count} preguntas actualizadas con recuadros en formato código")
