# Documentación Ampliada OCI Foundations (AI Focus)

## Resumen Examen Oracle Cloud Infrastructure 2025 AI Foundations Associate (1Z0-1122-25)

Este documento recopila el resumen teórico y las preguntas prácticas (oficiales y complementarias)
para la preparación del examen 1Z0-1122-25 de Oracle Cloud Infrastructure (OCI) AI Foundations Associate.
Incluye los conceptos clave de IA, ML, DL, Generative AI y los servicios de IA de OCI.

1️⃣ Fundamentos de la IA
• Simula procesos de inteligencia humana mediante algoritmos.
• Incluye tareas como reconocimiento de voz, visión por computadora y lenguaje natural.

2️⃣ Fundamentos del Aprendizaje Automático (ML)
• Subcampo de la IA que permite a los sistemas aprender a partir de datos.
• Tipos: supervisado, no supervisado y por refuerzo.

3️⃣ Fundamentos del Aprendizaje Profundo (DL)
• Subcampo del ML que utiliza redes neuronales profundas para procesar grandes volúmenes de datos.
• CNN para imágenes, RNN para secuencias, Transformers para texto.

4️⃣ Generative AI y Modelos de Lenguaje Grande (LLMs)
• Generan contenido nuevo similar a los datos de entrenamiento.
• Los LLM utilizan mecanismos de autoatención (Transformers) para comprender el lenguaje humano.

5️⃣ Servicios de OCI para IA
• OCI Vision: análisis de imágenes y videos.
• OCI Language: procesamiento de lenguaje natural.
• OCI Speech: conversión de voz a texto.
• OCI Document Understanding: extracción de información de documentos.
• OCI Data Science: entorno para crear, entrenar y desplegar modelos.

---
## Resumen Teórico (Distribución aproximada de dominios)

1. **AI Fundamentals (≈10%)**
	- Diferencias entre AI (paraguas), ML (aprende de datos), DL (redes profundas).
	- Tipos de datos: estructurados, no estructurados (texto, imagen, audio), semiestructurados.
	- Ejemplos: asistentes virtuales, reconocimiento de voz, visión artificial, recomendadores.
	- Ciclo de vida alto nivel: problema -> datos -> modelo -> despliegue -> monitoreo -> mejora.

2. **Machine Learning Fundamentals (≈15%)**
	- Componentes: dataset, features (X), labels (y), split (train/validation/test).
	- Supervisado: regresión (valor continuo), clasificación (etiquetas discretas).
	- No supervisado: clustering (descubrir grupos), reducción dimensionalidad (PCA, t-SNE) para visualizar/mitigar ruido.
	- Overfitting vs Underfitting:
		 - Overfitting: baja pérdida train, alta pérdida test.
		 - Underfitting: alta pérdida tanto train como test (modelo demasiado simple).
	- Técnicas de mitigación: regularización (L2, dropout), más datos, early stopping, data augmentation.
	- Métricas:
		 - Accuracy = (TP+TN)/(Total)
		 - Precision = TP/(TP+FP) (Qué tan confiables son los positivos predichos)
		 - Recall = TP/(TP+FN) (Qué porcentaje de positivos reales recuperamos)
		 - F1 = 2 * (precision * recall) / (precision + recall)
		 - AUC-ROC para discriminación binaria, MAE/MSE para regresión.
	- Evaluación adecuada: evitar leakage, k-fold cross validation cuando datos escasos.

3. **Deep Learning Fundamentals (≈10%)**
	- Redes neuronales profundas: capas lineales + activaciones no lineales (ReLU, GELU).
	- CNN: convoluciones, filtros, pooling, extracción jerárquica (bordes -> texturas -> objetos).
	- RNN/LSTM/GRU: manejo secuencial, problemas de vanishing/exploding gradient.
	- Transformers: atención multi-cabeza, paralelización, mejores para dependencias largas.
	- Parámetros vs hiperparámetros (learning rate, batch size, número de capas).
	- Regularización DL: dropout, batch normalization, weight decay.

