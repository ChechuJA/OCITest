# 📦 Plan: Terraform 004 + Vault (NUEVO)

**Estado**: ⏳ Esperando archivos  
**Fecha plan**: 2026-09-28  
**Prioridad**: Terraform 004 primero, luego Vault

---

## 📋 Resumen de lo que necesito

### De tu parte:
1. **Archivo Terraform 004** (Word, PDF, o JSON)
   - Q1-Q150: **OFICIALES** (estos van primero)
   - Q151-Q200+ : Opcionales (si hay más)
   
2. **Archivo Vault** (Word, PDF, o JSON)
   - Q1-Q150: **OFICIALES** (estos van primero)
   - Q151-Q300+ : Opcionales (si hay más)

### Formato esperado en el archivo:
```
[Opción A: Word/PDF]
├── Question 1
├── [Texto de la pregunta]
├── A. Opción A
├── B. Opción B
├── C. Opción C
├── D. Opción D
├── Correct Answer: B
└── [Explicación / Reference]

[Opción B: JSON]
[{
  "id": 1,
  "question": "...",
  "answers": [{"key": "A", "text": "..."}, ...],
  "correctKeys": ["B"],
  "explanation": "..."
}]
```

---

## 🔧 Mi Workflow (Paso-a-paso)

### Fase 1: Preparación (Cuando reciba tus archivos)

1. **Extraer preguntas**
   ```bash
   # Si es Word/PDF:
   python dev-tools/parse_terraform_docx.py
   
   # Genera:
   # - Descargables/Terraform/terraform-questions-004.json
   # - Descargables/Terraform/terraform-questions-004.md
   ```

2. **Validar integridad**
   ```bash
   # Verificar JSON válido
   python -c "import json; data = json.load(open('file.json')); print(f'Total Q: {len(data)}')"
   
   # Verificar structure:
   # - IDs secuenciales (1, 2, 3, ..., 150+)
   # - correctKeys es SIEMPRE array
   # - Todas las preguntas tienen explicación
   # - Opciones A, B, C, D presentes
   ```

3. **Limpiar formato** (si es necesario)
   ```bash
   python dev-tools/fix_terraform_questions.py
   # Normaliza keys, reagrupa opciones, valida correctKeys
   ```

4. **Generar Markdown** (para tu revisión)
   ```bash
   python dev-tools/regenerate_markdown.py
   # Terraform 003 → terraform-questions-003.md
   # Terraform 004 → terraform-questions-004.md
   # Vault       → vault-questions.md
   ```

### Fase 2: Integración (Confirmar contigo)

5. **Mostrar preview**
   - Primeras 5 preguntas en formato JSON
   - Primeras 5 preguntas en formato Markdown
   - Resumen: Total Q, IDs range, multi-respuesta count

6. **Tu aprobación**
   - ✅ "Perfecto, guarda esto"
   - 🔧 "Arregla esto..."

### Fase 3: Deploy (Después de tu confirmación)

7. **Actualizar catálogo**
   ```json
   // Actualizar TERRAFORM
   {
     "id": "hashicorp-terraform",
     "code": "004",                    // ← Cambiar de 003 a 004
     "file": "Descargables/Terraform/terraform-questions.json",
     "questions": 200                  // ← Actualizar total
   }
   
   // AGREGAR VAULT (NUEVO)
   {
     "id": "hashicorp-vault",
     "title": "HashiCorp Vault Associate",
     "code": "005",                    // ← O código oficial
     "file": "Descargables/Vault/vault-questions.json",
     "questions": 200,                 // ← o cantidad real
     "provider": "HashiCorp",
     "category": "DevOps",
     "description": "HashiCorp Certified: Vault Associate certification"
   }
   ```

8. **Actualizar metadata**
   ```json
   "metadata": {
     "totalExams": 12,                 // ← 11 + 1 (Vault)
     "totalQuestions": 1237,           // ← 837 + 200 (Terraform) + 200 (Vault)
     "lastUpdated": "2026-09-28"
   }
   ```

9. **Crear README para Vault**
   ```markdown
   # HashiCorp Vault - Recursos de Estudio
   
   ## Documentación Oficial
   - [Vault Documentation](https://www.vaultproject.io/docs)
   
   ## Certificación
   - [Exam Topics](...)
   - [Study Guide](...)
   - [Practice Labs](...)
   ```

