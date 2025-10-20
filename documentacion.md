# 📘 Documentación Ampliada OCI Foundations (AI Focus)

> Guía enriquecida para el examen **Oracle Cloud Infrastructure AI Foundations Associate (1Z0-1122-25)**.
> Incluye conceptos clave, servicios, métricas, buenas prácticas y mapa temático de preguntas oficiales.

## 🔍 Tabla de Contenidos
1. [Resumen Ejecutivo](#-resumen-ejecutivo)
2. [Distribución Teórica](#-distribución-teórica)
3. [Panorama General OCI](#-panorama-general-de-oci)
4. [Servicios de IA en OCI](#-servicios-de-ia-en-oci)
5. [Conceptos Clave ML/DL](#-conceptos-clave-de-mldl)
6. [Trustworthy AI](#-trustworthy-ai)
7. [Infraestructura para AI](#-infraestructura-para-ai-en-oci)
8. [Diseño de Preguntas](#-diseño-de-preguntas-y-mejora-continua)
9. [Estrategias de Estudio](#-estrategias-de-estudio-sugeridas)
10. [Mapa de Preguntas](#-mapa-de-preguntas-por-tema)
11. [Extensiones Futuras](#-próximas-extensiones)
12. [Referencias Sugeridas](#-referencias-sugeridas)
13. [Glosario](#-glosario-rápido)
14. [Checklist Calidad](#-checklist-de-calidad-para-nuevas-preguntas)
15. [Conclusión](#-conclusión)

---
## 🚀 Resumen Ejecutivo

| Área | Idea Clave | Ejemplo | Por qué Importa |
|------|------------|---------|-----------------|
| IA | Simula procesos cognitivos | Asistente virtual | Cubre dominio general del examen |
| ML | Aprende patrones de datos | Clasificador de spam | Núcleo de varias preguntas |
| DL | Redes profundas especializadas | CNN en visión | Potencia tareas complejas |
| Generative AI | Crea nuevo contenido | LLM redactando texto | Nuevo foco en fundamentos |
| Servicios OCI AI | APIs pre-entrenadas | Vision / Language / Speech | Facilitan integración rápida |

### � Profundización Rápida Servicios de IA (Resumen Ampliado)
| Servicio | Entrada principal | Salidas clave | Capacidades destacadas | Limitaciones típicas | Ejemplos examen |
|----------|------------------|---------------|------------------------|---------------------|------------------|
| Vision | Imagen / Documento (PDF, JPG, PNG) | Labels, bounding boxes, texto OCR, pares clave-valor | Clasificación documento, OCR, Detección objetos, Extracción campos | Calidad imagen / formato soportado, iluminación, tamaño máx | Factura → merchant/date/amount (key-value), Vehículos y matrículas (object detection) |
| Document Understanding | Documento estructurado / escaneado | Texto + estructura (tablas, tipo doc) | OCR + segmentación + clasificación tipológica | No transcribe audio, depende legibilidad | Diferenciar recibo vs currículo |
| Language | Texto | Categorías, sentimiento, NER, idioma | Multi‑idioma, ampliación categorías | Ambigüedad semántica, sarcasmo | Clasificar noticias (Politics/Tech/Sports) |
| Speech | Audio | Transcript, puntuación confianza, marcas tiempo, SRT | Soporte formatos, filtrado lenguaje (tagging/masking/removing), normalización | Ruido de fondo, acentos extremos | Transcripción y normalización números |
| Vector Search (DB 23ai) | Texto / Embeddings | IDs similares, puntuación similitud | Búsqueda semántica integrada en SQL con ONNX | Necesita embeddings consistentes | Consultas semánticas vs keyword |
| Generative AI | Prompt (texto) | Texto generado, embeddings, fine-tuning parcial | T-Few, in-context, respuestas multi-turn | Riesgo alucinaciones, coste tokens | Diferencia pretraining vs supervisado |

### 🔍 Matriz de Tareas Vision
| Tarea | Descripción | ¿Servicio Vision? | Output típico | Ejemplo de uso |
|-------|-------------|------------------|--------------|-----------------|
| Clasificación de Imágenes | Asigna etiqueta global | Sí | Label + score | Distinguir factura vs recibo |
| Clasificación de Documentos | Tipo documental | Sí | Document type | Identificar factura, currículum, contrato |
| OCR | Extraer texto crudo | Sí | Texto + posiciones | Extraer número de factura |
| Key-Value Extraction | Campos estructurados (merchant, total) | Sí | Pares (campo, valor, confianza) | Automatizar contabilidad |
| Object Detection | Localizar múltiples objetos | Sí | Lista (label, bbox, score) | Vehículos y matrículas en parking |
| Face Recognition | Identificar rostros específicos | No directo (requiere modelo custom) | Embeddings / labels | Control de acceso (custom) |
| Table Extraction | Reconstruir tabla estructurada | Parcial (mejor en Document Understanding) | Celdas + contenido | Importar tabla de inventario |

### 🧪 Flujo Combinado Ejemplo (Factura → Base de Datos)
| Paso | Servicio | Acción | Resultado | Valor |
|------|----------|--------|----------|-------|
| 1 | Object Storage | Almacenar PDF factura | Archivo accesible | Persistencia |
| 2 | Vision (Document Classification) | Determinar tipo factura | Tipo=Invoice | Ruteo correcto |
| 3 | Vision (OCR + Key-Value) | Extraer texto y campos | merchant, date, amount | Automatiza captura |
| 4 | Document Understanding | Extraer tabla de líneas | Items + precios | Detalle granular |
| 5 | Generative AI (resumen) | Generar resumen contable | Texto estructurado | Auditoría rápida |
| 6 | DB 23ai Vector Search | Indexar descripción ítems | Embeddings + índice | Búsquedas semánticas futuras |
| 7 | Dashboard / Reporting | Visualizar métricas | KPIs gastos | Decisión financiera |

### ⚙️ Métricas Relevantes por Tipo
| Tipo Modelo | Métrica Clave | Complementarias | Riesgo típico |
|-------------|--------------|-----------------|--------------|
| Clasificación (Vision/Language) | Accuracy / F1 | Precision, Recall | Desbalance clases |
| Detección Objetos | mAP (IoU thresholds) | Recall por clase | Occlusión / escala |
| OCR / Extracción Campos | Exactitud campo | Confianza agregada | Texto borroso |
| Speech | Word Error Rate (WER) | Char Error Rate, Latencia | Ruido ambiente |
| Generative | Coherencia semántica | Perplexity, BLEU/ROUGE | Alucinación |
| Vector Search | Similaridad (coseno) | Latencia consulta | Embeddings inconsistentes |

> Nota: Las métricas exactas de la plataforma pueden presentarse como puntuaciones de confianza; el examen tiende a evaluar comprensión conceptual (qué métrica se aplica y por qué) más que fórmulas avanzadas.

### �📂 Servicios Principales
| Servicio | Función | Ejemplos Funcionales | Preguntas Relacionadas |
|----------|--------|----------------------|------------------------|
| Vision 🖼️ | Imagen/Documento | OCR, key-value, detección | Q9, Q14, Q32, Q33, Q38 |
| Language 🗣️ | NLP | Sentimiento, clasificación, NER | Q35 |
| Speech 🎙️ | Voz a texto | Transcripción, SRT, confianza | Q12, Q13, Q17, Q19 |
| Document Understanding 📄 | Extraer estructura | Tipo doc, tablas, pares | Complementario |
| Data Science 🧪 | Ciclo ML | Notebook, catálogo, despliegue | Q5, varios |
| Generative AI ✨ | LLM y PEFT | Prompting, T-Few | Q10, Q15, Q22–Q30 |
| Vector Search 🔍 | Semántica | Embeddings + ONNX | Q22, Q23, Q37 |

---

---
## 📊 Distribución Teórica (Estimada)

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

## 🎯 Objetivo
Explicar el contenido base que originó el banco de preguntas y proporcionar una guía conceptual extendida para reforzar y mejorar la calidad de futuras preguntas del examen OCI Foundations con énfasis en servicios de IA y conceptos de Machine Learning.

## 🌐 Panorama General de OCI
Oracle Cloud Infrastructure (OCI) ofrece servicios para cómputo, almacenamiento, networking y plataformas especializadas (Data Science, AI Services, Database 23ai). El examen Foundations cubre:
- Principios de la nube (IaaS, PaaS, SaaS)
- Arquitectura de OCI (regiones, dominios de disponibilidad, dominios de fallas)
- Identidad y seguridad (IAM, políticas, compartimentos, cifrado)
- Servicios base: Compute, Object Storage, Block Storage, VCN, Load Balancer, Autonomous Database
- Facturación y soporte (modelos de precio, SLA, niveles de soporte)

## 🛠️ Servicios de IA en OCI
### 🧪 OCI Data Science
Entorno administrado para:
- Notebook Sessions: Desarrollo interactivo (Python, ADS SDK).
- Model Training: Entrenamiento de modelos tradicionales y deep learning.
- Model Catalog: Versionar, registrar, gobernar modelos.
- Model Deployment: Exponer endpoints de inferencia gestionados.
- Integration: Conda packs, GPUs (en formas disponibles), logging y monitoreo.

### 🧩 OCI AI Services
Servicios pre-entrenados listos para integración mediante API/SDK:
- Vision: Clasificación de imágenes y documentos, OCR, extracción clave-valor, detección de objetos.
- Language: Clasificación de texto (gran conjunto de categorías), sentimiento, detección de idioma, NER.
- Speech: Transcripción de audio, normalización, puntuación de confianza, soporte SRT, filtrado de lenguaje (tagging/masking/removing).
- Anomaly Detection (no detallado en preguntas oficiales): Identificación de patrones anómalos en series temporales.
- Generative AI: Modelos LLM para prompting, few-shot y fine-tuning eficiente (T-Few).

### 🗄️ Oracle Database 23ai y Vector Search
- Integración de embeddings directamente en la base de datos.
- Carga de modelos ONNX para generar representaciones vectoriales.
- Consultas semánticas mezclando SQL y búsqueda vectorial.
- Reducción de latencia al evitar extracción masiva de datos.

## 🧠 Conceptos Clave de ML/DL
| Concepto | Definición | Relación Preguntas | Emoji |
|----------|------------|--------------------|-------|
| Overfitting | Memoriza entrenamiento, falla en test | Q4 | 🔁 |
| Inference | Uso del modelo para nuevos datos | Q21 | 📤 |
| Regression | Predicción continua | Q6 | 📈 |
| Classification | Predicción de etiquetas discretas | Q35, Q39 | 🏷️ |
| RNN | Manejo de secuencias temporales | Q18, Q29, Q36 | 🔄 |
| CNN | Patrones espaciales en imágenes | Q33, Q38 | 🖼️ |
| Tokens | Unidades mínimas de texto | Q28 | ✂️ |
| Few-Shot | Ejemplos cortos en prompt | Q27 | 🎯 |
| In-Context Learning | Adaptación sin cambiar pesos | Opcional O106 | 🧩 |
| T-Few (PEFT) | Fine-tuning eficiente parcial | Q10 | ⚙️ |
| Vanishing Gradient | Gradiente se atenúa en secuencias largas | Q36 | 🥀 |
| Loss Function | Mide error para optimizar | Q41 | 📉 |

## 🛡️ Trustworthy AI
Principios: Lawful, Ethical, Robust.
- Lawful: Cumplimiento regulatorio (privacidad, protección de datos).
- Ethical: Minimizar sesgos, transparencia, uso responsable.
- Robust: Fiabilidad técnica y resistencia a ataques adversarios.
Aplicación práctica: Monitoreo post-despliegue, auditorías de modelos, filtrado de contenido.

## ⚙️ Infraestructura para AI en OCI
### 🏗️ Superclusters
- Conjuntos de nodos GPU de alta densidad.
- Red RDMA para baja latencia y alto ancho de banda.
- Escalabilidad para entrenamiento de LLM y modelos de visión a gran escala.

### 🧲 GPUs Disponibles
- A100: Escala pequeña-mediana (equilibrio rendimiento/memoria).
- GB200: Escenarios masivos (Grace Blackwell, exascala, HPC extremo).
- H100/H200: Generaciones avanzadas (no directamente preguntadas, pero relevantes en comparación).

### 🚫 Componentes NO de AI Compute
- OCI Vault: Gestión de llaves y secretos (seguridad), no cómputo de IA.

## 🧪 Diseño de Preguntas y Mejora Continua
Para mejorar la calidad de las preguntas:
1. Evitar duplicados semánticos salvo que refuercen (ej: Select AI repetido -> fusionar en una pregunta multi-parte).
2. Incluir distractores plausibles (opciones incorrectas que representen errores comunes reales).
3. Añadir contexto breve (escenario de negocio) para aumentar aplicabilidad.
4. Balancear taxonomía cognitiva (recordar, comprender, aplicar, analizar).
5. Revisar conclusiones contra documentación oficial para evitar ambigüedades.

### 🔧 Ejemplo de Mejora
Pregunta original: "GPU para massive-scale?" -> Añadir contexto: "Entrenar un LLM multilingüe de cientos de miles de millones de parámetros" para reforzar la elección de GB200.

### ⚠️ Errores Comunes a Vigilar
- Confundir OCR con Document Classification.
- Usar 'in-context learning' como sinónimo de fine-tuning (son distintos).
- Considerar que Vector Search hace coincidencia exacta de palabras (usa similitud semántica).
- Asumir que cualquier capa oculta 'produce la salida final'.

## 📚 Estrategias de Estudio Sugeridas
- Bloques tematizados (Vision, Speech, Language, Infra, Prompting).
- Prácticas espaciadas: repetir cada bloque 24h después.
- Técnica de Enseñar: Explicar cada concepto a otra persona o grabar un audio explicativo.
- Registro de Fallos: Usar `last_wrong.json` (quiz) para enfocarse en debilidades.

## 🗺️ Mapa de Preguntas por Tema
| Tema | Preguntas Oficiales | Opcionales | Icono |
|------|---------------------|-----------|-------|
| Vision | Q9, Q14, Q32, Q33, Q38 | O103 | 🖼️ |
| Speech | Q12, Q13, Q17, Q19 | O107 | 🎙️ |
| Language | Q35 | O101, O109 | 🗣️ |
| Generative / LLM | Q10, Q15, Q22, Q23, Q27–Q30, Q41 | O104, O106 | ✨ |
| Infra / GPUs | Q24–Q26 | O105 | 🧲 |
| Core ML | Q3, Q4, Q6, Q21, Q31, Q34, Q36, Q39, Q40 | O102 | 🔧 |
| Database / Vector | Q22, Q23, Q37 | O108 | 🔍 |
| Trustworthy AI | Q20 | - | 🛡️ |

## 🔮 Próximas Extensiones
- Añadir sección de preguntas de desarrollo seguro y compliance.
- Incorporar ejemplos de prompts optimizados (zero-shot vs few-shot vs chain-of-thought).
- Añadir métricas de evaluación: precisión, recall, F1 (no incluidas aún).
- Explorar casos de uso multi-servicio (Vision + Language + DB 23ai).

## 📎 Referencias Sugeridas
(No se incluyen URLs directas para evitar dependencia; buscar en documentación oficial OCI):
- OCI Data Science Documentation
- OCI AI Services Overview
- Oracle Database 23ai Vector Search Guide
- Trustworthy AI Principles (Oracle / Industria)

## 🧾 Glosario Rápido
| Término | Definición Breve | Emoji |
|---------|------------------|-------|
| Embedding | Vector semántico denso de texto/imagen | 🔗 |
| Token | Unidad mínima de entrada LLM | ✂️ |
| Endpoint de Inferencia | API que expone predicciones | 🚀 |
| OCR | Extracción de texto en imágenes | 🔍 |
| Key-Value Extraction | Pares estructurados (doc) | 🧾 |
| Few-Shot | Pocos ejemplos en prompt | 🎯 |
| In-Context Learning | Adaptación sin reentrenar | 🧩 |
| Vanishing Gradient | Gradiente que se extingue | 🥀 |
| T-Few | Fine-tuning eficiente | ⚙️ |
| RDMA | Red de baja latencia | 🚄 |
| Loss Function | Mide error optimización | 📉 |

## ✅ Checklist de Calidad para Nuevas Preguntas
Antes de agregar una nueva pregunta:
1. ¿El distractor más plausible refleja un error conceptual común?
2. ¿La respuesta es inequívoca con base en documentación oficial?
3. ¿El escenario aporta aplicación práctica (si corresponde)?
4. ¿Evita ambigüedad terminológica (OCR vs Clasificación Documentos)?
5. ¿No duplica innecesariamente otra pregunta sin variar el ángulo cognitivo?

## 🏁 Conclusión
Este documento extiende el material inicial proporcionando una base teórica estructurada y criterios de mejora continua para el banco de preguntas. Úsalo junto con el `quiz.py` para un ciclo de aprendizaje activo: leer -> probar -> analizar fallos -> reforzar.

---
Fin de documentación.

---
## 📦 Nuevas Preguntas Propuestas (Generadas Originalmente)
Estas NO provienen de fuentes externas copiadas; se diseñan para ampliar cobertura conceptual.

1. Vision Key-Value Extraction – ¿Cuál es la principal ventaja frente a solo OCR?
	A. Reduce tamaño de archivo
	B. Elimina necesidad de indexar
	C. Proporciona estructura semántica con campos específicos ✅
	D. Convierte imágenes en audio
	Explicación: OCR da texto plano; key-value añade pares semánticos listos para bases de datos.

2. Document Understanding vs Vision – ¿Cuándo preferir Document Understanding para tablas?
	A. Cuando se requieren bounding boxes de objetos pequeños
	B. Cuando la prioridad es texto continuo sin estructura
	C. Cuando se necesita reconstruir celdas y encabezados coherentes ✅
	D. Cuando se traducen idiomas en línea
	Explicación: Document Understanding encapsula estructura tabular mejor que OCR puro.

3. Speech Normalization – ¿Qué transforma 12/10/2025 y “www.example.com” en formato estándar?
	A. Confidence scoring
	B. Profanity tagging
	C. Normalization ✅
	D. SRT alignment
	Explicación: Normalization estandariza números, fechas, URLs para lectura uniforme.

4. Vector Search – ¿Qué sucede si dos documentos comparten sinónimos pero pocas palabras exactas?
	A. No se pueden encontrar
	B. Búsqueda semántica aún los asocia por embeddings ✅
	C. Requiere stemming manual
	D. Solo coincide si hay mismo número de tokens
	Explicación: Embeddings capturan significado más allá de coincidencia literal.

5. Generative AI Seguridad – ¿Cuál es una mitigación ante prompt injection?
	A. Aumentar batch size
	B. Sanitizar y delimitar contenido del usuario ✅
	C. Usar más GPUs
	D. Reducir tokens
	Explicación: Delimitadores y limpieza previenen ejecución de instrucciones maliciosas.

6. Vision Object Detection – Métrica adecuada para evaluar superposición entre predicción y verdad:
	A. Perplexity
	B. Intersection over Union (IoU) ✅
	C. Word Error Rate
	D. Cosine similarity pura
	Explicación: IoU mide calidad de bounding box; se agrega en mAP.

7. Speech – ¿Por qué incluir SRT export en pipeline de transcripción?
	A. Reduce consumo GPU
	B. Facilita subtitulado sincronizado en video ✅
	C. Mejora privacidad
	D. Deshabilita tagging
	Explicación: SRT estándar facilita integración multimedia.

8. Trustworthy AI – ¿Ejemplo práctico de Robust?
	A. Modelo ignora auditorías
	B. Sistema incluye pruebas adversariales para inputs manipulados ✅
	C. Elimina logs
	D. Expone contraseñas para depurar
	Explicación: Robustez implica resistencia frente a ataques o ruido.

9. GPUs – ¿Por qué elegir A100 en fase experimental en vez de GB200?
	A. Mayor exascala necesaria
	B. Coste y escala ajustados a pruebas medianas ✅
	C. A100 no soporta entrenamiento
	D. GB200 menor latencia siempre
	Explicación: A100 balance costo/rendimiento para iteración antes de escalar.

10. Embeddings – ¿Qué pasa si se mezclan embeddings generados con distintos modelos en mismo índice Vector Search?
	 A. Mejora precisión
	 B. Degrada coherencia semántica y similitud ✅
	 C. Acelera consultas
	 D. Obliga a usar labeled data
	 Explicación: Embeddings inconsistentes producen distancias no comparables.

> Puedes integrar estas propuestas al banco opcional marcándolas con nuevos IDs (O110+), manteniendo trazabilidad.

---
## ⚖️ Nota sobre Fuentes Externas
Se han referenciado públicamente enlaces (Scribd, repositorio GitHub) pero NO se copia texto directo para evitar infringir derechos. El contenido aquí es síntesis original basada en conocimiento general de OCI y prácticas comunes de examen de fundamentos.

