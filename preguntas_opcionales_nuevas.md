# Preguntas Opcionales Nuevas (Derivadas de Skill Check / Fuentes Externas Parafraseadas)

Este archivo agrega preguntas adicionales NO presentes de forma equivalente en el banco oficial (Q1–Q41). Se han PARAFRASEADO para evitar copia literal y se incluyen explicaciones en español. Si un tema estaba cubierto de forma casi idéntica en las oficiales se omitió. IDs comienzan en O110 para no colisionar.

Leyenda:
- ✅ Respuesta correcta
- Duplicadas/Omitidas: Reinforcement básico (ya tocado tangencialmente), spam/regresión, tokens, RNN característica general, object detection vehículos, etc.

## Tabla de Contenido
O110–O134 (25 preguntas)

---
## Lista de Nuevas Preguntas

### O110. Identificar tarea Generative AI
¿Cuál de los siguientes ejemplos representa una tarea típica de Generative AI?
A. Detectar fraude en tarjetas
B. Calcular número total de palabras
C. Identificar tema de una noticia
D. Redactar un poema a partir de un tema ✅
Explicación: Generative AI produce contenido nuevo (texto, imagen, audio) a partir de patrones aprendidos.

### O111. Uso de Reinforcement Learning en conducción autónoma
¿Qué tipo de aprendizaje se emplea para que un vehículo autónomo mejore decisiones mediante recompensas por conducción segura?
A. Aprendizaje supervisado
B. Aprendizaje no supervisado
C. Reinforcement Learning ✅
D. NLP
Explicación: El agente (coche) interactúa con entorno y optimiza recompensa acumulada (seguridad, eficiencia).

### O112. Tarea NO típica de visión
¿Cuál NO es un caso central de Computer Vision en el contexto del examen?
A. Reconocimiento facial
B. Clasificación de imágenes
C. Detección de objetos
D. Reparación/restauración de imágenes dañadas ✅
Explicación: Restauración es posible con IA, pero el examen se centra en reconocer, clasificar y localizar.

### O113. Aprendizaje para descubrir tendencias sin etiquetas
¿Qué paradigma se utiliza para encontrar patrones o grupos en datos sin etiquetas?
A. Supervisado
B. Unsupervised Learning ✅
C. Reinforcement Learning
D. Regresión logística
Explicación: El aprendizaje no supervisado identifica estructura inherente (clusters, asociaciones) sin objetivos definidos.

### O114. Caso que NO necesita ML
¿Cuál de estas aplicaciones típicamente no requiere Machine Learning?
A. Validación de contraseña por longitud y caracteres ✅
B. Detección de spam
C. Segmentación de clientes
D. Predicción de precios de acciones
Explicación: Validar contraseña aplica reglas determinísticas simples.

### O115. Función activación en Logistic Regression
¿Qué función se usa para mapear la combinación lineal de entradas a probabilidad en regresión logística?
A. Identidad
B. Escalón
C. Sigmoide (sigmoidal) ✅
D. Gaussiana
Explicación: Sigmoid ∈ (0,1) permite interpretar salida como probabilidad de clase.

### O116. Arquitectura RNN para traducción máquina
¿Qué arquitectura secuencial soporta entrada y salida como secuencias (source→target)?
A. One-to-One
B. One-to-Many
C. Many-to-One
D. Many-to-Many ✅
Explicación: Traducción requiere mapear secuencia completa a otra secuencia completa.

### O117. Modelo para dependencias largas en secuencias
¿Qué tipo de red maneja mejor dependencia de largo plazo en secuencias?
A. RNN simple
B. CNN
C. LSTM ✅
D. Perceptrón multicapa sin memoria
Explicación: LSTM introduce puertas que mitigan vanishing gradient y preservan información.

### O118. Elemento que realiza suma ponderada + activación
En una red neuronal ¿qué componente combina entradas y activa para producir señal de salida?
A. Neurona ✅
B. Bias
C. Clasificador externo
D. Iterador
Explicación: La neurona aplica w·x + b y luego función de activación.

