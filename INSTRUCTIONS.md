# Instrucciones de Desarrollo - Quiz de Certificaciones

## Estructura del Proyecto

```
OCITest/
├── index.html                          # Interfaz principal del quiz
├── quiz.js                             # Motor del quiz (lógica principal)
├── exam-loader.js                      # Cargador de exámenes (JSON/MD)
├── style.css                           # Estilos
├── exams-catalog.json                  # Catálogo central de exámenes
├── Descargables/
│   ├── GH-300/                        # GitHub Copilot
│   │   ├── gh300-questions.json       # Preguntas en JSON
│   │   ├── gh300-questions.md         # Preview en Markdown
│   │   └── README.md                  # Recursos de estudio
│   ├── Terraform/                     # HashiCorp Terraform
│   │   ├── terraform-questions.json   # Preguntas en JSON
│   │   ├── terraform-questions.md     # Preview en Markdown
│   │   └── README.md                  # Recursos de estudio
│   └── OCI/                           # Oracle Cloud Infrastructure
│       └── README.md                  # Recursos de estudio
├── Nuevos/                            # Archivos MD de OCI
│   ├── OCI AI Foundations 1Z0-1122-25.md
│   ├── AI Vector Search Professional 1Z0-184-25.md
│   └── ...
└── dev-tools/                         # Scripts de procesamiento
    ├── parse_terraform_docx.py        # Extrae preguntas de Word
    ├── fix_terraform_questions.py     # Corrige formato
    ├── regenerate_markdown.py         # Regenera MD desde JSON
    └── gh300_to_md.py                 # Convierte JSON a MD
```

## Formato de Datos

### Catálogo de Exámenes (`exams-catalog.json`)

```json
{
  "exams": [
    {
      "id": "unique-exam-id",
      "title": "Título del Examen",
      "code": "EXAM-CODE",
      "file": "ruta/al/archivo.json",
      "questions": 100,
      "provider": "ProviderName",
      "category": "Category",
      "description": "Descripción breve"
    }
  ],
  "categories": [
    {
      "id": "AI",
      "name": "Artificial Intelligence",
      "description": "AI, ML, GenAI"
    }
  ],
  "metadata": {
    "version": "1.0.0",
    "totalExams": 11,
    "totalQuestions": 837,
    "lastUpdated": "2025-12-26"
  }
}
```

**Importante**: Actualizar `metadata.totalQuestions` cuando se añadan/modifiquen exámenes.

### Formato de Preguntas JSON

```json
[
  {
    "id": 1,
    "question": "Texto de la pregunta completa con contexto necesario",
    "answers": [
      {
        "key": "A",
        "text": "Primera opción"
      },
      {
        "key": "B",
        "text": "Segunda opción"
      }
    ],
    "correctKeys": ["A"],  // Puede ser array para multi-respuesta
    "explanation": "Explicación de la respuesta correcta con referencia"
  }
]
```

**Reglas Críticas**:
- `correctKeys` es **SIEMPRE un array** (incluso para una sola respuesta: `["A"]`)
- Las opciones deben estar ordenadas alfabéticamente por `key`
- La pregunta NO debe contener las opciones
- Si hay "(Choose two)", debe estar en la pregunta, no en una opción

### Formato de Preguntas Markdown

```markdown
#### Q1. Texto de la pregunta

- [ ] A. Primera opción (incorrecta)
- [x] B. Segunda opción (correcta)
- [ ] C. Tercera opción (incorrecta)

> Explicación con referencia: https://example.com
```

## Agregar un Nuevo Examen

### Paso 1: Preparar las Preguntas

#### Desde JSON:
```python
# Ya está en formato correcto, solo validar estructura
import json
data = json.load(open('preguntas.json', encoding='utf-8'))

# Validar cada pregunta
for q in data:
    assert 'id' in q and 'question' in q and 'answers' in q
    assert isinstance(q['correctKeys'], list)
    assert all('key' in a and 'text' in a for a in q['answers'])
```

