# Banco Completo (Reconstrucción Verbatim Solicitada)

Este archivo agrupa TODAS las preguntas oficiales Q1–Q41 tal como aparecen en `preguntas_oficiales.md` y prepara espacios para incorporar tus ENUNCIADOS EXTENDIDOS (los que incluyen narrativa y explicaciones largas) pregunta por pregunta. También reserva sección para las opcionales (O101–O109) que ya no constan en el repositorio en su forma original larga.

Por favor: para cada pregunta que quieras versión extendida, pega debajo del bloque "[ENUNCIADO EXTENDIDO PENDIENTE]" el texto EXACTO que me enviaste en su momento (escenario + opciones + explicación larga). Ya añadiste ejemplos de estilo para Q31–Q34; los colocaré cuando me los vuelvas a pasar confirmando que son definitivos.

---
## Oficiales Q1–Q41 (Verbatim Corto Actual)

### Q1
Which algorithm is a non-parametric approach for supervised learning?
- A. Linear Regression
- B. K-Nearest Neighbors (KNN) ✅
- C. Random Forest
- D. Decision Trees
Correct: B. KNN
Explicación: Almacena datos y usa distancias; no ajusta parámetros internos.
ENUNCIADO EXTENDIDO:
K-Nearest Neighbors (KNN) is considered a non-parametric algorithm: Unlike parametric models (e.g., linear regression, neural networks), KNN doesn't have any parameters that need to be learned from the data. The only parameter to tune is the number of nearest neighbors (K).
1. Which algorithm is a non-parametric approach for supervised learning?
O Linear Regression
@ K-Nearest Neighbors (KNN) e
O Random Forest
O Decision Trees

### Q2
OCI Vector Search - What would you use Oracle AI Vector Search for?
- A. Store business data
- B. Manage security protocols
- C. Keyword queries
- D. Semantic queries ✅
Correct: D
Explicación: Búsqueda semántica mediante embeddings.
ENUNCIADO EXTENDIDO:
4. What would you use Oracle AI Vector Search for?
• A. Store business data in a cloud database.
• B. Manage database security protocols.
• C. Query data based on keywords.
• D. Query data based on semantics. ✅
Explicación: Vector Search permite realizar búsquedas de similitud semántica usando embeddings, no coincidencia literal de palabras.

### Q3
ML Concepts - What is 'overfitting'?
- A. Model too simple
- B. Model learns training data too well ✅
- C. Model ignores input
- D. Model has no output
Correct: B
Explicación: Memoriza entrenamiento y generaliza mal.
ENUNCIADO EXTENDIDO:
Q12: ML Concepts - What is 'overfitting'?
• A. Model is too simple
• B. Model learns training data too well ✅
• C. Model ignores input data
• D. Model has no output
Explicación extendida: El sobreajuste ocurre cuando el modelo memoriza ejemplos específicos del entrenamiento, resultando en baja capacidad para generalizar. Se detecta cuando la pérdida de entrenamiento es baja pero la de validación/test es alta. Mitigación: regularización, más datos, early stopping, aumento de datos.

### Q4
Deep Learning - What is a key feature of RNNs?
- A. Parallel processing
- B. Used for images
- C. Feedback loop retains info across time steps ✅
- D. No internal state
Correct: C
Explicación: Conexiones recurrentes mantienen estado temporal.
ENUNCIADO EXTENDIDO:
Q10: Deep Learning - What is a key feature of RNNs?
• A. Parallel processing
• B. Used for images
• C. Feedback loop retains info across time steps ✅
• D. No internal state
Explicación extendida: Una RNN mantiene un estado oculto que se actualiza paso a paso, permitiendo capturar dependencias temporales. Problemas: vanishing/exploding gradient; soluciones: LSTM/GRU, clipping, atención.

