# OCI Foundations AI Practice Exam

Este repositorio contiene un examen de práctica con 41 preguntas oficiales (se añadió Q41 sobre función de pérdida) y recursos de estudio para prepararte para el examen **Oracle Cloud Infrastructure Foundations (con foco en AI)**.

## Contenido
- `preguntas_oficiales.md`: Banco oficial Q1–Q41 con explicaciones.
- `preguntas_no_oficiales.md`: Inventario y plantilla para nuevas preguntas.
- `quiz.py`: Quiz CLI (41 oficiales + opcionales) con segunda ronda y estados (correct, wrong, skipped, marked).
- `index.html` + `quiz.js` + `style.css`: Versión web responsive con timer, progreso y segunda ronda.
- `documentacion.md`: Resumen teórico ampliado y mapa temático.
- `README.md`: Este documento.

## Características
- Preguntas organizadas y numeradas (Q1–Q41) con respuesta y explicación breve.
- Traducción completa al español para afianzar comprensión.
- Ficha de repaso rápido (servicios OCI AI, conceptos clave, hardware, principios).
- Quiz CLI: modos aleatorio, secuencial, repaso de fallos previos; controles A-D, X (explicación+skip), S (skip), M (marcar). Persistencia de fallos.
- Web quiz: selección banco (oficial / opcional / ambos), modos (aleatorio, secuencial, repaso), timer 2h, segunda ronda para marcadas, almacenamiento de fallos en localStorage.

## Requisitos
- Python 3.9+

## Uso del Quiz CLI
Ejecuta:
```bash
python quiz.py
```
Flujo:
1. Elige banco (41 / 9 / 50 preguntas).
2. Elige modo (aleatorio / secuencial / repasar fallos previos).
3. Controles por pregunta:
	- A-D: responder
	- X: explicación y saltar (skipped)
	- S: saltar sin explicación (skipped)
	- M: marcar para segunda ronda
4. Segunda ronda automática sólo de marcadas.
5. Resumen final: correctas, incorrectas, skipped. Guarda IDs incorrectos en `last_wrong.json`.

## Uso del Quiz Web
Abre `index.html` en tu navegador (desktop o móvil). Controles equivalentes con botones:
- Explicación (X) muestra explicación y marca skipped.
- Saltar (S) salta sin explicación.
- Marcar (M) difiere la pregunta para segunda ronda.
Al terminar: resumen con puntuación efectiva, incorrectas y skipped. Fallos se guardan en `localStorage` (clave `lastWrongIds`).

## Estructura del Quiz
Cada pregunta presenta:
- Enunciado
- Opciones (A, B, C, D)
- Solicitud de tu respuesta (introduce letra)

## Próximas Mejoras (Opcionales)
- Exportar resultados a CSV/JSON en web.
- Indicador visual de categoría (correct/wrong/skipped) en barra de progreso.
- Estadísticas históricas (sesiones previas) en localStorage.
- Modo aprendizaje adaptativo (mayor frecuencia de fallos).
- Integración con flashcards (Anki) / generación automática de tarjetas.

## Licencia
Contenido educativo. Puedes reutilizarlo citando la fuente.

## Contribuir
Sugerencias y PRs son bienvenidos: mejorar redacción, añadir referencias a documentación OCI oficial.

## Disclaimer
Este material no sustituye la documentación oficial de Oracle. Úsalo como complemento para reforzar conceptos.