#### Desde Markdown:
```bash
# Usar el parser existente en exam-loader.js
# Formato esperado:
#### Qn. Pregunta
- [x] A. Correcta
- [ ] B. Incorrecta
> Explicación
```

#### Desde Word (.docx):
```bash
# Usar el script de extracción
python dev-tools/parse_terraform_docx.py

# Patrón esperado en el documento:
# Question XXX
# [Texto de la pregunta]
# [Opciones como párrafos]
# Answer XXX
# Correct Answer: [letra(s)]
# Reference [URL]
```

### Paso 2: Crear Estructura de Archivos

```bash
# Crear directorio del provider
mkdir Descargables/ProviderName

# Crear archivos
# 1. questions.json (obligatorio para la app)
# 2. questions.md (opcional, para revisión manual)
# 3. README.md (recursos de estudio)
```

### Paso 3: Actualizar el Catálogo

Editar `exams-catalog.json`:

```json
{
  "id": "provider-exam-name",
  "title": "Título Completo del Examen",
  "code": "EXAM-CODE",
  "file": "Descargables/ProviderName/questions.json",
  "questions": 100,
  "provider": "ProviderName",
  "category": "AI|Infrastructure|Database|DevOps",
  "description": "Descripción del examen"
}
```

**Providers prioritarios**: `GitHub`, `HashiCorp` aparecen primero en el dropdown.

### Paso 4: Crear README de Referencias

Template en `Descargables/ProviderName/README.md`:

```markdown
# ProviderName ExamName - Recursos de Estudio

## Documentación Oficial
- [Link principal](url)

## Certificación
- Exam Topics
- Study Guide
- Practice Tests

## Hands-on Labs
- Labs interactivos

## Tips para el Examen
- Duración
- Formato
- Passing score
- Conceptos clave
```

## Scripts de Desarrollo

### Extraer desde Word

```bash
python dev-tools/parse_terraform_docx.py
# Input: Descargables/Provider/document.docx
# Output: questions.json + questions.md
```

### Corregir Formato de Preguntas

```bash
python dev-tools/fix_terraform_questions.py
# Detecta y corrige:
# - Opciones que deberían ser parte de la pregunta
# - Re-asigna letras (A, B, C...)
# - Ajusta correctKeys
```

### Regenerar Markdown desde JSON

```bash
python dev-tools/regenerate_markdown.py
# Usa: questions.json
# Genera: questions.md
```

### Convertir JSON a Markdown

```bash
python dev-tools/gh300_to_md.py
# Útil para auditoría manual
```

## Buenas Prácticas

### 1. Preguntas con Respuestas Múltiples

```json
{
  "question": "Select TWO correct options. (Choose two.)",
  "correctKeys": ["B", "D"]  // Array con múltiples valores
}
```

En la UI:
- Se muestran checkboxes en lugar de radio buttons
- Botón "Comprobar" en lugar de "Siguiente"
- Permite seleccionar/deseleccionar múltiples opciones

### 2. Preguntas FILL BLANK

```json
{
  "question": "FILL BLANK - What command initializes a Terraform directory?",
  "answers": [
    {"key": "A", "text": "terraform init"}
  ],
  "correctKeys": ["A"]
}
```

### 3. Preguntas con Código

Incluir el código en la pregunta:

```json
{
  "question": "Given this configuration:\n```hcl\nvariable 'name' {\n  type = string\n}\n```\nWhat is the type?",
  "answers": [...]
}
```

### 4. Explicaciones con Referencias

```json
{
  "explanation": "Terraform uses state locking to prevent concurrent modifications. Reference: https://developer.hashicorp.com/terraform/language/state/locking"
}
```

## Debugging

### Verificar Integridad del JSON

```bash
python -c "import json; json.load(open('file.json'))"
```

### Contar Preguntas

```bash
python -c "import json; print(len(json.load(open('file.json'))))"
```

### Buscar Preguntas Faltantes