### Q5
What is the purpose of the Model Catalog in OCI Data Science?
- Stores raw datasets
- Deploy models as endpoints
- Real-time processing engine
- Repository for storing, tracking, managing ML models ✅
Correct: Repositorio de gestión.
Explicación: Versionado y gobernanza centralizada.
ENUNCIADO EXTENDIDO:
[AÚN NO PROPORCIONADO – PEGAR AQUÍ SI EXISTE]
Q5: OCI AI Infrastructure - What advantage do OCI Superclusters offer for AI workloads?
• A. Ideal for text-to-speech
• B. Integrates with social media
• C. Cost-effective for simple tasks
• D. High performance for complex AI
✅ Respuesta Correcta: D
💡 Explicación: Ofrecen rendimiento y escalabilidad excepcionales para entrenar modelos grandes y complejos.

### Q6
Technique to predict house price based on features?
- Regression ✅
- Time Series Analysis
- Classification
- Clustering
Correct: Regression
Explicación: Variable continua -> regresión.
ENUNCIADO EXTENDIDO:
[AÚN NO PROPORCIONADO – PEGAR AQUÍ SI EXISTE]
Q6: LLMs - What is 'in-context learning' in LLMs?
• A. Training a model on diverse tasks
• B. Modifying model permanently
• C. Zero-shot learning
• D. Providing examples via input prompt
✅ Respuesta Correcta: D
💡 Explicación: Permite al modelo aprender tareas nuevas a partir de ejemplos dentro del propio prompt, sin reentrenar.

### Q7
Service to deploy trained model for real-time predictions?
- OCI Object Storage
- OCI Language
- OCI Data Science ✅
- OCI Speech
Correct: OCI Data Science
Explicación: Despliegue de endpoints.
ENUNCIADO EXTENDIDO:
Q9: OCI Data Science - What feature provides an interactive coding environment for building and training models?
• A. ADS SDK
• B. Conda
• C. Model Catalog
• D. Notebook Sessions ✅
Explicación: Notebook Sessions brindan entorno interactivo (Jupyter) para experimentar y entrenar antes de desplegar.
Q7: OCI AI Services - Which feature does the OCI Speech service offer?
• A. Convert text to images
• B. Recognize objects
• C. Transcribe speech to text
• D. Analyze sentiment
✅ Respuesta Correcta: C
💡 Explicación: El servicio convierte voz en texto, útil para transcripciones y asistentes virtuales.

### Q8
NOT an unsupervised ML application?
- Spam detection ✅
- Outlier detection
- Targeted marketing campaigns
- Customer segmentation
Correct: Spam detection
Explicación: Clasificación supervisada.
ENUNCIADO EXTENDIDO:
Q8: OCI Document Understanding - What can OCI Document Understanding NOT do?
• A. Generate transcript
• B. Extract tables
• C. Classify documents
• D. Extract text ✅ Correct Answer: A
Explicación: No transcribe audio; su foco es estructura de documentos (texto, tablas, tipos).
Q8: OCI Document Understanding - What can OCI Document Understanding NOT do?
• A. Generate transcript
• B. Extract tables
• C. Classify documents
• D. Extract text
✅ Respuesta Correcta: A
💡 Explicación: No genera transcripciones de audio; se centra en procesar texto y tablas de documentos.

### Q9
OCI Vision feature to identify invoice/receipt/resume?
- Table extraction
- Image classification
- Document classification ✅
- OCR
Correct: Document classification
Explicación: Determina tipo documental.
ENUNCIADO EXTENDIDO:
Q3 (otro set): CNN purpose ya registrado en Q3 extendido arriba. [SIN EXTENSIÓN ESPECÍFICA PARA ESTA PREGUNTA AÚN]
Q9: OCI Data Science - What feature provides an interactive coding environment for building and training models?
• A. ADS SDK
• B. Conda
• C. Model Catalog
• D. Notebook Sessions
✅ Respuesta Correcta: D
💡 Explicación: Los Notebook Sessions ofrecen entornos interactivos para desarrollar y entrenar modelos directamente.

