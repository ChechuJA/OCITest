# Preguntas Oficiales OCI Foundations (Q1–Q40)

Este documento separa exclusivamente las 40 preguntas oficiales con sus respuestas y explicaciones en español. Corresponden al banco consolidado final (Q1=KNN, Q2=Vector Search, etc. tal como está en `examen.md`).

## Tabla de Contenido

1. [Uso](#uso)
2. [Listado de Preguntas Q1–Q40](#listado-de-preguntas-q140)
3. [Resumen Rápido](#resumen-rapido)
4. [Mapa Temático](#mapa-tematico)

---
## Uso
Lee cada pregunta intentando responder antes de ver la opción correcta (marcada con ✅). Usa este archivo para repaso limpio sin secciones extra.

---
## Listado de Preguntas Q1–Q40

### Q1
Which algorithm is a non-parametric approach for supervised learning?
- A. Linear Regression
- B. K-Nearest Neighbors (KNN) ✅
- C. Random Forest
- D. Decision Trees
Correct: B. KNN
Explicación: Almacena datos y usa distancias; no ajusta parámetros internos.

### Q2
OCI Vector Search - What would you use Oracle AI Vector Search for?
- A. Store business data
- B. Manage security protocols
- C. Keyword queries
- D. Semantic queries ✅
Correct: D
Explicación: Búsqueda semántica mediante embeddings.

### Q3
ML Concepts - What is 'overfitting'?
- A. Model too simple
- B. Model learns training data too well ✅
- C. Model ignores input
- D. Model has no output
Correct: B
Explicación: Memoriza entrenamiento y generaliza mal.

### Q4
Deep Learning - What is a key feature of RNNs?
- A. Parallel processing
- B. Used for images
- C. Feedback loop retains info across time steps ✅
- D. No internal state
Correct: C
Explicación: Conexiones recurrentes mantienen estado temporal.

### Q5
What is the purpose of the Model Catalog in OCI Data Science?
- Stores raw datasets
- Deploy models as endpoints
- Real-time processing engine
- Repository for storing, tracking, managing ML models ✅
Correct: Repositorio de gestión.
Explicación: Versionado y gobernanza centralizada.

### Q6
Technique to predict house price based on features?
- Regression ✅
- Time Series Analysis
- Classification
- Clustering
Correct: Regression
Explicación: Variable continua -> regresión.

### Q7
Service to deploy trained model for real-time predictions?
- OCI Object Storage
- OCI Language
- OCI Data Science ✅
- OCI Speech
Correct: OCI Data Science
Explicación: Despliegue de endpoints.

### Q8
NOT an unsupervised ML application?
- Spam detection ✅
- Outlier detection
- Targeted marketing campaigns
- Customer segmentation
Correct: Spam detection
Explicación: Clasificación supervisada.

### Q9
OCI Vision feature to identify invoice/receipt/resume?
- Table extraction
- Image classification
- Document classification ✅
- OCR
Correct: Document classification
Explicación: Determina tipo documental.

### Q10
T-Few fine-tuning reduces cost because it...
- Manual config layers
- Trains entire model from scratch
- Selectively updates fraction of weights ✅
- No customization
Correct: Actualiza pocos parámetros.
Explicación: Parameter-efficient tuning.

### Q11
Data type most used with deep learning?
- Human interpretable features
- Complex non-human interpretable features ✅
- Time series data
- Only string data
Correct: Datos complejos.
Explicación: Imágenes/audio/video.

### Q12
Normalization in OCI Speech improves readability by...
- Translating languages
- Lowercasing all
- Converting numbers/dates/URLs to standard formats ✅
- Removing unnecessary words
Correct: Formatos estándar.
Explicación: Estandariza elementos.

### Q13
Profanity filtering option to retain words but mark them?
- Tagging ✅
- Removing
- Normalization
- Masking
Correct: Tagging
Explicación: Etiqueta sin eliminar.

### Q14
Vision feature to extract merchant/date/amount?
- OCR
- Document classification
- Key-value extraction ✅
- Table extraction
Correct: Key-value extraction
Explicación: Pares clave:valor.

### Q15
Difference between LLMs and traditional ML models?
- Pretrained on large corpus ✅
Correct: Pretraining masivo.
Explicación: Generalización multitarea.

### Q16
Self-driving car concept applied?
- Artificial Intelligence ✅
Correct: AI
Explicación: Integra múltiples capacidades cognitivas.

### Q17
Speech feature for per-word certainty?
- Confidence scoring ✅
Correct: Confidence scoring
Explicación: Puntuación de fiabilidad.

### Q18
Neural network best for generating music sequences?
- RNN ✅
Correct: RNN
Explicación: Maneja dependencias temporales.

### Q19
Speech feature to add closed captions?
- SRT file support ✅
Correct: SRT
Explicación: Formato estándar subtítulos.

### Q20
Guiding principles for trustworthy AI?
- Lawful, ethical, robust ✅
Correct: Legal, ética, robusta.
Explicación: Marco de confianza.

### Q21
Primary function of inference in ML?
- Predict new data outcomes ✅
Correct: Predicción.
Explicación: Uso del modelo entrenado.

### Q22
How does Select AI generate SQL?
- Connects to LLM, infers intent, formulates SQL ✅
Correct: Mapeo NL→SQL.
Explicación: Interpreta intención.

### Q23
Select AI enhances interaction with Autonomous DB by...
- Enabling natural language prompts instead of SQL code ✅
Correct: Prompts NL.
Explicación: Reduce necesidad de escribir SQL.

### Q24
NOT part of OCI AI Infrastructure?
- OCI Vault ✅
Correct: OCI Vault
Explicación: Gestión de llaves, no cómputo AI.

### Q25
GPU for massive-scale HPC AI workloads?
- GB200 ✅
Correct: GB200
Explicación: Grace Blackwell exascala.

### Q26
GPU for small/medium-scale training/inference?
- A100 ✅
Correct: A100
Explicación: Equilibrio rendimiento/memoria.

### Q27
Prompt technique with explicit examples guiding response?
- Few-shot prompting ✅
Correct: Few-shot.
Explicación: Ejemplos en prompt.

### Q28
Role of tokens in LLMs?
- Minimal units text is divided into ✅
Correct: Tokens
Explicación: Unidad mínima de procesamiento.

### Q29
Model to complete poem lines suggesting words?
- RNN ✅
Correct: RNN
Explicación: Contexto secuencial.

### Q30
Pretraining process of Generative AI model?
- Learns patterns without labeled data ✅
Correct: Auto-supervisión.
Explicación: Predicción de tokens/masks.

### Q31
Purpose of hidden layer in ANN?
- Processes/transforms inputs via weights & activations ✅
Correct: Transformación no lineal.
Explicación: Representaciones internas.

### Q32
Locate & label vehicles and plates per frame?
- Object detection ✅
Correct: Object detection
Explicación: Bounding boxes múltiples.

### Q33
AI subset for image classification?
- Deep Learning ✅
Correct: Deep Learning
Explicación: CNN / Vision Transformers.

### Q34
Role of target variable in supervised learning?
- Desired output / class labels ✅
Correct: Etiquetas.
Explicación: Calcula pérdida.

### Q35
Categorize news articles (Politics/Tech/Sports)?
- Text classification ✅
Correct: Text classification
Explicación: Etiquetado temático.

### Q36
Primary limitation of RNNs on long sequences?
- Vanishing gradient long-range dependencies ✅
Correct: Vanishing gradient
Explicación: Gradiente se atenúa.

### Q37
Use pretrained AI models for vector search in DB 23ai?
- Loading ONNX models directly ✅
Correct: ONNX
Explicación: Embeddings en la base.

### Q38
Network best for face recognition?
- CNN ✅
Correct: CNN
Explicación: Rasgos espaciales jerárquicos.

### Q39
Technique to reduce spam via automated filtering?
- Machine Learning ✅
Correct: ML supervisado
Explicación: Clasificación spam/no spam.

### Q40
Data type for predicting stock prices?
- Time series data ✅
Correct: Time series
Explicación: Serie temporal indexada.

### Q41
Role of loss function in supervised learning algorithms?
- A. It helps in feature scaling.
- B. It measures the similarity between predictions and actual targets.
- C. It evaluates the model's complexity.
- D. It quantifies the cost of incorrect predictions. ✅
Correct: D. Quantifies cost of incorrect predictions.
Explicación: La función de pérdida define numéricamente el error (diferencia entre predicción y objetivo) y guía el ajuste de parámetros minimizándolo (optimización). La opción B es ambigua porque algunas pérdidas implícitamente miden disimilitud, pero la formulación estándar es cuantificar el coste del error.

---
## Resumen Rápido
- Infraestructura: Superclusters (alto rendimiento), GPUs (GB200 exascala, A100 mediana).
- Servicios: Data Science (despliegue), Vision (clasificación, extracción), Speech (transcripción, SRT, confianza), Language (clasificación texto), Vector Search (búsqueda semántica).
- Técnicas: Few-shot, in-context, T-Few, tokens, embeddings.
- Riesgos: Overfitting, vanishing gradient.
- Principios éticos: Legal, ética, robusta.

## Mapa Temático
- ML Fundamentos: Q3, Q21, Q34
- Deep Learning: Q4, Q18, Q29, Q31, Q36
- Infraestructura GPU: Q25–Q26
- Vision: Q9, Q14, Q32, Q38
- Speech: Q12, Q13, Q17, Q19, Q21
- Language / Texto: Q35, Q28 (tokens)
- Generative / LLM: Q10, Q15, Q22, Q23, Q27, Q28, Q30
- Vector / Base de Datos: Q2, Q37
- Ética / Confiabilidad: Q20
- Optimización / Entrenamiento: Q41

---
Fin del documento.