4. **Generative AI & Large Language Models (≈15%)**
	- Modelos generativos: aprenden distribución de datos (auto-regresivos, diffusion, VAEs, GANs).
	- LLMs (Transformers): embeddings -> bloques atención -> capa salida (softmax tokens).
	- In-Context Learning: ejemplos en el prompt; sin cambio de pesos.
	- Fine-tuning vs Parameter-efficient (LoRA, adapters, T-Few) para reducir costo.
	- Prompt Engineering: claridad, rol, ejemplos, restricciones (format specs), chain-of-thought opcional.
	- Evaluación generativa:
		 - Perplexity (fluidez), BLEU/ROUGE (similaridad n-gramas), METEOR (alineación semántica), Human eval (calidad subjetiva), Toxicity checks.
	- Riesgos: alucinaciones, sesgos, fuga de información (prompt injection), coste de cómputo.

5. **OCI AI Services & Infrastructure (≈10%)**
	- AI Services:
		 - Vision: OCR, clasificación documento, extracción clave-valor, detección objetos.
		 - Language: clasificación, sentimiento, NER, detección idioma.
		 - Speech: transcripción, normalización, puntuación confianza, archivos SRT, filtrado lenguaje (tagging/masking/removing).
		 - Document Understanding: OCR + estructuración avanzada (no transcribe audio).
		 - Anomaly Detection: series temporales; modelado patrones y desviaciones.
		 - Generative AI: acceso a LLMs, T-Few, embeddings.
	- Data Science:
		 - Notebook Sessions (entorno interactivo), Model Catalog (registro/versionado), Deployment (endpoints), ADS SDK.
	- Infraestructura:
		 - Superclusters: GPUs de alta densidad + RDMA (latencia baja). Escala para LLM y entrenamiento intensivo.
		 - GPUs: A100 (escala mediana), GB200 (exascala y entrenamiento extremo), roles comparativos.
		 - Almacenamiento y red: Object Storage para datasets, Block para rendimiento, RDMA para throughput inter-nodos.
	- AI Vector Search:
		 - Embeddings para búsqueda semántica (texto, documentos, potencial multimodal).
		 - Índices vectoriales: aproximación vs exacta (ANN – HNSW, IVF; conceptual).
		 - ONNX dentro de Database 23ai para inferencia cercana a los datos.
	- Gobernanza y seguridad:
		 - Uso de OCI Vault para llaves y secretos (no parte directa del cómputo AI).
		 - Principios de Trustworthy AI (lawful, ethical, robust) aplicados a despliegues.

6. **Evaluación y Monitoreo (Complementario)**
	- Monitoreo post-despliegue: drift de datos, degradación de métricas, latencia.
	- Observabilidad: logging inferencias, tasas de error, perfilado de GPU.
	- Re-entrenamiento programado vs bajo demanda (trigger por caída métrica).

7. **Optimización y Coste**
	- Escalado horizontal vs vertical (más nodos vs GPU más potente).
	- Técnicas de ahorro: PEFT (T-Few), batching, caching embeddings.
	- Elección de forma de cómputo: ajustar recursos a etapa (experimento vs producción).

8. **Buenas Prácticas de Prompting (Generative)**
	- Estructura sugerida: (Rol) + (Instrucción clara) + (Ejemplos opcionales) + (Formato esperado) + (Restricciones).
	- Evitar ambigüedad y peticiones múltiples sin delimitadores.
	- Uso de delimitadores (```texto```) para evitar inyección accidental.

9. **Riesgos y Mitigación**
	- Sesgo: diversificar dataset, auditorías.
	- Seguridad: sanitizar entrada, limitar capacidad de ejecutar código, rotar llaves.
	- Privacidad: anonimización de datos sensibles, encriptación en reposo y tránsito.

10. **Resumen Fórmulas Clave**
	- Accuracy = (TP+TN)/(TP+TN+FP+FN)
	- Precision = TP/(TP+FP)
	- Recall = TP/(TP+FN)
	- F1 = 2*(Precision*Recall)/(Precision+Recall)
	- MSE = (1/n) Σ (y_pred - y_true)^2
	- Perplexity ≈ exp(average cross-entropy)

---

## Objetivo
Explicar el contenido base que originó el banco de preguntas y proporcionar una guía conceptual extendida para reforzar y mejorar la calidad de futuras preguntas del examen OCI Foundations con énfasis en servicios de IA y conceptos de Machine Learning.