### Q10
T-Few fine-tuning reduces cost because it...
- Manual config layers
- Trains entire model from scratch
- Selectively updates fraction of weights ✅
- No customization
Correct: Actualiza pocos parámetros.
Explicación: Parameter-efficient tuning.
ENUNCIADO EXTENDIDO:
Q4 (otro set) generative AI ya reasignado a Q20 abajo. [SIN EXTENSIÓN ESPECÍFICA PARA T-Few AÚN]
Q10: Deep Learning - What is a key feature of RNNs?
• A. Parallel processing
• B. Used for images
• C. Feedback loop retains info across time steps
• D. No internal state
✅ Respuesta Correcta: C
💡 Explicación: Las RNN mantienen memoria a través del tiempo, ideales para datos secuenciales como texto o voz.

### Q11
Data type most used with deep learning?
- Human interpretable features
- Complex non-human interpretable features ✅
- Time series data
- Only string data
Correct: Datos complejos.
Explicación: Imágenes/audio/video.
ENUNCIADO EXTENDIDO:
Q11: OCI Vector Search extendido ya se integró en Q2. [SIN EXTENSIÓN ESPECÍFICA PARA TIPO DE DATOS AÚN]
Q11: OCI Vector Search - What would you use Oracle AI Vector Search for?
• A. Store business data
• B. Manage security protocols
• C. Keyword queries
• D. Semantic queries
✅ Respuesta Correcta: D
💡 Explicación: Permite realizar búsquedas semánticas, comparando significado en lugar de coincidencia exacta de texto.

### Q12
Normalization in OCI Speech improves readability by...
- Translating languages
- Lowercasing all
- Converting numbers/dates/URLs to standard formats ✅
- Removing unnecessary words
Correct: Formatos estándar.
Explicación: Estandariza elementos.
ENUNCIADO EXTENDIDO:
Q6 (otro set) Speech transcribe corresponde a servicio, no a normalización. [SIN EXTENSIÓN ESPECÍFICA PARA NORMALIZACIÓN AÚN]
Q12: ML Concepts - What is 'overfitting'?
• A. Model is too simple
• B. Model learns training data too well
• C. Model ignores input data
• D. Model has no output
✅ Respuesta Correcta: B
💡 Explicación: El sobreajuste ocurre cuando el modelo memoriza los datos de entrenamiento, perdiendo capacidad de generalización.

### Q13
Profanity filtering option to retain words but mark them?
- Tagging ✅
- Removing
- Normalization
ENUNCIADO EXTENDIDO:
Which of these summarizes the three guiding principles for Al to be trustworthy?
O Al should be fast, unbiased, and autonomous.
O Al should replace human oversight, be independent, and highly scalable.
O Al should be cost-effective, cloud-based, and user-friendly.
O Al should be lawful, ethical, and robust. ✅
Explicación extendida: Se enfatiza cumplimiento normativo (lawful), mitigación de sesgos y ética en el uso (ethical), y solidez técnica ante fallos y ataques (robust).
Correct: Tagging
Explicación: Etiqueta sin eliminar.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q14
Vision feature to extract merchant/date/amount?
- OCR
- Document classification
- Key-value extraction ✅
ENUNCIADO EXTENDIDO:
How does Select Al enhance the interaction with Oracle Autonomous Database?
O By improving network security protocols
O By eliminating the need for database administrators
O By enabling natural language prompts instead of SQL code ✅
O By providing advanced data visualization tools
Explicación extendida: Facilita consultas ad-hoc y exploración rápida sin sintaxis SQL manual.
Correct: Key-value extraction
Explicación: Pares clave:valor.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q15
Difference between LLMs and traditional ML models?
- Pretrained on large corpus ✅
Correct: Pretraining masivo.
Explicación: Generalización multitarea.
ENUNCIADO EXTENDIDO:
5. What role do tokens play in Large Language Models (LLMs)?
O They represent the numerical values of model parameters.
O They are individual units into which a piece of text is divided during processing by the model. ✅
O They determine the size of the model's memory.
O They are used to define the architecture of the model's neural network.
Explicación extendida: El texto se fragmenta en tokens (palabras, subpalabras, símbolos) para que el modelo aplique embeddings y atención sobre secuencias discretas.

