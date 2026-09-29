# 📋 Instrucciones Claras - Sistema de Exámenes de Certificación

## 🎯 Visión General

Este es un **sistema multi-examen interactivo** de certificaciones que combina:
- **Quiz web** (index.html + quiz.js) con soporte para múltiples exámenes
- **Quiz CLI** (quiz.py) para terminal
- **Catálogo centralizado** (exams-catalog.json) que índiza todos los exámenes
- **11 exámenes** con **837+ preguntas** totales

---

## 📁 Estructura de Carpetas

```
OCITest/
├── 📄 index.html                    # UI web del quiz (punto de entrada)
├── 📄 quiz.js                       # Motor del quiz web
├── 📄 quiz.py                       # Motor del quiz CLI
├── 📄 exam-loader.js                # Cargador de exámenes (JSON/MD)
├── 📄 style.css                     # Estilos
├── 📄 exams-catalog.json            # ⭐ CATÁLOGO CENTRAL
│
├── Descargables/                    # Exámenes en formato JSON
│   ├── GH-300/
│   │   ├── gh300-questions.json     # 129 preguntas (formato estándar)
│   │   ├── gh300-questions.md       # Preview legible
│   │   └── README.md                # Recursos de estudio
│   ├── Terraform/
│   │   ├── terraform-questions.json # 378 preguntas (TERRAFORM 003)
│   │   ├── terraform-questions.md   # Preview
│   │   └── README.md                # Recursos
│   └── OCI/
│       └── README.md                # Recursos
│
├── Nuevos/                          # Exámenes en formato Markdown
│   ├── OCI AI Foundations 1Z0-1122-25.md
│   ├── AI Vector Search Professional 1Z0-184-25.md
│   ├── OCI Foundations 1Z0-1085-25.md
│   └── MySQL *.md
│
├── dev-tools/                       # Scripts de procesamiento
│   ├── parse_terraform_docx.py      # Extrae preguntas de Word/PDF
│   ├── fix_terraform_questions.py   # Limpia y normaliza JSON
│   ├── regenerate_markdown.py       # JSON → Markdown
│   └── otros...
│
└── Otros examenes/                  # Backup de archivos fuente
```

---

## 📊 Exámenes Actuales (11 totales = 837 preguntas)

| # | Examen | Código | Preguntas | Formato | Ubicación |
|---|--------|--------|-----------|---------|-----------|
| 1 | OCI AI Foundations (Oficial) | - | 41 | Integrado | quiz.js |
| 2 | OCI AI Foundations (Opcional) | - | 34 | Integrado | quiz.js |
| 3 | OCI AI Foundations 1Z0-1122-25 | 1Z0-1122-25 | 44 | Markdown | Nuevos/ |
| 4 | AI Vector Search Professional | 1Z0-184-25 | 50 | Markdown | Nuevos/ |
| 5 | OCI Foundations (Curated) | 1Z0-1085-25 | 39 | Markdown | Nuevos/ |
| 6 | OCI Foundations (Full) | 1Z0-1085-25 | 47 | Markdown | Nuevos/ |
| 7 | MySQL Database Developer | 1Z0-909 | 77 | Markdown | Nuevos/ |
| 8 | MySQL Implementation | 1Z0-922 | 52 | Markdown | Nuevos/ |
| 9 | Terraform Associate | **003** | **378** | JSON | Descargables/Terraform/ |
| 10 | GitHub Copilot (GH-300) | GH-300 | 129 | JSON | Descargables/GH-300/ |
| 11 | (Vacío) | - | - | - | - |

---

## 📝 Formato Estándar de Preguntas

### JSON (Terraform, GH-300)

```json
[
  {
    "id": 1,
    "question": "Texto completo de la pregunta con todo el contexto",
    "answers": [
      {"key": "A", "text": "Primera opción"},
      {"key": "B", "text": "Segunda opción"},
      {"key": "C", "text": "Tercera opción"},
      {"key": "D", "text": "Cuarta opción"}
    ],
    "correctKeys": ["A"],  // ⚠️ SIEMPRE array, incluso si es una sola
    "explanation": "Explicación clara con referencias. Ref: https://docs.example.com"
  }
]
```

**Reglas críticas JSON:**
- ✅ `correctKeys` = **SIEMPRE array**: `["A"]` o `["B", "D"]`
- ✅ Las opciones en orden alfabético (A, B, C, D)
- ✅ Pregunta NO incluye las opciones
- ✅ Si es multi-respuesta, decir "(Choose two)" en la pregunta

### Markdown (OCI, MySQL)

```markdown
#### Q1. Texto de la pregunta

- [x] A. Opción correcta
- [ ] B. Opción incorrecta
- [ ] C. Opción incorrecta
- [ ] D. Opción incorrecta

> Explicación de por qué es correcta. Ref: https://docs.example.com
```