## 1. Panorama General de OCI
Oracle Cloud Infrastructure (OCI) ofrece servicios para cómputo, almacenamiento, networking y plataformas especializadas (Data Science, AI Services, Database 23ai). El examen Foundations cubre:
- Principios de la nube (IaaS, PaaS, SaaS)
- Arquitectura de OCI (regiones, dominios de disponibilidad, dominios de fallas)
- Identidad y seguridad (IAM, políticas, compartimentos, cifrado)
- Servicios base: Compute, Object Storage, Block Storage, VCN, Load Balancer, Autonomous Database
- Facturación y soporte (modelos de precio, SLA, niveles de soporte)

## 2. Servicios de IA en OCI
### 2.1 OCI Data Science
Entorno administrado para:
- Notebook Sessions: Desarrollo interactivo (Python, ADS SDK).
- Model Training: Entrenamiento de modelos tradicionales y deep learning.
- Model Catalog: Versionar, registrar, gobernar modelos.
- Model Deployment: Exponer endpoints de inferencia gestionados.
- Integration: Conda packs, GPUs (en formas disponibles), logging y monitoreo.

### 2.2 OCI AI Services
Servicios pre-entrenados listos para integración mediante API/SDK:
- Vision: Clasificación de imágenes y documentos, OCR, extracción clave-valor, detección de objetos.
- Language: Clasificación de texto (gran conjunto de categorías), sentimiento, detección de idioma, NER.
- Speech: Transcripción de audio, normalización, puntuación de confianza, soporte SRT, filtrado de lenguaje (tagging/masking/removing).
- Anomaly Detection (no detallado en preguntas oficiales): Identificación de patrones anómalos en series temporales.
- Generative AI: Modelos LLM para prompting, few-shot y fine-tuning eficiente (T-Few).

### 2.3 Oracle Database 23ai y Vector Search
- Integración de embeddings directamente en la base de datos.
- Carga de modelos ONNX para generar representaciones vectoriales.
- Consultas semánticas mezclando SQL y búsqueda vectorial.
- Reducción de latencia al evitar extracción masiva de datos.

## 3. Conceptos Clave de ML/DL
| Concepto | Definición | Relevancia en Preguntas |
|----------|------------|-------------------------|
| Overfitting | Modelo memoriza entrenamiento y falla al generalizar | Q3, Q12 (traducción) |
| Inference | Uso del modelo entrenado para predecir nuevos datos | Q21, Q30 |
| Regression | Predice valores continuos | Q6, Q15 (ES) |
| Classification | Asigna etiquetas discretas | Varias (spam, noticias, documentos) |
| RNN | Maneja secuencias temporales (música, texto) | Q1, Q18, Q27 |
| CNN | Extrae patrones espaciales en imágenes | Q33, Q38 |
| Tokens | Unidades mínimas procesadas por LLM | Q28 |
| Few-shot Prompting | Ejemplos en prompt guían salida | Q27 |
| In-Context Learning | Ajuste sin cambiar pesos usando ejemplos | Opcional O6 |
| Parameter-Efficient Fine-Tuning (T-Few) | Actualiza fracción de pesos para reducir costo | Q10, Q19 |
| Vanishing Gradient | Pérdida de señal en secuencias largas RNN | Q36 |

## 4. Trustworthy AI
Principios: Lawful, Ethical, Robust.
- Lawful: Cumplimiento regulatorio (privacidad, protección de datos).
- Ethical: Minimizar sesgos, transparencia, uso responsable.
- Robust: Fiabilidad técnica y resistencia a ataques adversarios.
Aplicación práctica: Monitoreo post-despliegue, auditorías de modelos, filtrado de contenido.

## 5. Infraestructura para AI en OCI
### Superclusters
- Conjuntos de nodos GPU de alta densidad.
- Red RDMA para baja latencia y alto ancho de banda.
- Escalabilidad para entrenamiento de LLM y modelos de visión a gran escala.

### GPUs Disponibles (contexto de preguntas)
- A100: Escala pequeña-mediana (equilibrio rendimiento/memoria).
- GB200: Escenarios masivos (Grace Blackwell, exascala, HPC extremo).
- H100/H200: Generaciones avanzadas (no directamente preguntadas, pero relevantes en comparación).

### Componentes NO de AI Compute
- OCI Vault: Gestión de llaves y secretos (seguridad), no cómputo de IA.

