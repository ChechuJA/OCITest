# OCI Foundations AI Quiz - Sistema Multi-Examen# OCI Foundations AI Practice Exam



Sistema de quiz interactivo con soporte para múltiples exámenes de certificación Oracle.Este repositorio contiene un examen de práctica con 41 preguntas oficiales (se añadió Q41 sobre función de pérdida) y recursos de estudio para prepararte para el examen **Oracle Cloud Infrastructure Foundations (con foco en AI)**.



## 🎯 Características## Contenido

- `preguntas_oficiales.md`: Banco oficial Q1–Q41 con explicaciones.

- ✅ **75 preguntas integradas** (41 oficiales + 34 opcionales)- `preguntas_no_oficiales.md`: Inventario y plantilla para nuevas preguntas.

- ✅ **6 exámenes externos** desde archivos markdown (309 preguntas adicionales)- `quiz.py`: Quiz CLI (41 oficiales + opcionales) con segunda ronda y estados (correct, wrong, skipped, marked).

- ✅ **3 modos de estudio**: Aleatorio, Secuencial, Repasar falladas- `index.html` + `quiz.js` + `style.css`: Versión web responsive con timer, progreso y segunda ronda.

- ✅ **Timer** de 2 horas con advertencia en últimos 10 minutos- `documentacion.md`: Resumen teórico ampliado y mapa temático.

- ✅ **Almacenamiento local** de respuestas incorrectas- `README.md`: Este documento.

- ✅ **Categorización** por temas (AI, Infrastructure, Database)

- ✅ **Responsive** - funciona en móvil y desktop## Características

- ✅ **Sin backend** - 100% cliente (GitHub Pages ready)- Preguntas organizadas y numeradas (Q1–Q41) con respuesta y explicación breve.

- Traducción completa al español para afianzar comprensión.

## 📚 Exámenes Disponibles- Ficha de repaso rápido (servicios OCI AI, conceptos clave, hardware, principios).

- Quiz CLI: modos aleatorio, secuencial, repaso de fallos previos; controles A-D, X (explicación+skip), S (skip), M (marcar). Persistencia de fallos.

### Preguntas Integradas (en código)- Web quiz: selección banco (oficial / opcional / ambos), modos (aleatorio, secuencial, repaso), timer 2h, segunda ronda para marcadas, almacenamiento de fallos en localStorage.

- **Oficiales**: 41 preguntas de AI Foundations curadas

- **Opcionales**: 34 preguntas avanzadas de ML/AI/OCI## Requisitos

- Python 3.9+

### Exámenes Externos (desde markdown)

## Uso del Quiz CLI

#### 🤖 Artificial IntelligenceEjecuta:

1. **OCI 2025 AI Foundations Associate (1Z0-1122-25)** - 44 preguntas```bash

2. **Oracle AI Vector Search Professional (1Z0-184-25)** - 50 preguntaspython quiz.py

   - RAG, embeddings, similarity search, Oracle 23ai```

Flujo:

#### ☁️ Cloud Infrastructure  1. Elige banco (41 / 9 / 50 preguntas).

3. **OCI 2025 Foundations Associate (1Z0-1085-25) - Curated** - 39 preguntas2. Elige modo (aleatorio / secuencial / repasar fallos previos).

4. **OCI 2025 Foundations Associate (1Z0-1085-25) - Full** - 47 preguntas3. Controles por pregunta:

   - Regiones, ADs, Security, Networking, Compute, Storage	- A-D: responder

	- X: explicación y saltar (skipped)

#### 💾 Database	- S: saltar sin explicación (skipped)

5. **MySQL 8.0 Database Developer (1Z0-909)** - 77 preguntas	- M: marcar para segunda ronda

6. **MySQL Implementation Associate (1Z0-922)** - 52 preguntas4. Segunda ronda automática sólo de marcadas.

5. Resumen final: correctas, incorrectas, skipped. Guarda IDs incorrectos en `last_wrong.json`.

**Total: 384 preguntas únicas**

## Uso del Quiz Web

## 🚀 UsoAbre `index.html` en tu navegador (desktop o móvil). Controles equivalentes con botones:

- Explicación (X) muestra explicación y marca skipped.

### Método 1: GitHub Pages (Recomendado)- Saltar (S) salta sin explicación.

1. Sube el repositorio a GitHub- Marcar (M) difiere la pregunta para segunda ronda.

2. Activa GitHub Pages en Settings > PagesAl terminar: resumen con puntuación efectiva, incorrectas y skipped. Fallos se guardan en `localStorage` (clave `lastWrongIds`).

3. Accede a `https://tu-usuario.github.io/tu-repo`

## Estructura del Quiz

### Método 2: LocalCada pregunta presenta:

```bash- Enunciado

# Clona y abre index.html- Opciones (A, B, C, D)

# (Opcional) usa servidor local para evitar CORS:- Solicitud de tu respuesta (introduce letra)

python -m http.server 8000

# o## Próximas Mejoras (Opcionales)

npx serve- Exportar resultados a CSV/JSON en web.

```- Indicador visual de categoría (correct/wrong/skipped) en barra de progreso.

- Estadísticas históricas (sesiones previas) en localStorage.

## 📊 Resumen Técnico- Modo aprendizaje adaptativo (mayor frecuencia de fallos).

- Integración con flashcards (Anki) / generación automática de tarjetas.

- **Frontend**: HTML5 + CSS3 + JavaScript (Vanilla)

- **Almacenamiento**: LocalStorage API## Licencia

- **Formato datos**: JSON + MarkdownContenido educativo. Puedes reutilizarlo citando la fuente.

- **Carga dinámica**: Fetch API

- **Sin dependencias externas**## Contribuir

Sugerencias y PRs son bienvenidos: mejorar redacción, añadir referencias a documentación OCI oficial.

---

## Disclaimer

**Última actualización**: 22 de octubre de 2025  Este material no sustituye la documentación oficial de Oracle. Úsalo como complemento para reforzar conceptos.

**Versión**: 1.0.0  
**Total preguntas**: 384