```bash
python -c "
import json
data = json.load(open('file.json'))
ids = [q['id'] for q in data]
expected = set(range(1, max(ids)+1))
missing = sorted(expected - set(ids))
print('Faltantes:', missing)
"
```

### Verificar Multi-respuesta

```bash
python -c "
import json
data = json.load(open('file.json'))
multi = [q['id'] for q in data if len(q['correctKeys']) > 1]
print(f'{len(multi)} preguntas multi-respuesta:', multi[:10])
"
```

## Modificar el Frontend

### `quiz.js` - Funciones Principales

- `startQuiz()`: Inicializa el examen
- `renderCurrent()`: Muestra pregunta actual
- `selectOption(idx)`: Maneja selección de respuestas
- `nextBtn.addEventListener()`: Avanza a siguiente pregunta
- `finishQuiz()`: Muestra resumen final
- `isMultiAnswerQuestion(q)`: Detecta preguntas multi-respuesta

### `exam-loader.js` - Parsers

- `loadExamsCatalog()`: Carga catálogo
- `loadExam(file)`: Carga examen (auto-detecta JSON/MD)
- `parseJsonExam(text)`: Parser para JSON
- `parseMarkdownExam(text)`: Parser para Markdown

### Agregar Soporte para Nuevo Formato

1. Detectar extensión en `loadExam()`
2. Crear función `parseNewFormat()`
3. Retornar array con estructura estándar:
```javascript
[{
  id: 1,
  q: "pregunta",
  o: ["opción1", "opción2"],
  a: [0, 2],  // índices correctos o número único
  e: "explicación"
}]
```

## Flujo de Usuario

1. Seleccionar **Provider** → filtra exámenes
2. Seleccionar **Examen** → carga preguntas
3. Seleccionar **Modo**:
   - `random`: Orden aleatorio
   - `sequential`: Orden original
   - `review`: Solo incorrectas previas
4. Clic **"Comenzar"** → inicia timer
5. Responder preguntas:
   - Una respuesta: Auto-avanza
   - Múltiples: Botón "Comprobar" → "Siguiente"
6. Ver **Resumen** final con score

## Características Implementadas

✅ Multi-respuesta con checkboxes
✅ Timer configurable
✅ Modo review (incorrectas)
✅ Tracking de preguntas falladas
✅ Explicaciones con referencias
✅ Selector de provider
✅ Soporte JSON y Markdown
✅ Preguntas integradas (builtin)
✅ Loading desde catálogo
✅ Progress bar visual
✅ Feedback color-coded

## Próximas Mejoras Sugeridas

- [ ] Exportar resultados a PDF
- [ ] Modo práctica (sin timer)
- [ ] Favoritos/marcadores
- [ ] Búsqueda de preguntas
- [ ] Notas por pregunta
- [ ] Comparación de intentos
- [ ] Modo flashcards
- [ ] Dark mode
- [ ] Internacionalización

## Troubleshooting

### Las preguntas no cargan
- Verificar consola del navegador
- Comprobar ruta en `exams-catalog.json`
- Validar JSON con linter

### Respuestas incorrectas marcadas como correctas
- Verificar `correctKeys` (debe ser array)
- Asegurar que keys coinciden (A, B, C...)
- Verificar índices en preguntas multi-respuesta

### Timer no funciona
- Comprobar `totalTimeSeconds` en quiz.js
- Verificar que `startTimer()` se llama en `startQuiz()`

### Opciones aparecen mal formateadas
- Revisar que no haya código en answers.text
- Usar comillas correctamente en JSON
- Escapar caracteres especiales

## Contacto y Contribuciones

Para agregar nuevos exámenes o reportar problemas:
1. Seguir el formato de este documento
2. Validar JSON antes de commitear
3. Actualizar `exams-catalog.json`
4. Regenerar markdown si es necesario
5. Probar en navegador antes de publicar

---

**Última actualización**: 2025-12-26
**Versión del catálogo**: 1.0.0
**Total exámenes**: 11 (378 TF + 129 GH + OCI integrados)
