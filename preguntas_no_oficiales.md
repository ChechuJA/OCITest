# Preguntas No Oficiales OCI Foundations (Depuradas)

Este archivo ha sido simplificado para contener únicamente preguntas realmente complementarias que NO estén ya cubiertas en el banco oficial. Tras la revisión, todas las 9 preguntas iniciales se identificaron como duplicados exactos o conceptuales de las oficiales (Q1–Q40) o ya presentes en otros materiales.

## Situación Actual
No quedan preguntas "no oficiales" únicas después de eliminar duplicados.

## Duplicados Detectados (Referencia)
| Etiqueta Original | Tema | Pregunta Oficial Equivalente |
|-------------------|------|------------------------------|
| O1 (NLP Sentiment & Translation) | NLP | Abordado en documentación general y banco oficial de texto (Q35 cubre clasificación; concepto NLP en resumen) |
| O2 (Model Training) | ML Fundamentos | Explicado en secciones de documentación y base conceptual (varias preguntas sobre flujo ML) |
| O3 (CNN propósito) | Vision / DL | Q33 / Q38 (clasificación imagen / reconocimiento facial) |
| O4 (Generative vs Supervisado) | Generative AI | Q30 (pretraining), Q15 (diferencia LLM), documentación Generative AI |
| O5 (Ventaja Superclusters) | Infra GPU | Q25 / Q26 / sección infraestructura |
| O6 (In-context learning) | Prompting | Sección Generative AI (Prompting), Q27 (few-shot), resumen teórico |
| O7 (Speech transcripción) | Speech | Q19 (SRT), Q12 (normalización), documentación Speech (transcripción base) |
| O8 (Document Understanding NO transcribe audio) | Document AI | Q14 (key-value), Q9 (doc classification), documentación DO Understanding |
| O9 (Notebook Sessions) | Data Science | Sección Data Science (Notebook Sessions), flujo despliegue |

## Próximos Pasos Sugeridos
Puedes optar por:
1. Añadir nuevas preguntas verdaderamente complementarias (escenarios integrados Vision+Language, métricas avanzadas, drift de datos, seguridad de prompts).
2. Crear un banco "Escenarios" separado (ej.: caso de fraude, pipeline MLOps, análisis de logs).
3. Mantener este archivo como inventario de duplicados para evitar reintroducirlos.

## Plantilla para Nuevas Preguntas (Ejemplo)
```
Escenario: Un equipo necesita detectar anomalías en una serie temporal de métricas de rendimiento de una aplicación.
Pregunta: ¿Qué servicio de OCI usarías para detectar patrones anómalos sin etiquetado previo?
A. OCI Speech
B. OCI Vision
C. OCI Anomaly Detection ✅
D. OCI Language
Explicación: OCI Anomaly Detection modela patrones normales y resalta desviaciones en series temporales.
```

## Estado Final
Archivo listo. Sin preguntas activas no oficiales. Se recomienda usarlo como lista de control para no generar redundancias.

---
Fin del archivo depurado.