## 6. Diseño de Preguntas y Mejora Continua
Para mejorar la calidad de las preguntas:
1. Evitar duplicados semánticos salvo que refuercen (ej: Select AI repetido -> fusionar en una pregunta multi-parte).
2. Incluir distractores plausibles (opciones incorrectas que representen errores comunes reales).
3. Añadir contexto breve (escenario de negocio) para aumentar aplicabilidad.
4. Balancear taxonomía cognitiva (recordar, comprender, aplicar, analizar).
5. Revisar conclusiones contra documentación oficial para evitar ambigüedades.

### Ejemplo de Mejora
Pregunta original: "GPU para massive-scale?" -> Añadir contexto: "Entrenar un LLM multilingüe de cientos de miles de millones de parámetros" para reforzar la elección de GB200.

### Errores Comunes a Vigilar
- Confundir OCR con Document Classification.
- Usar 'in-context learning' como sinónimo de fine-tuning (son distintos).
- Considerar que Vector Search hace coincidencia exacta de palabras (usa similitud semántica).
- Asumir que cualquier capa oculta 'produce la salida final'.

## 7. Estrategias de Estudio Sugeridas
- Bloques tematizados (Vision, Speech, Language, Infra, Prompting).
- Prácticas espaciadas: repetir cada bloque 24h después.
- Técnica de Enseñar: Explicar cada concepto a otra persona o grabar un audio explicativo.
- Registro de Fallos: Usar `last_wrong.json` (quiz) para enfocarse en debilidades.

## 8. Mapa de Preguntas por Tema
| Tema | Preguntas Oficiales | Opcionales |
|------|---------------------|------------|
| Vision | Q9, Q14, Q32, Q33, Q38, Q23 | O3 |
| Speech | Q12, Q13, Q17, Q19, Q26, Q28 | O7 |
| Language | Q35 | O1, O9 |
| Generative / LLM | Q10, Q15, Q22, Q23, Q27–Q30 | O4, O6 |
| Infra / GPUs | Q24–Q26 | O5 |
| Core ML | Q3, Q6, Q21, Q31, Q34, Q36, Q39, Q40 | O2 |
| Database / Vector | Q22, Q23, Q37 | O8 |
| Trustworthy AI | Q20, Q29 | - |

## 9. Próximas Extensiones
- Añadir sección de preguntas de desarrollo seguro y compliance.
- Incorporar ejemplos de prompts optimizados (zero-shot vs few-shot vs chain-of-thought).
- Añadir métricas de evaluación: precisión, recall, F1 (no incluidas aún).
- Explorar casos de uso multi-servicio (Vision + Language + DB 23ai).

## 10. Referencias Sugeridas
(No se incluyen URLs directas para evitar dependencia; buscar en documentación oficial OCI):
- OCI Data Science Documentation
- OCI AI Services Overview
- Oracle Database 23ai Vector Search Guide
- Trustworthy AI Principles (Oracle / Industria)

## 11. Glosario Rápido
| Término | Definición Breve |
|---------|------------------|
| Embedding | Vector que representa significado semántico de un objeto (texto, imagen). |
| Token | Unidad mínima de texto procesada por un LLM. |
| Endpoint de Inferencia | API que sirve predicciones de un modelo entrenado. |
| OCR | Reconocer y extraer texto de imágenes/documentos escaneados. |
| Key-Value Extraction | Identificar pares estructurados en documentos. |
| Few-Shot | Prompt con pocos ejemplos para guiar salida. |
| In-Context Learning | Uso de ejemplos en el prompt para adaptar respuesta sin reentrenar. |
| Vanishing Gradient | Pérdida de magnitud del gradiente en redes recurrentes largas. |
| T-Few | Método parameter-efficient fine-tuning en OCI Generative AI. |
| RDMA | Acceso directo a memoria remota con baja latencia. |

## 12. Checklist de Calidad para Nuevas Preguntas
Antes de agregar una nueva pregunta:
1. ¿El distractor más plausible refleja un error conceptual común?
2. ¿La respuesta es inequívoca con base en documentación oficial?
3. ¿El escenario aporta aplicación práctica (si corresponde)?
4. ¿Evita ambigüedad terminológica (OCR vs Clasificación Documentos)?
5. ¿No duplica innecesariamente otra pregunta sin variar el ángulo cognitivo?

## 13. Conclusión
Este documento extiende el material inicial proporcionando una base teórica estructurada y criterios de mejora continua para el banco de preguntas. Úsalo junto con el `quiz.py` para un ciclo de aprendizaje activo: leer -> probar -> analizar fallos -> reforzar.

---
Fin de documentacion.