10. **Probar en navegador**
    - Abrir `index.html`
    - Dropdown Provider → HashiCorp
    - Selector Examen → "HashiCorp Vault Associate"
    - Cargar y verificar primeras Q

11. **Commit + Push**
    ```bash
    git add .
    git commit -m "feat: Update Terraform to 004 and add Vault certification (200 + 150 questions)"
    git push origin main
    ```

---

## 📊 Tabla de Cambios Esperados

| Aspecto | Actual | Después | Cambio |
|--------|--------|---------|--------|
| **Total exámenes** | 11 | 12 | +1 (Vault) |
| **Terraform código** | 003 | 004 | Actualizar |
| **Terraform Q** | 378 | ~200 | Reemplazar |
| **Total Questions** | 837 | ~1237 | +400 |
| **Providers** | OCI, HashiCorp, GitHub, MySQL | + Vault | + DevOps |

---

## 📁 Archivos que se modificarán

```
Cambios:
├── Descargables/Terraform/
│   ├── terraform-questions.json      # ← REEMPLAZAR (004)
│   ├── terraform-questions.md        # ← REGENERAR
│   └── README.md                     # ✅ Sin cambios (recursos igual)
│
├── Descargables/Vault/               # ← NUEVO
│   ├── vault-questions.json          # ← CREAR
│   ├── vault-questions.md            # ← CREAR
│   └── README.md                     # ← CREAR
│
└── exams-catalog.json                # ← ACTUALIZAR
    ├── Terraform entry (code, questions)
    ├── + Vault entry (NUEVO)
    └── metadata (totalExams, totalQuestions, lastUpdated)
```

---

## 💬 Cómo Quiero que Pases los Archivos

### Opción 1: Upload directo (MEJOR)
```
Adjunta los archivos en el chat:
- terraform-004.pdf  (o .docx)
- vault-nuevo.pdf    (o .docx)

Yo los procesaré automáticamente.
```

### Opción 2: Contenido en el chat
```
Si los pegas aquí, los procesaré igual de bien.

Formato esperado (solo ejemplos):
---
TERRAFORM 004 - Q1
Question: ¿Qué es terraform state?
A. Un archivo JSON
B. Una base de datos
C. Un objeto remoto
D. Un concepto teórico
Correct Answer: A
Explanation: El state es el archivo JSON que almacena el estado...
---
```

### Opción 3: Enlace de descarga
```
Si tienes un Drive, Dropbox, etc.:
Pasa el link y descargo directamente.
```

---

## ⏱️ Timeline Estimado

| Fase | Tiempo | Status |
|------|--------|--------|
| 1. Recibir archivos | - | ⏳ Esperando |
| 2. Extraer + Validar | 5-10 min | Automático |
| 3. Tu revisión | TBD | Depende de ti |
| 4. Integración | 5 min | Rápido |
| 5. Testing | 2-3 min | Automático |
| 6. Commit + Push | 1 min | Automático |
| **Total** | **~20-30 min** | ⏳ |

---

## ✅ Checklist: Antes de Pasar Archivos

- [ ] Archivo Terraform 004: Word, PDF, o JSON
- [ ] Archivo Vault nuevo: Word, PDF, o JSON
- [ ] Confirmación: Q1-Q150 son OFICIALES (primero)
- [ ] Confirmación: Q151+ son opcionales (después, si hay)
- [ ] Confirmación: Orden es importante

---

## 🎯 Después: Lo que haremos

1. **Tu revisión** → Apruebas formato y contenido
2. **Deploy** → Commit automático
3. **Testing** → Verifico en navegador
4. **Listo** → Terraform 004 + Vault disponibles en quiz web

---

## 📞 Dudas o Cambios

Si durante el proceso:
- Preguntas mal formateadas → Te muestro ejemplos, tú confirmas
- Falta explicación → Te pido que la agregues
- Código oficial diferente → Actualizamos el catálogo

---

## 🚀 ¡Listo!

**Pasa tus archivos cuando estés listo.** Puedo procesarlos en cualquier formato (PDF, Word, JSON, texto plano, imagen, lo que tengas).

**¿Tienes los archivos listos?** 📁

