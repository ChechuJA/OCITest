# ⚡ Quick Reference - Comandos y Formatos

## 🚀 Comandos Rápidos

### Procesar Archivos Word/PDF
```bash
# Extraer preguntas (genera JSON + MD)
python dev-tools/parse_terraform_docx.py

# Limpiar JSON corrupto
python dev-tools/fix_terraform_questions.py

# Regenerar Markdown desde JSON
python dev-tools/regenerate_markdown.py
```

### Validar Datos
```bash
# ✅ Validar JSON
python -c "import json; json.load(open('file.json')); print('✅ OK')"

# Contar preguntas
python -c "import json; print(len(json.load(open('file.json'))))"

# Verificar IDs secuenciales
python -c "
import json
data = json.load(open('file.json'))
ids = [q['id'] for q in data]
missing = set(range(1, max(ids)+1)) - set(ids)
print(f'Faltantes: {sorted(missing) if missing else \"Ninguno\"}')
"

# Verificar multi-respuesta
python -c "
import json
data = json.load(open('file.json'))
multi = [q['id'] for q in data if len(q['correctKeys']) > 1]
print(f'Multi-respuesta ({len(multi)}): {multi[:5]}...')
"
```

---

## 📝 Formato JSON (Copiar-Pegar)

```json
[
  {
    "id": 1,
    "question": "¿Cuál es el propósito de Terraform State?",
    "answers": [
      {"key": "A", "text": "Almacenar la configuración deseada"},
      {"key": "B", "text": "Almacenar el estado actual de la infraestructura"},
      {"key": "C", "text": "Realizar copias de seguridad automáticas"},
      {"key": "D", "text": "Compilar el código"}
    ],
    "correctKeys": ["B"],
    "explanation": "El archivo state mantiene el estado actual. Ref: https://www.terraform.io/docs/state"
  },
  {
    "id": 2,
    "question": "¿Cuál es la mejor práctica para compartir state? (Choose two.)",
    "answers": [
      {"key": "A", "text": "Archivos locales"},
      {"key": "B", "text": "Backend remoto"},
      {"key": "C", "text": "Email"},
      {"key": "D", "text": "Sistemas de versión (Git)"}
    ],
    "correctKeys": ["B", "D"],
    "explanation": "Usar backend remoto y control de versiones. Ref: https://..."
  }
]
```

---

## 📋 Formato Markdown (Copiar-Pegar)

```markdown
#### Q1. ¿Cuál es el propósito de Terraform State?

- [x] B. Almacenar el estado actual de la infraestructura
- [ ] A. Almacenar la configuración deseada
- [ ] C. Realizar copias de seguridad automáticas
- [ ] D. Compilar el código

> El archivo state mantiene el estado actual. Ref: https://www.terraform.io/docs/state

#### Q2. ¿Cuál es la mejor práctica para compartir state? (Choose two.)

- [x] B. Backend remoto
- [ ] A. Archivos locales
- [ ] C. Email
- [x] D. Sistemas de versión (Git)

> Usar backend remoto y control de versiones. Ref: https://...
```

---

## 📊 Estructura exams-catalog.json

```json
{
  "exams": [
    {
      "id": "hashicorp-terraform",
      "title": "HashiCorp Terraform Associate",
      "code": "004",
      "file": "Descargables/Terraform/terraform-questions.json",
      "questions": 200,
      "provider": "HashiCorp",
      "category": "Infrastructure",
      "description": "HashiCorp Certified: Terraform Associate certification"
    }
  ],
  "categories": [
    {
      "id": "Infrastructure",
      "name": "Cloud Infrastructure",
      "description": "..."
    }
  ],
  "metadata": {
    "version": "1.0.0",
    "totalExams": 12,
    "totalQuestions": 1237,
    "lastUpdated": "2026-09-28"
  }
}
```

---

## 🏷️ Convenciones

### IDs de Examen
```
✅ hashicorp-terraform, hashicorp-vault, oci-ai-foundations
❌ HashiCorp Terraform, terraform-associate, TerraformAssociate
```

### Códigos de Certificación
```
✅ "003", "004", "005", "1Z0-1122-25", "GH-300"
❌ Nombres completos, versiones sin formato
```

### Providers (en orden de precedencia)
```
1. GitHub          → aparece primero en dropdown
2. HashiCorp       → segundo
3. OCI             → tercero
4. MySQL           → cuarto (si hay)
```

