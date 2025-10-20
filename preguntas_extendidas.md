# Banco de Preguntas Extendidas (Consolidación Verbatim)

Este archivo reúne SOLO los enunciados extendidos y explicaciones largas que aparecieron en la conversación. No altera textos, no inventa contenido nuevo. Donde hubo mezcla incorrecta entre pregunta y bloque, separamos y marcamos como NO ASIGNADO. Donde falta el largo original, se marca como "NO DISPONIBLE (no se encontró en historial)".

Leyenda:
- [OK] Bloque extendido presente (verbatim).
- [FALTA] No se recuperó tu versión extendida propia.
- [DESALINEADO] El bloque que estaba pegado pertenece a otro tema; lo movimos a "Fragmentos Desalineados".

---
## Preguntas Extendidas Recuperadas (Orden libre)

### KNN no paramétrico (Originalmente Q1 corto)
[OK]
K-Nearest Neighbors (KNN) is considered a non-parametric algorithm: Unlike parametric models (e.g., linear regression, neural networks), KNN doesn't have any parameters that need to be learned from the data. The only parameter to tune is the number of nearest neighbors (K).
1. Which algorithm is a non-parametric approach for supervised learning?
O Linear Regression
@ K-Nearest Neighbors (KNN) e
O Random Forest
O Decision Trees
Explicación: Almacena datos y usa distancias; no ajusta parámetros internos.

### Vector Search (Originalmente Q2 corto)
[OK]
4. What would you use Oracle AI Vector Search for?
• A. Store business data in a cloud database.
• B. Manage database security protocols.
• C. Query data based on keywords.
• D. Query data based on semantics. ✅
Explicación: Vector Search permite realizar búsquedas de similitud semántica usando embeddings, no coincidencia literal de palabras.

### Overfitting (Originalmente Q3 / también alternativo #12)
[OK]
ML Concepts - What is 'overfitting'?
• A. Model is too simple
• B. Model learns training data too well ✅
• C. Model ignores input data
• D. Model has no output
Explicación extendida: El sobreajuste ocurre cuando el modelo memoriza ejemplos específicos del entrenamiento, resultando en baja capacidad para generalizar. Se detecta cuando la pérdida de entrenamiento es baja pero la de validación/test es alta. Mitigación: regularización, más datos, early stopping, aumento de datos.

### RNN característica clave (Originalmente Q4 / alternativo #10)
[OK]
Deep Learning - What is a key feature of RNNs?
• A. Parallel processing
• B. Used for images
• C. Feedback loop retains info across time steps ✅
• D. No internal state
Explicación extendida: Una RNN mantiene un estado oculto que se actualiza paso a paso, permitiendo capturar dependencias temporales. Problemas: vanishing/exploding gradient; soluciones: LSTM/GRU, clipping, atención.

### Superclusters (Se había pegado bajo Q5 corto Model Catalog) 
[DESALINEADO]
OCI AI Infrastructure - What advantage do OCI Superclusters offer for AI workloads?
• A. Ideal for text-to-speech
• B. Integrates with social media
• C. Cost-effective for simple tasks
• D. High performance for complex AI ✅
Explicación: Escalabilidad alta + RDMA + GPUs densas.

### In-Context Learning (Se había pegado bajo Q6 corto Regression)
[DESALINEADO]
LLMs - What is 'in-context learning' in LLMs?
• A. Training a model on diverse tasks
• B. Modifying model permanently
• C. Zero-shot learning
• D. Providing examples via input prompt ✅
Explicación: Adapta comportamiento con ejemplos sin ajuste de pesos.

### Notebook Sessions (Se había mezclado bajo Q7 / Q9)
[DESALINEADO]
OCI Data Science - What feature provides an interactive coding environment for building and training models?
• A. ADS SDK
• B. Conda
• C. Model Catalog
• D. Notebook Sessions ✅
Explicación: Entorno interactivo de experimentación.

### Speech: Transcribe (Se mezcló en Q7 corto de despliegue y Q12 normalización)
[DESALINEADO]
OCI AI Services - Which feature does the OCI Speech service offer?
• A. Convert text to images
• B. Recognize objects
• C. Transcribe speech to text ✅
• D. Analyze sentiment
Explicación: Voz → texto para transcripciones.

### Document Understanding LIMITACIÓN (Se colocó en Q8 spam detection)
[DESALINEADO]
OCI Document Understanding - What can OCI Document Understanding NOT do?
• A. Generate transcript ✅
• B. Extract tables
• C. Classify documents
• D. Extract text
Explicación: No transcribe audio.

### Tokens (Se pegó bajo Q15 LLMs vs traditional / y referencia Q28)
[DESALINEADO]
What role do tokens play in Large Language Models (LLMs)?
O They represent the numerical values of model parameters.
O They are individual units into which a piece of text is divided during processing by the model. ✅
O They determine the size of the model's memory.
O They are used to define the architecture of the model's neural network.
Explicación: Fragmentación en unidades mínimas para embeddings y atención.

### Trustworthy AI principios (Se mezcló en Q13 Tagging)
[DESALINEADO]
Which of these summarizes the three guiding principles for AI to be trustworthy?
O Al should be fast, unbiased, and autonomous.
O Al should replace human oversight, be independent, and highly scalable.
O Al should be cost-effective, cloud-based, and user-friendly.
O Al should be lawful, ethical, and robust. ✅
Explicación extendida: Cumplimiento normativo (lawful), mitigación de sesgos y ética (ethical), solidez técnica ante fallos y ataques (robust).