---

## 🔄 Catálogo Central (exams-catalog.json)

**Este archivo es la fuente única de verdad.**

```json
{
  "exams": [
    {
      "id": "hashicorp-terraform",           // ID único, lowercase con guiones
      "title": "HashiCorp Terraform Associate",
      "code": "003",                         // Código de certificación
      "file": "Descargables/Terraform/terraform-questions.json",
      "questions": 378,                      // Total de preguntas
      "provider": "HashiCorp",               // OCI, HashiCorp, GitHub, MySQL
      "category": "Infrastructure",          // AI, Infrastructure, Database, DevOps
      "description": "Descripción breve del examen"
    }
  ],
  "categories": [
    {"id": "AI", "name": "Artificial Intelligence", "description": "..."},
    {"id": "Infrastructure", "name": "Cloud Infrastructure", "description": "..."},
    {"id": "Database", "name": "Database", "description": "..."},
    {"id": "DevOps", "name": "DevOps", "description": "..."}
  ],
  "metadata": {
    "version": "1.0.0",
    "totalExams": 11,           // ⚠️ Actualizar cuando agregues examen
    "totalQuestions": 837,      // ⚠️ Sumar todas las preguntas
    "lastUpdated": "2025-12-26"
  }
}
```

---

## 🚀 Agregar un Nuevo Examen (Step-by-step)

### Paso 1: Preparar el archivo de preguntas

#### Opción A: Desde Word/PDF
```bash
python dev-tools/parse_terraform_docx.py
# Input:  Documento Word con formato:
#   Question 1
#   [Texto]
#   Correct Answer: B
#   [Explicación]
# Output: questions.json + questions.md
```