### Q16
Self-driving car concept applied?
- Artificial Intelligence ✅
Correct: AI
Explicación: Integra múltiples capacidades cognitivas.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q17
Speech feature for per-word certainty?
- Confidence scoring ✅
Correct: Confidence scoring
Explicación: Puntuación de fiabilidad.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q18
Neural network best for generating music sequences?
- RNN ✅
Correct: RNN
Explicación: Maneja dependencias temporales.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q19
Speech feature to add closed captions?
- SRT file support ✅
Correct: SRT
Explicación: Formato estándar subtítulos.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q20
Guiding principles for trustworthy AI?
- Lawful, ethical, robust ✅
Correct: Legal, ética, robusta.
Explicación: Marco de confianza.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q21
Primary function of inference in ML?
- Predict new data outcomes ✅
Correct: Predicción.
Explicación: Uso del modelo entrenado.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q22
How does Select AI generate SQL?
- Connects to LLM, infers intent, formulates SQL ✅
Correct: Mapeo NL→SQL.
Explicación: Interpreta intención.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q23
Select AI enhances interaction with Autonomous DB by...
- Enabling natural language prompts instead of SQL code ✅
Correct: Prompts NL.
Explicación: Reduce necesidad de escribir SQL.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q24
NOT part of OCI AI Infrastructure?
- OCI Vault ✅
Correct: OCI Vault
Explicación: Gestión de llaves, no cómputo AI.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q25
GPU for massive-scale HPC AI workloads?
- GB200 ✅
Correct: GB200
Explicación: Grace Blackwell exascala.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q26
GPU for small/medium-scale training/inference?
- A100 ✅
Correct: A100
Explicación: Equilibrio rendimiento/memoria.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q27
Prompt technique with explicit examples guiding response?
- Few-shot prompting ✅
Correct: Few-shot.
Explicación: Ejemplos en prompt.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q28
Role of tokens in LLMs?
- Minimal units text is divided into ✅
Correct: Tokens
Explicación: Unidad mínima de procesamiento.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q29
Model to complete poem lines suggesting words?
- RNN ✅
Correct: RNN
Explicación: Contexto secuencial.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q30
Pretraining process of Generative AI model?
- Learns patterns without labeled data ✅
Correct: Auto-supervisión.
Explicación: Predicción de tokens/masks.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q31
Purpose of hidden layer in ANN?
- Processes/transforms inputs via weights & activations ✅
Correct: Transformación no lineal.
Explicación: Representaciones internas.
ENUNCIADO EXTENDIDO:
Hidden layers , take the input from input or other hidden layer and multiples it through weights and activations. Input layer accepts input and output layer outputs the final result.
31. What is the purpose of the hidden layer in an artificial neural network?
O This layer is optional, and it processes and transforms inputs from the network's weights and activation functions. e
O This layer receives and passes input data to the subsequent layers; it does not perform any computations.
O This layer applies filters to the image data.
@ This layer produces the final outputs of the network based on the processed information from the other layers. S

### Q32
Locate & label vehicles and plates per frame?
- Object detection ✅
Correct: Object detection
Explicación: Bounding boxes múltiples.
ENUNCIADO EXTENDIDO:
To detect and label specific objects (vehicles and license plates) within images, object detection is the best choice.
32. Lisa runs an automated security system that monitors parking lots using cameras. She wants to locate and label vehicles and license plates in each frame.
Which OCI Vision feature should she use?
@ Image classification
O Object detection
C) Speech-to-text
O Document Classification