### O119. Cuándo NO necesitas fine-tuning de LLM
Fine-tuning de un LLM puede omitirse cuando tu caso:
A. Requiere adaptación específica a tarea ✅ (si NO lo requiere se omite)
B. Demanda vocabulario muy especializado
C. Busca mitigar sesgo
D. Necesita optimización de latencia
Explicación: Si sólo haces prompting genérico sin adaptación específica, basta ingeniería de prompts.

### O120. Caso NO ideal para modelos de secuencia
¿Cuál NO es la mejor aplicación de modelos secuenciales (RNN/LSTM/Transformers)?
A. Análisis de series temporales
B. Clasificación de imágenes / reconocimiento objetos ✅
C. Traducción automática
D. Reconocimiento de voz
Explicación: Imágenes se abordan mejor con CNN o Vision Transformers diseñados para patrones espaciales.

### O121. Factor que impacta capacidad de un LLM
¿Qué factor impacta fuertemente capacidad y coste de un LLM?
A. Número de botones en la interfaz
B. Lenguaje de programación usado
C. Tamaño del modelo (parámetros, embeddings, tokens) ✅
D. Número de usuarios concurrentes
Explicación: Parámetros y longitud de contexto definen memoria semántica y coste computacional.

### O122. Datatype para comparar documentos en DB 23ai
¿Qué tipo de dato permite almacenar embeddings para búsquedas de similitud?
A. ARRAY
B. VECTOR ✅
C. STRING
D. BOOLEAN
Explicación: VECTOR almacena representaciones densas y habilita comparaciones semánticas.

### O123. Repetición de tareas en OCI Data Science
¿Qué componente facilita ejecutar tareas ML repetibles en infraestructura gestionada?
A. Conda Packs
B. Jobs ✅
C. Compartimentos
D. Notebook Sessions
Explicación: Jobs programan y reproducen ejecuciones (entrenos, evaluaciones) de forma consistente.

### O124. Publicar modelo como endpoint
¿Cuál recurso expone modelos registrados vía HTTP para inferencia?
A. Model Catalog
B. Model Deployments ✅
C. Jobs
D. Artifact Storage
Explicación: Deployment crea endpoint escalable con versionado controlado.

### O125. Servicio que NO es parte de OCI AI Services
¿Cuál NO corresponde a un servicio AI nativo en OCI?
A. Vision
B. Speech
C. Language
D. Translator ✅
Explicación: "Translator" no figura como servicio separado; traducción puede cubrirse vía Language/Generative.

### O126. Diferencia Chat vs Embeddings (Generative AI)
Chat models vs embedding models:
A. Ambos generan texto
B. Chat genera texto, embedding genera vectores semánticos ✅
C. Embedding genera texto, chat vectores
D. Embedding sólo indexa imágenes
Explicación: Embeddings representan significado numérico; chat produce secuencias lingüísticas.

### O127. Propósito del Playground Generative AI
¿Para qué sirve el Playground de OCI Generative AI?
A. Optimizar hardware GPU
B. Visualmente probar modelos (prompt/fine-tuned) sin código ✅
C. Crear redes VCN
D. Convertir imágenes en audio
Explicación: Espacio interactivo para iterar prompts y evaluar respuestas antes de integrar vía API.

### O128. Finalidad de endpoints en OCI Generative AI
¿Cuál es su rol principal?
A. Escalar almacenamiento
B. Servir inferencias de modelos ajustados ✅
C. Generar métricas de facturación
D. Traducir automáticamente SQL
Explicación: Endpoints exponen predicciones con control de versionado y seguridad.

### O129. Recurso necesario para fine-tuning especializado
Para adaptar un LLM a dominio específico se requiere:
A. Shared tenancy genérica
B. Object Storage sin más
C. Dedicated AI Cluster ✅
D. Dashboard de métricas
Explicación: Cluster dedicado provee cómputo garantizado y aislamiento para ajuste de parámetros.