### Categorías
```
- AI
- Infrastructure
- Database
- DevOps
```

---

## 🎯 Checklist Rápido

### Antes de Agregar Examen
- [ ] JSON válido
- [ ] IDs secuenciales (1, 2, 3, ...)
- [ ] Todas las opciones presentes (A, B, C, D)
- [ ] correctKeys es array `["A"]`
- [ ] Explicaciones con referencias
- [ ] Contar preguntas totales

### Antes de Hacer Commit
- [ ] exams-catalog.json actualizado
- [ ] totalExams incrementado
- [ ] totalQuestions recalculado
- [ ] lastUpdated con fecha de hoy
- [ ] Verificar en navegador (index.html)

---

## 🐛 Errores Comunes

### Error: "JSON inválido"
```bash
# Solución:
python -m json.tool file.json > /dev/null
# Si falla, buscar comillas dobles sin escapar
```

### Error: "Pregunta no carga"
- ✅ Verificar ruta en catalog
- ✅ Verificar archivo existe
- ✅ Ver consola (F12 en navegador)

### Error: "Respuesta marcada mal"
- ✅ Verificar correctKeys es array
- ✅ Verificar keys corresponden (A, B, C, D)
- ✅ Si multi-respuesta, debe decir "(Choose two.)"

---

## 🔄 Git Workflow

```bash
# Ver cambios
git status

# Agregar cambios
git add Descargables/Terraform/
git add exams-catalog.json

# Commit descriptivo
git commit -m "feat: Update Terraform to 004 (200 questions, 150 official)"

# Push
git push origin main
```

---

## 📱 Testing Local

### Web Quiz
1. Abrir `index.html` en navegador
2. Seleccionar Provider (HashiCorp)
3. Seleccionar Examen (Terraform 004)
4. Responder 3-5 preguntas
5. Verificar: Timer, progreso, almacenamiento

### CLI Quiz
```bash
python quiz.py
# Seleccionar banco
# Seleccionar modo
# Responder 2-3 preguntas
# Presionar X para ver explicación
```

---

## 💾 Estructura de Carpetas (Referencia)

```
Descargables/
├── GH-300/
│   ├── gh300-questions.json          # 129 Q
│   ├── gh300-questions.md
│   └── README.md
├── Terraform/
│   ├── terraform-questions.json      # 200 Q (actualizado)
│   ├── terraform-questions.md
│   └── README.md
└── Vault/                            # NUEVO
    ├── vault-questions.json          # 200 Q
    ├── vault-questions.md
    └── README.md

Nuevos/
├── OCI AI Foundations 1Z0-1122-25.md
├── MySQL Database Developer 1Z0-909.md
└── ...
```

---

## 🎓 Estado Actual

| Examen | Q | Ubicación | Status |
|--------|---|-----------|--------|
| OCI AI (Oficial) | 41 | quiz.js | ✅ |
| OCI AI (Optional) | 34 | quiz.js | ✅ |
| OCI AI 1Z0-1122-25 | 44 | Nuevos/ | ✅ |
| AI Vector Search | 50 | Nuevos/ | ✅ |
| OCI Foundations (Curated) | 39 | Nuevos/ | ✅ |
| OCI Foundations (Full) | 47 | Nuevos/ | ✅ |
| MySQL Developer | 77 | Nuevos/ | ✅ |
| MySQL Implementation | 52 | Nuevos/ | ✅ |
| **Terraform 003** | **378** | Descargables/ | ✅ |
| GitHub GH-300 | 129 | Descargables/ | ✅ |
| **(Vacío)** | **-** | - | - |
| **TOTAL** | **891** | - | ✅ |

**Después de actualización:**
- Terraform 004: 200 Q (reemplaza 378)
- Vault: 200 Q (nuevo)
- **TOTAL**: ~937 Q

---

## 🚀 Próximos Pasos

1. **Tú**: Pasa los archivos (Terraform 004 + Vault)
2. **Yo**: Extraigo y muestro preview
3. **Tú**: Apruebas cambios
4. **Yo**: Deploy + testing
5. **Ambos**: ✅ Listo

---

*Última actualización: 2026-09-28*  
*Referencia rápida - Consulta INSTRUCCIONES-CLARAS.md para detalles*
