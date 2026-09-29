# Guía de Estudio para GH-300: GitHub Copilot

Esta guía está diseñada para ayudarte a preparar la certificación **GH-300: GitHub Copilot**. Abarca los dominios principales y habilidades medidas en el examen, traducidos y explicados para facilitar su comprensión en español.

## 🎧 Recurso de Audio

**[📥 Descargar preguntas en audio (MP3)](GH-300examen.mp3)**

Escucha las preguntas del examen en formato de audio para repasar mientras te desplazas, haces ejercicio o en cualquier momento que prefieras el aprendizaje auditivo.

---

## 📚 Estructura del Examen

El examen evalúa tus habilidades en las siguientes áreas:

| Dominio | Peso |
| :--- | :--- |
| **Dominio 1: IA Responsable** | 7% |
| **Dominio 2: Planes y características de GitHub Copilot** | 31% |
| **Dominio 3: Cómo funciona GitHub Copilot y manejo de datos** | 15% |
| **Dominio 4: Elaboración e Ingeniería de Prompts** | 9% |
| **Dominio 5: Casos de uso de IA para desarrolladores** | 14% |
| **Dominio 6: Pruebas (Testing) con GitHub Copilot** | 9% |
| **Dominio 7: Fundamentos de privacidad y exclusiones de contexto** | 15% |

---

## 🧠 Dominio 1: IA Responsable (7%)

Aborda la ética y seguridad en el uso de herramientas generativas.

*   **Riesgos de la IA:** Comprender sesgos, alucinaciones y errores.
*   **Limitaciones:** Los modelos dependen de sus datos de entrenamiento; pueden tener información desactualizada o sesgada.
*   **Validación:** **SIEMPRE** se debe revisar el código generado. La responsabilidad final es del desarrollador.
*   **Daños potenciales:**
    *   *Sesgo (Bias):* Estereotipos en el código o comentarios.
    *   *Seguridad:* Código vulnerable.
    *   *Privacidad:* Fugas de datos sensibles.
*   **IA Ética:** Principios de transparencia, justicia y responsabilidad.

---

## 💼 Dominio 2: Planes y Características (31%)

Diferencias clave entre las versiones de Copilot.

### Comparativa de Planes

1.  **Copilot Individual:**
    *   Para uso personal.
    *   Gestión individual de facturación.
    *   No tiene gestión centralizada de políticas.
2.  **Copilot Business:**
    *   Para organizaciones.
    *   Gestión de políticas a nivel de organización (ej. bloquear sugerencias de código público).
    *   Gestión de licencias por puesto (seat management).
    *   **Exclusión de archivos (Content Exclusions):** Bloquear repositorios o rutas específicas para que no sean usados por Copilot.
    *   Logs de auditoría.
3.  **Copilot Enterprise:**
    *   Integración profunda con GitHub.com.
    *   **Copilot Chat en GitHub.com:** Preguntar sobre repositorios enteros.
    *   **Knowledge Bases:** Indexar documentación interna y código para respuestas personalizadas.
    *   Resúmenes de Pull Requests automáticos.

### Características en el IDE y CLI
*   **Autocompletado (Ghost text):** Sugerencias mientras escribes.
*   **Chat:** Panel lateral o inline para preguntas y refactorización.
*   **CLI:** Comandos en terminal (`gh copilot suggest`, `gh copilot explain`).

---

## ⚙️ Dominio 3: Funcionamiento y Datos (15%)

Entender qué pasa "bajalel capó".

### Ciclo de vida de una sugerencia (Data Pipeline)
1.  **Context Gathering (Recolección de contexto):** Copilot mira el archivo abierto, pestañas vecinas, y cursor para entender qué necesitas.
2.  **Prompt Building:** Construye un prompt para el LLM (Large Language Model) con ese contexto.
3.  **Filtrado (Proxy):** Pasa por filtros de toxicidad y seguridad antes de ir al modelo.
4.  **Generación:** El modelo (OpenAI Codex/GPT) genera opciones.
5.  **Post-procesamiento:** Se filtra de nuevo (ej. filtro de duplicidad contra código público).
6.  **Sugerencia:** Aparece en tu editor.

### Manejo de Datos
*   **Individual:** Puede compartir snippets para mejorar el modelo (opcional).
*   **Business/Enterprise:** Por defecto NO usan tu código para entrenar modelos base.

### Limitaciones Técnicas
*   **Ventana de contexto:** Cantidad limitada de "memoria" (tokens) que el modelo puede "leer" a la vez.
*   **Alucinaciones:** El modelo predice texto probable, no "piensa" ni verifica hechos.

---

## 🗣️ Dominio 4: Ingeniería de Prompts (9%)

Cómo pedir las cosas para obtener mejores resultados.

*   **Componentes de un buen Prompt:**
    *   **Contexto:** ¿Qué quieres hacer? ¿Qué lenguaje? ¿Qué librerías?
    *   **Instrucción:** Verbo claro ("Escribe", "Explica", "Refactoriza").
    *   **Ejemplos (Few-shot prompting):** Darle ejemplos de entrada/salida ayuda mucho al modelo.
*   **Mejorar resultados:**
    *   Abrir archivos relacionados (para dar contexto).
    *   Ser específico.
    *   Iterar (refinar la pregunta).

---

## 🛠️ Dominio 5: Casos de Uso (14%)

¿Para qué sirve realmente en el día a día?

*   **Aprender lenguajes:** "Explícame qué hace este código de Rust".
*   **Traducir código:** "Pasa esta función de Python a JavaScript".
*   **Documentación:** "Genera JSDoc para esta función".
*   **Refactorización:** "Simplifica este bucle", "Mejora la legibilidad".
*   **Debugging:** "¿Por qué falla esto?", "Encuentra el bug lógico".
*   **Generar datos de prueba:** "Crea un JSON con 10 usuarios ficticios".
*   **Modernización:** Actualizar código legacy.

---

## 🧪 Dominio 6: Testing (9%)

Automatización de pruebas.

*   **Generación de Unit Tests:** "Genera pruebas unitarias para esta clase usando Jest".
*   **Casos borde (Edge cases):** Copilot es bueno sugiriendo entradas nulas, vacías o extremas.
*   **Boilerplate:** Escribir la estructura repetitiva de los tests.
*   **Aserciones:** Sugerir validaciones lógicas.

---

## 🔒 Dominio 7: Privacidad y Exclusiones (15%)

Proteger la propiedad intelectual.

### Exclusiones de Contenido (Content Exclusions)
*   Configurables a nivel de Organización o Repositorio.
*   Si un archivo está excluido:
    *   Copilot NO lo lee para generar contexto.
    *   Copilot NO ofrece sugerencias dentro de ese archivo.
*   Útil para código sensible, secretos, o datos PII.

### Detección de Duplicados (Duplication Detection)
*   Opción para bloquear sugerencias que coincidan con código público existente en GitHub (aprox. 150 caracteres).
*   Protege contra infracciones de copyright involuntarias.

### Solución de Problemas (Troubleshooting)
*   Si no hay sugerencias:
    *   Verificar conexión a internet.
    *   Verificar login.
    *   Verificar si el archivo está excluido.
    *   Verificar si el tipo de archivo es compatible.

---

## 🔗 Recursos Adicionales

*   [Documentación Oficial de GitHub Copilot](https://docs.github.com/es/copilot)
*   [GitHub Copilot Trust Center](https://resources.github.com/copilot-trust-center/)
*   [Microsoft Learn - GH-300 Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300)