### O130. Idioma NO soportado en lista base Speech (caso ejemplo)
¿Cuál se asume como NO soportado en conjunto dado (ejemplo)?
A. Inglés
B. Español
C. Portugués
D. Mandarín ✅
Explicación: Ejemplo didáctico donde Mandarín no figura (verificar lista oficial actual para el examen real).

### O131. Extraer contenido tabular
Para recuperar estructura de tablas (celdas, encabezados) de PDFs escaneados:
A. Language
B. Speech
C. Document Understanding ✅
D. Object Storage
Explicación: Document Understanding produce estructura y clasificación; Vision apoya OCR y key-value pero DU especializa tablas.

### O132. Capacidad del OCI Language Service
¿Cuál función característica provee?
A. Object detection en imágenes
B. Sentiment analysis de texto ✅
C. Conversión voz a texto
D. Compilación de código
Explicación: Language incluye análisis de sentimiento, clasificación, NER e idioma.

### O133. Algoritmo que ajusta pesos en entrenamiento ANN
¿Cuál algoritmo se usa para propagar errores y actualizar pesos en redes profundas estándar?
A. Random Forest
B. Support Vector Machine
C. Backpropagation ✅
D. K-Means
Explicación: Backprop calcula gradientes de la pérdida respecto a cada peso y guía optimización (normalmente con Gradient Descent / variantes).

### O134. Mecanismo de atención en Transformers
¿Qué logra el mecanismo de self-attention?
A. Obligar al modelo a sólo ver últimas palabras
B. Aplicar misma importancia a cada token
C. Asignar pesos contextuales distintos a cada token en la secuencia ✅
D. Reemplazar embeddings por reglas manuales
Explicación: Self-attention pondera tokens relevantes para representar relaciones de largo alcance.

---
## Resumen Temático Nuevas vs Existentes
| Nueva Pregunta | Tema | ¿Ya cubierta? | Motivo Inclusión |
|----------------|------|---------------|------------------|
| O110 | Generative AI tarea creativa | No exacta | Diferenciar creación vs clasificación |
| O111 | Reinforcement Learning conducción | Parcial (AI general) | Introducir RL explícito |
| O112 | Visión negativa (restauración) | No | Aclarar límites del servicio |
| O113 | Unsupervised descubrimiento | Parcial | Enfatizar clustering/patrones |
| O114 | Regla determinística | No | Explicar casos fuera de ML |
| O115 | Sigmoid logistic | No | Añadir fundamentos clasificadores |
| O116 | Many-to-Many secuencias | No | Arquitecturas secuencia |
| O117 | LSTM dependencias largas | No | Mitigar vanishing gradient |
| O118 | Neurona operación interna | No | Micro-nivel ANN |
| O119 | Cuándo evitar fine-tuning | No | Estrategia costo/caso |
| O120 | No uso secuencial imagen | Parcial | Reforzar elección de arquitectura |
| O121 | Tamaño modelo impacto | Tokens ya, no tamaño global | Completar dimensión recursos |
| O122 | VECTOR datatype | No | Aspecto específico DB 23ai |
| O123 | Jobs Data Science | No | Orquestación repetible |
| O124 | Model Deployments | Parcial (despliegue general) | Recurso concreto |
| O125 | Servicio inexistente (Translator) | No | Diferenciar catálogo real |
| O126 | Chat vs Embeddings | No | Comparación funcional |
| O127 | Playground propósito | No | Uso exploratorio |
| O128 | Endpoint función | Parcial | Rol explícito inferencia |
| O129 | Dedicated AI Cluster | No | Requisito cómputo fine-tune |
| O130 | Idioma no soportado ejemplo | No | Evaluar conocimiento soporte |
| O131 | Document Understanding tablas | Parcial | Profundizar diferencia Vision/DU |
| O132 | Sentiment Language | Parcial (clasificación general) | Función concreta |
| O133 | Backpropagation | No | Algoritmo entrenamiento clave |
| O134 | Self-attention | No | Mecánica interna Transformer |

---
## Nota
Si el examen actualiza lista de idiomas o servicios, revisar O125 y O130 antes de uso. Ninguna pregunta copia texto literal de fuentes externas; todas están reformuladas.

Fin del archivo.