### Select AI interacción NL→SQL (Se mezcló en Q14 key-value y en Q22/Q23)
[DESALINEADO]
How does Select AI enhance the interaction with Oracle Autonomous Database?
O By improving network security protocols
O By eliminating the need for database administrators
O By enabling natural language prompts instead of SQL code ✅
O By providing advanced data visualization tools
Explicación: Facilita consultas ad-hoc y exploración rápida sin escribir SQL manual.

### Hidden Layer propósito (Q31)
[OK]
Hidden layers take the input from input or other hidden layer and multiply it through weights and activations. Input layer accepts input and output layer outputs the final result.
31. What is the purpose of the hidden layer in an artificial neural network?
O This layer is optional, and it processes and transforms inputs from the network's weights and activation functions. e
O This layer receives and passes input data to the subsequent layers; it does not perform any computations.
O This layer applies filters to the image data.
@ This layer produces the final outputs of the network based on the processed information from the other layers. S

### Vision: Object Detection escenario (Q32)
[OK]
To detect and label specific objects (vehicles and license plates) within images, object detection is the best choice.
32. Lisa runs an automated security system that monitors parking lots using cameras. She wants to locate and label vehicles and license plates in each frame.
Which OCI Vision feature should she use?
@ Image classification
O Object detection
C) Speech-to-text
O Document Classification

### Deep Learning para clasificación de imágenes (Q33)
[OK]
Object detection is implemented using Deep Learning. Hence the answer is Deep Learning.
33. You're developing an image classification software that can identify specific objects.
Which AI subset would you use?
@ Reinforcement Learning
O Machine Learning
O Deep Learning e
O Natural Language Processing

### Target variable (Q34)
[OK]
The target variable refers to desired outcome. It could be a numerical value or a label. e.g. spam or not spam or predicted rainfall in milimeters.
34. What is the role of a target variable in supervised learning?
@ It helps in feature selection. S
O It represents the input data.
O It is used to split the dataset.
O It contains the desired output or class labels. e

### Loss Function rol (Q41)
[OK]
6. What is the role of the loss function in supervised learning algorithms?
O It helps in feature scaling.
O It measures the similarity between predictions and actual targets.
O It evaluates the model's complexity.
O It quantifies the cost of incorrect predictions. ✅
Explicación extendida: La pérdida guía el descenso de gradiente; define objetivo de optimización (MSE, Cross-Entropy). Alinea errores numéricos con metas de negocio.

---
## Preguntas sin versión extendida recuperada
(Se encontró solo versión corta, faltó tu bloque largo original)
- Model Catalog (Q5) [FALTA]
- Regression (Q6) [FALTA]
- Vision Document Classification (Q9) [FALTA]
- T-Few fine-tuning (Q10) [FALTA]
- Tipo de datos más usados en DL (Q11) [FALTA]
- Speech Normalization (Q12) [FALTA]
- Profanity Tagging (Q13) [FALTA]
- Key-Value Extraction contexto factura (Q14) [FALTA]
- LLMs vs Traditional ML corpus (Q15) [FALTA]
- Self-driving car concepto (Q16) [FALTA]
- Confidence scoring detalle (Q17) [FALTA]
- RNN para música (Q18) [FALTA]
- SRT captions (Q19) [FALTA]
- Trustworthy AI (Q20) BLOQUE YA RECUPERADO (ver arriba en desalineados) pero falta versión adaptada exacta para pregunta.
- Inference función (Q21) [FALTA]
- Select AI generación SQL (Q22) BLOQUE recuperado arriba.
- Select AI prompts NL (Q23) BLOQUE recuperado arriba.
- OCI Vault no es compute (Q24) [FALTA]
- GPU GB200 (Q25) BLOQUE Superclusters relacionado pero no específico—[FALTA versión dedicada]
- GPU A100 (Q26) [FALTA]
- Few-shot prompting (Q27) [FALTA]
- Tokens (Q28) BLOQUE recuperado.
- RNN completar poema (Q29) [FALTA]
- Pretraining generative (Q30) [FALTA]
- Vision vehículos y placas (Q32) OK
- CNN face recognition (Q38) [FALTA]
- Spam filtering ML (Q39) [FALTA]
- Time series stock (Q40) [FALTA]
- Text classification noticias (Q35) [FALTA]
- Vanishing gradient (Q36) [FALTA]
- ONNX Vector Search DB23ai (Q37) [FALTA]

---
## Fragmentos Desalineados (para que no se pierdan)
Ya listados en secciones DESALINEADO arriba.

---
## Banco Extendido Usuario (Set Alternativo Original Q1–Q12)
(Conservado tal cual, no duplico aquí para evitar repetición excesiva. Ver archivo `preguntas_completas.md` si se desea la versión íntegra.)

---
## Nota Final
Si en algún momento decides que sí quieres reconstrucciones (crear un bloque largo donde falta usando estilo consistente), puedo hacerlo pero quedará claramente marcado como reconstrucción no-verbatim. Por ahora este archivo es puramente extracción de lo que ya existía.

Fin.