### Q33
AI subset for image classification?
- Deep Learning ✅
Correct: Deep Learning
Explicación: CNN / Vision Transformers.
ENUNCIADO EXTENDIDO:
Object detection is implemented using Deep Learning. Hence the answer is Deep Learning.
33. You're developing an image classification software that can identify specific objects.
Which AI subset would you use?
@ Reinforcement Learning
O Machine Learning
O Deep Learning e
O Natural Language Processing

### Q34
Role of target variable in supervised learning?
- Desired output / class labels ✅
Correct: Etiquetas.
Explicación: Calcula pérdida.
ENUNCIADO EXTENDIDO:
The target variable refers to desired outcome. It could be a numerical value or a label. e.g. spam or not spam or predicted rainfall in milimeters.
34. What is the role of a target variable in supervised learning?
@ It helps in feature selection. S
O It represents the input data.
O It is used to split the dataset.
O It contains the desired output or class labels. e

### Q35
Categorize news articles (Politics/Tech/Sports)?
- Text classification ✅
Correct: Text classification
Explicación: Etiquetado temático.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q36
Primary limitation of RNNs on long sequences?
- Vanishing gradient long-range dependencies ✅
Correct: Vanishing gradient
Explicación: Gradiente se atenúa.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q37
Use pretrained AI models for vector search in DB 23ai?
- Loading ONNX models directly ✅
Correct: ONNX
Explicación: Embeddings en la base.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q38
Network best for face recognition?
- CNN ✅
Correct: CNN
Explicación: Rasgos espaciales jerárquicos.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q39
Technique to reduce spam via automated filtering?
- Machine Learning ✅
Correct: ML supervisado
Explicación: Clasificación spam/no spam.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q40
Data type for predicting stock prices?
- Time series data ✅
Correct: Time series
Explicación: Serie temporal indexada.
[ENUNCIADO EXTENDIDO PENDIENTE]

### Q41
Role of loss function in supervised learning algorithms?
- A. It helps in feature scaling.
- B. It measures the similarity between predictions and actual targets.
- C. It evaluates the model's complexity.
- D. It quantifies the cost of incorrect predictions. ✅
Correct: D. Quantifies cost of incorrect predictions.
Explicación: La función de pérdida define numéricamente el error (diferencia entre predicción y objetivo) y guía el ajuste de parámetros minimizándolo (optimización). La opción B es ambigua porque algunas pérdidas implícitamente miden disimilitud, pero la formulación estándar es cuantificar el coste del error.
ENUNCIADO EXTENDIDO:
6. What is the role of the loss function in supervised learning algorithms?
O It helps in feature scaling.
O It measures the similarity between predictions and actual targets.
O It evaluates the model's complexity.
O It quantifies the cost of incorrect predictions. ✅
Explicación extendida: La pérdida guía el descenso de gradiente; define objetivo de optimización (ej. MSE, Cross-Entropy). Un buen diseño de la pérdida alinea métricas de negocio con el entrenamiento.

---
## Opcionales O101–O109 (Necesitan Texto Original Extendido)
Actualmente sólo disponemos de la lista depurada (archivo `preguntas_no_oficiales.md`). Si deseas recuperar las versiones largas, pégalas aquí una por una usando el mismo patrón:

Formato sugerido:
```
O101. <Enunciado largo / escenario>
Opciones:
A. ...
B. ...
C. ... ✅ (si corresponde marcar)
D. ...
Explicación: ... (detalle completo)
```

Placeholders:
- O101 [PENDIENTE]
- O102 [PENDIENTE]
- O103 [PENDIENTE]
- O104 [PENDIENTE]
- O105 [PENDIENTE]
- O106 [PENDIENTE]
- O107 [PENDIENTE]
- O108 [PENDIENTE]
- O109 [PENDIENTE]