#### Opción B: Desde Markdown existente
- Copiar archivo .md
- Validar formato (#### Q1, opciones con - [x], explicación con >)

#### Opción C: Formato JSON directo
- Estructurar según schema JSON arriba
- Validar con: `python -c "import json; json.load(open('file.json'))"`

### Paso 2: Crear carpeta y archivos

```bash
# Para JSON (como Terraform, GH-300)
mkdir -p Descargables/NombreProvider/
cp questions.json Descargables/NombreProvider/

# Para Markdown (como OCI, MySQL)
cp questions.md Nuevos/Provider-Exam-Code.md

# Crear README con recursos
cat > Descargables/NombreProvider/README.md << 'EOF'
# Provider - Exam Name

## Documentación Oficial
- [Link oficial](https://example.com)

## Certificación
- Exam Topics
- Study Guide
- Practice Labs

## Tips
- Duración: XXX minutos
- Passing Score: XXX%
- Formato: Multiple choice
EOF
```

### Paso 3: Actualizar exams-catalog.json

Agregar entrada en `exams` array:

```json
{
  "id": "provider-exam-id",                 // Único, lowercase-con-guiones
  "title": "Nombre Completo del Examen",
  "code": "EXAM-CODE",                      // Código oficial (ej: "004")
  "file": "Descargables/Provider/questions.json",  // o Nuevos/*.md
  "questions": 150,                         // Número exacto de Q
  "provider": "Provider Name",
  "category": "Infrastructure",
  "description": "Descripción para el dropdown"
}
```

### Paso 4: Actualizar metadata

```json
"metadata": {
  "version": "1.0.0",
  "totalExams": 12,                    // ← Incrementar
  "totalQuestions": 987,              // ← Recalcular (837 + 150)
  "lastUpdated": "2026-09-28"         // ← Hoy
}
```

---

## 🔄 Workflow: Actualizar Terraform (003 → 004) + Agregar Vault

### Tu flujo (resumido):

1. **Pasas archivos** (Word/PDF) con:
   - Terraform 004: Q1-Q150 (OFICIALES) + Q151-Q200 (opcionales)
   - Vault: Q1-Q150 (OFICIALES) + Q151-Q300 (opcionales)

2. **Yo extraigo** preguntas con parser
   - Valido formato JSON
   - Genero Markdown preview
   - Confirmo contigo antes de commitear

3. **Actualizo catálogo**:
   - Terraform: `code: "004"`, `questions: 200` (o lo que sea)
   - Vault (NUEVO): `id: "hashicorp-vault"`, `code: "005"` (o código oficial)

4. **Verifico**:
   - JSON válido
   - IDs únicos y secuenciales
   - Explicaciones presentes

---

## 🎮 Cómo Funciona el Quiz (Usuario)

### Web (index.html)

1. **Dropdown Provider** → Filtra exámenes (OCI, HashiCorp, GitHub, MySQL)
2. **Selector Examen** → Carga preguntas
3. **Modo**:
   - `Random`: Aleatorio
   - `Sequential`: Orden original
   - `Review`: Solo incorrectas previas
4. **Comenzar** → Inicia timer (2 horas)
5. **Responder**:
   - Una respuesta: Auto-avanza
   - Múltiples: Botón "Comprobar" → "Siguiente"
6. **Resumen** → Puntuación, incorrectas guardadas en localStorage

### CLI (quiz.py)

```bash
python quiz.py
# Elige banco (41 / 34 / 75 preguntas)
# Elige modo (aleatorio / secuencial / repasar fallos)
# Controles: A-D responder, X explicación+skip, S skip, M marcar
# Segunda ronda de marcadas
# Resumen final
```

---

## 🛠️ Scripts de Desarrollo

| Script | Entrada | Salida | Uso |
|--------|---------|--------|-----|
| `parse_terraform_docx.py` | .docx / .pdf | questions.json + .md | Extraer de Word/PDF |
| `fix_terraform_questions.py` | questions.json | questions.json (limpio) | Corregir formato |
| `regenerate_markdown.py` | questions.json | questions.md | JSON → Markdown |
| `gh300_to_md.py` | gh300.json | gh300.md | JSON → Markdown (GH-300) |
| `extract_terraform.py` | Archivos varios | terraform.json | Consolidar Terraform |

---

## ✅ Checklist: Agregar Nuevo Examen

- [ ] Archivo de preguntas preparado (JSON o MD)
- [ ] Validar JSON: `python -c "import json; json.load(open('file.json'))"`
- [ ] Contar preguntas: `python -c "import json; print(len(json.load(open('file.json'))))"`
- [ ] Crear carpeta `Descargables/Provider/` o usar `Nuevos/`
- [ ] Copiar questions.json (o .md)
- [ ] Crear README.md con recursos
- [ ] Actualizar `exams-catalog.json`:
  - [ ] Agregar entrada en `exams`
  - [ ] Actualizar `totalExams`
  - [ ] Actualizar `totalQuestions`
  - [ ] Actualizar `lastUpdated`
- [ ] Probar en browser (seleccionar examen, cargar preguntas)
- [ ] Commit + push

---

## 🐛 Troubleshooting

### "El examen no carga en el web quiz"
- ✅ Verificar ruta en `exams-catalog.json`
- ✅ Validar JSON: `python -m json.tool file.json`
- ✅ Ver consola del navegador (F12)

### "Respuestas se marcan mal"
- ✅ `correctKeys` es array: `["A"]` o `["B", "D"]`
- ✅ Keys corresponden (A, B, C, D)
- ✅ Preguntas multi-respuesta: decir "(Choose two)" en la pregunta

### "Timer no funciona"
- ✅ Verificar `totalTimeSeconds` en quiz.js
- ✅ Comprobar consola del navegador

### "JSON corrupto"
```bash
python -c "
import json
try:
    json.load(open('file.json'))
    print('✅ JSON válido')
except json.JSONDecodeError as e:
    print(f'❌ Error: {e}')
"
```

---

## 📌 Convenciones Importantes

| Aspecto | Regla |
|--------|-------|
| **IDs de Examen** | Lowercase, guiones: `hashicorp-terraform` |
| **Códigos** | Oficiales de certificación: `003`, `1Z0-1122-25`, `GH-300` |
| **Providers** | GitHub, HashiCorp, OCI, MySQL (orden en dropdown) |
| **Categorías** | AI, Infrastructure, Database, DevOps |
| **correctKeys** | **SIEMPRE array** `["A"]` |
| **Secuencia de IDs** | Sin gaps (1, 2, 3, ..., 150) |
| **Nombres archivos** | `questions.json` o `Provider-Code.md` |

---

## 🔗 URLs Importantes

- **Repository**: GitHub
- **Web Quiz**: Abre `index.html` en navegador
- **Catálogo JSON**: `exams-catalog.json`
- **Exámenes JSON**: `Descargables/*/questions.json`
- **Exámenes MD**: `Nuevos/*.md`

---

## 📅 Versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0.0 | 2025-12-26 | Setup inicial: 11 exámenes, 837 preguntas |
| 1.1.0 | 2026-09-28 | (Preparado para Terraform 004 + Vault) |

---

## 🎯 Plan: Próximas Actualizaciones

- [ ] Actualizar Terraform: 003 → 004
- [ ] Agregar Vault (nuevo)
- [ ] Posible: HashiCorp Consul, Nomad
- [ ] Posible: Azure certifications
- [ ] Feature: Exportar resultados a PDF
- [ ] Feature: Favoritos/Bookmarks

---

**Última actualización**: 2026-09-28
**Autor**: Sistema Multi-Examen
**Estado**: ✅ Funcional, listo para actualizaciones

