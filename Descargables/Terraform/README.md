# HashiCorp Terraform - Recursos de Estudio

## Documentación Oficial

### Terraform Core
- **Documentación oficial**: https://developer.hashicorp.com/terraform/docs
- **Tutoriales interactivos**: https://developer.hashicorp.com/terraform/tutorials
- **CLI Commands**: https://developer.hashicorp.com/terraform/cli/commands

### Terraform Language
- **Configuration Language**: https://developer.hashicorp.com/terraform/language
- **HCL Syntax**: https://developer.hashicorp.com/terraform/language/syntax
- **Variables**: https://developer.hashicorp.com/terraform/language/values/variables
- **Outputs**: https://developer.hashicorp.com/terraform/language/values/outputs
- **Functions**: https://developer.hashicorp.com/terraform/language/functions

### State Management
- **State**: https://developer.hashicorp.com/terraform/language/state
- **Remote State**: https://developer.hashicorp.com/terraform/language/state/remote
- **State Locking**: https://developer.hashicorp.com/terraform/language/state/locking
- **Backends**: https://developer.hashicorp.com/terraform/language/settings/backends

## Certificación Terraform Associate

### Guías de Estudio
- **Exam Review**: https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-review-003
- **Study Guide**: https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-study-003
- **Sample Questions**: https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-questions

### Objetivos del Examen (003)
1. Understand infrastructure as code (IaC) concepts
2. Understand the purpose of Terraform (vs other IaC)
3. Understand Terraform basics
4. Use Terraform outside of core workflow
5. Interact with Terraform modules
6. Use the core Terraform workflow
7. Implement and maintain state
8. Read, generate, and modify configuration
9. Understand Terraform Cloud capabilities

## Providers

### AWS Provider
- **AWS Provider**: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
- **AWS Resources**: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources

### Google Cloud Provider
- **GCP Provider**: https://registry.terraform.io/providers/hashicorp/google/latest/docs
- **Terraformer (import GCP resources)**: https://cloud.google.com/docs/terraform

### Azure Provider
- **Azure Provider**: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs

## Terraform Cloud & Enterprise

### Terraform Cloud
- **Getting Started**: https://developer.hashicorp.com/terraform/cloud-docs
- **Workspaces**: https://developer.hashicorp.com/terraform/cloud-docs/workspaces
- **VCS Integration**: https://developer.hashicorp.com/terraform/cloud-docs/vcs
- **Sentinel Policies**: https://developer.hashicorp.com/sentinel/docs/terraform

### Terraform Enterprise
- **Documentation**: https://developer.hashicorp.com/terraform/enterprise

## Módulos

### Module Registry
- **Public Registry**: https://registry.terraform.io/
- **Publishing Modules**: https://developer.hashicorp.com/terraform/registry/modules/publish
- **Module Sources**: https://developer.hashicorp.com/terraform/language/modules/sources

### Best Practices
- **Module Structure**: https://developer.hashicorp.com/terraform/language/modules/develop/structure
- **Module Composition**: https://developer.hashicorp.com/terraform/language/modules/develop/composition

## Conceptos Avanzados

### Provisioners
- **Provisioners**: https://developer.hashicorp.com/terraform/language/resources/provisioners
- **local-exec**: https://developer.hashicorp.com/terraform/language/resources/provisioners/local-exec
- **remote-exec**: https://developer.hashicorp.com/terraform/language/resources/provisioners/remote-exec
- **null_resource**: https://registry.terraform.io/providers/hashicorp/null/latest/docs/resources/resource

### Import & Migration
- **terraform import**: https://developer.hashicorp.com/terraform/cli/import
- **State Migration**: https://developer.hashicorp.com/terraform/cli/commands/init#backend-initialization
- **Moved Blocks**: https://developer.hashicorp.com/terraform/language/modules/develop/refactoring

### Security & Secrets
- **Managing Secrets**: https://blog.gruntwork.io/a-comprehensive-guide-to-managing-secrets-in-your-terraform-code-1d586955ace1
- **Sensitive Data**: https://developer.hashicorp.com/terraform/language/values/variables#suppressing-values-in-cli-output

## Hands-on Labs

### HashiCorp Learn
- **Get Started**: https://developer.hashicorp.com/terraform/tutorials/aws-get-started
- **Configuration Language**: https://developer.hashicorp.com/terraform/tutorials/configuration-language
- **Modules**: https://developer.hashicorp.com/terraform/tutorials/modules
- **State**: https://developer.hashicorp.com/terraform/tutorials/state

### Katacoda (Archivado)
- Nota: Los labs de Katacoda fueron migrados a HashiCorp Learn

## Comunidad y Recursos

### GitHub
- **Terraform Core**: https://github.com/hashicorp/terraform
- **Terraform Providers**: https://github.com/terraform-providers

### Blog Posts
- **HashiCorp Blog**: https://www.hashicorp.com/blog/products/terraform
- **Infrastructure as Code Best Practices**: https://docs.microsoft.com/en-us/azure/devops/learn/what-is-infrastructure-as-code

### Videos
- **HashiCorp YouTube**: https://www.youtube.com/c/HashiCorp
- **Terraform Tutorials**: https://www.youtube.com/playlist?list=PL81sUbsFNc5bDS1lH0HPJFyBnAP8Iv-t0

## Tips para el Examen

### Comandos Esenciales
```bash
terraform init       # Inicializar directorio
terraform plan       # Ver cambios propuestos
terraform apply      # Aplicar cambios
terraform destroy    # Destruir infraestructura
terraform refresh    # Actualizar state con infraestructura real
terraform validate   # Validar sintaxis
terraform fmt        # Formatear código
terraform import     # Importar recursos existentes
terraform state      # Gestionar state
terraform taint      # Marcar recurso para recrear
```

### Workflow Core
1. **Write** - Escribir configuración
2. **Plan** - Revisar cambios
3. **Apply** - Aplicar cambios

### Meta-Arguments Importantes
- `depends_on` - Dependencias explícitas
- `count` - Crear múltiples instancias
- `for_each` - Iterar sobre map/set
- `provider` - Provider específico
- `lifecycle` - Control del ciclo de vida
- `provisioner` - Provisioners

### Variables y Outputs
- Variables: `var.variable_name`
- Local values: `local.local_name`
- Resource attributes: `resource_type.resource_name.attribute`
- Data sources: `data.data_type.data_name.attribute`
- Module outputs: `module.module_name.output_name`

### Backend Types
- `local` - Local (default)
- `remote` - Terraform Cloud
- `s3` - AWS S3
- `azurerm` - Azure Storage
- `gcs` - Google Cloud Storage
- `consul` - HashiCorp Consul
- `http` - REST API

## Notas del Examen

- **Duración**: 60 minutos
- **Formato**: Multiple choice y scenarios
- **Passing score**: 70%
- **Precio**: $70.50 USD
- **Validez**: 2 años
- **Idiomas**: Inglés