---
## Instrucciones para Continuar
1. Pega cada bloque extendido donde veas "[ENUNCIADO EXTENDIDO ...]" sin cambiar lo ya existente.
2. Avísame cuando hayas completado algunas preguntas y puedo limpiar los marcadores.
3. Cuando tengamos todas las versiones largas, puedo generar otro banco específico para el quiz con "modo extendido".

---
Fin de reconstrucción inicial. Esperando tus enunciados extendidos para completar.

---
## Banco Extendido Usuario (Set Alternativo Original Q1–Q12)

SE CONSERVA A CONTINUACIÓN el primer bloque de 12 preguntas extendidas que compartiste (numeración alternativa) para referencia histórica tal como se enviaron inicialmente, sin reasignación a numeración oficial:

1. AI Fundamentals - Which AI domain is associated with tasks like identifying the sentiment of a text and translating text between languages?
• A. Natural Language Processing ✅
• B. Computer Vision
• C. Speech Processing
• D. Anomaly Detection
Explicación: NLP procesa lenguaje humano (sentimiento, traducción).

2. Machine Learning Fundamentals - In Machine Learning, what does 'Model training' involve?
• A. Writing code for the entire program
• B. Collecting and labeling data
• C. Establishing a relationship between input and output parameters ✅
• D. Analyzing the accuracy of a trained model
Explicación: Ajuste de parámetros que relacionan entradas y salidas.

3. Deep Learning Fundamentals - What is the primary purpose of Convolutional Neural Networks (CNNs)?
• A. Generating high-resolution images
• B. Creating music compositions
• C. Processing sequential data
• D. Detecting patterns in images ✅
Explicación: CNN extrae características jerárquicas (bordes → formas → objetos).

4. Generative AI Fundamentals - What distinguishes generative AI from supervised learning?
• A. Focuses on decision-making
• B. Understands data distribution to create new examples ✅
• C. Generates labeled outputs for training
• D. Used only for text-based apps
Explicación: Modela distribución para generar muestras nuevas.

5. OCI AI Infrastructure - What advantage do OCI Superclusters offer for AI workloads?
• A. Ideal for text-to-speech
• B. Integrates with social media
• C. Cost-effective for simple tasks
• D. High performance for complex AI ✅
Explicación: Escalabilidad alta + RDMA + GPUs densas.

6. LLMs - What is 'in-context learning' in LLMs?
• A. Training a model on diverse tasks
• B. Modifying model permanently
• C. Zero-shot learning
• D. Providing examples via input prompt ✅
Explicación: Adapta comportamiento con ejemplos sin ajuste de pesos.

7. OCI AI Services - Which feature does the OCI Speech service offer?
• A. Convert text to images
• B. Recognize objects
• C. Transcribe speech to text ✅
• D. Analyze sentiment
Explicación: Voz → texto para transcripciones.

8. OCI Document Understanding - What can OCI Document Understanding NOT do?
• A. Generate transcript ✅
• B. Extract tables
• C. Classify documents
• D. Extract text
Explicación: No transcribe audio.

9. OCI Data Science - What feature provides an interactive coding environment for building and training models?
• A. ADS SDK
• B. Conda
• C. Model Catalog
• D. Notebook Sessions ✅
Explicación: Entorno interactivo de experimentación.

10. Deep Learning - What is a key feature of RNNs?
• A. Parallel processing
• B. Used for images
• C. Feedback loop retains info across time steps ✅
• D. No internal state
Explicación: Estado oculto para secuencias.

11. OCI Vector Search - What would you use Oracle AI Vector Search for?
• A. Store business data
• B. Manage security protocols
• C. Keyword queries
• D. Semantic queries ✅
Explicación: Búsqueda semántica con embeddings.

12. ML Concepts - What is 'overfitting'?
• A. Model is too simple
• B. Model learns training data too well ✅
• C. Model ignores input data
• D. Model has no output
Explicación: Memoriza entrenamiento, falla al generalizar.
