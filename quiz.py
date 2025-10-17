import random
import textwrap

# Banco de preguntas oficiales (Q1–Q40). Estructura: dict con 'question', 'options', 'answer', 'explanation'
QUESTIONS_OFFICIAL = [
    {
        "id": 1,
    QUESTIONS_OPTIONAL = [
        {"id": 101, "question": "AI domain for sentiment analysis & translation?", "options": ["Computer Vision", "Speech Processing", "Natural Language Processing", "Anomaly Detection"], "answer": 2, "explanation": "NLP cubre análisis de sentimiento y traducción."},
        {"id": 102, "question": "Model training primarily involves?", "options": ["Writing full program code", "Establishing input-output parameter relationships", "Deploying the model", "Running inference"], "answer": 1, "explanation": "Ajustar parámetros para mapear entradas a salidas."},
        {"id": 103, "question": "Primary purpose of CNNs?", "options": ["Process sequential data", "Detect patterns in images", "Generate music", "Store labels"], "answer": 1, "explanation": "Extraen características espaciales en imágenes."},
        {"id": 104, "question": "Generative AI differs from supervised by?", "options": ["Only classification tasks", "Modeling data distribution to create new samples", "Requires labeled pairs only", "No training stage"], "answer": 1, "explanation": "Genera ejemplos nuevos aprendiendo la distribución."},
        {"id": 105, "question": "Advantage of OCI Superclusters?", "options": ["Integrate social media", "High performance for complex AI workloads", "Cheaper than all services", "Only for simple scripts"], "answer": 1, "explanation": "Escalabilidad GPU y red rápida para entrenamiento masivo."},
        {"id": 106, "question": "In-context learning means?", "options": ["Permanent weight changes", "Provide examples in the prompt", "Zero-shot classification", "Manual feature engineering"], "answer": 1, "explanation": "Ejemplos en el prompt sin ajuste de pesos."},
        {"id": 107, "question": "OCI Speech service offers?", "options": ["Transcribe speech to text", "Classify documents", "Generate images", "Detect faces"], "answer": 0, "explanation": "Convierte audio en texto."},
        {"id": 108, "question": "OCI Document Understanding cannot?", "options": ["Generate audio transcript", "Extract tables", "Classify documents", "Extract text"], "answer": 0, "explanation": "No transcribe audio; hace OCR, clasificación y extracción."},
        {"id": 109, "question": "Interactive coding environment in OCI Data Science?", "options": ["Model Catalog", "Conda Pack", "Notebook Sessions", "ADS Jobs"], "answer": 2, "explanation": "Notebook Sessions brindan entorno gestionado interactivo."},
    ]
        "question": "Deep Learning - Key feature of RNNs?",
        "options": ["Parallel processing", "Used for images", "Feedback loop retains info across time steps", "No internal state"],
        "answer": 2,
        "explanation": "RNN conserva estado histórico para secuencias."},
    {
        "id": 2,
        "question": "Oracle AI Vector Search primary use?",
        "options": ["Store business data", "Manage security", "Keyword queries", "Semantic queries"],
        "answer": 3,
        "explanation": "Comparación de embeddings para significado semántico."},
    {
        "id": 3,
        "question": "What is overfitting?",
        "options": ["Model too simple", "Model memorizes training data and fails to generalize", "Model ignores input", "No output"],
        "answer": 1,
        "explanation": "Pierde capacidad de generalización al memorizar datos."},
    {
        "id": 4,
        "question": "Non-parametric supervised algorithm?",
        "options": ["Linear Regression", "K-Nearest Neighbors (KNN)", "Random Forest", "Decision Trees"],
        "answer": 1,
        "explanation": "KNN usa distancias sin entrenar parámetros internos."},
    {
        "id": 5,
        "question": "Purpose of Model Catalog?",
        "options": ["Store raw datasets", "Deploy endpoints", "Real-time engine", "Repository to store, track, manage ML models"],
        "answer": 3,
        "explanation": "Gestiona versiones y metadatos de modelos."},
    {
        "id": 6,
        "question": "Technique to predict house price?",
        "options": ["Regression", "Time Series Analysis", "Classification", "Clustering"],
        "answer": 0,
        "explanation": "Variable continua -> regresión."},
    {
        "id": 7,
        "question": "OCI service to deploy trained model for real-time predictions?",
        "options": ["Object Storage", "OCI Language", "OCI Data Science", "OCI Speech"],
        "answer": 2,
        "explanation": "Data Science ofrece endpoints de inferencia."},
    {
        "id": 8,
        "question": "NOT an unsupervised ML application?",
        "options": ["Spam detection", "Outlier detection", "Targeted marketing", "Customer segmentation"],
        "answer": 0,
        "explanation": "Spam es clasificación supervisada."},
    {
        "id": 9,
        "question": "Vision feature to identify invoice/receipt/resume?",
        "options": ["Table extraction", "Image classification", "Document classification", "OCR"],
        "answer": 2,
        "explanation": "Clasifica documentos por estructura y contenido."},
    {
        "id": 10,
        "question": "T-Few fine-tuning reduces cost because it...",
        "options": ["Manually config layers", "Trains entire model from scratch", "Selectively updates fraction of weights", "No customization"],
        "answer": 2,
        "explanation": "Actualiza pocos parámetros (efficient)."},
    {
        "id": 11,
        "question": "Data type suited for deep learning?",
        "options": ["Human-interpretable simple", "Complex non-human interpretable", "Only time series", "Only strings"],
        "answer": 1,
        "explanation": "Imágenes/audio/video presentan características complejas."},
    {
        "id": 12,
        "question": "Normalization in Speech does?",
        "options": ["Translates languages", "Lowercases all", "Standardizes numbers/dates/URLs", "Removes filler words"],
        "answer": 2,
        "explanation": "Uniformiza formatos para legibilidad."},
    {
        "id": 13,
        "question": "Profanity option to retain words and mark them?",
        "options": ["Tagging", "Removing", "Normalization", "Masking"],
        "answer": 0,
        "explanation": "Tagging conserva texto y etiqueta."},
    {
        "id": 14,
        "question": "Vision feature to extract merchant/date/amount?",
        "options": ["OCR", "Document classification", "Key-value extraction", "Table extraction"],
        "answer": 2,
        "explanation": "Extrae pares clave:valor."},
    {
        "id": 15,
        "question": "Difference LLM vs traditional ML?",
        "options": ["LLM pretraining on large corpus", "LLM fewer params", "Traditional ML better at language", "LLM needs heavy feature engineering"],
        "answer": 0,
        "explanation": "LLM se preentrena en gran corpus genérico."},
    {
        "id": 16,
        "question": "Concept applied in self-driving car scenario?",
        "options": ["Artificial Intelligence", "Deep Learning", "NLP", "Optimization"],
        "answer": 0,
        "explanation": "Integra percepción, decisión, planeación."},
    {
        "id": 17,
        "question": "Speech feature for per-word certainty?",
        "options": ["Confidence scoring", "Normalization", "Batch support", "Masking"],
        "answer": 0,
        "explanation": "Proporciona puntuación de confianza."},
    {
        "id": 18,
        "question": "NN best for generating music sequences?",
        "options": ["FNN", "RNN", "CNN", "Autoencoder"],
        "answer": 1,
        "explanation": "Secuencias -> RNN (o variantes)."},
    {
        "id": 19,
        "question": "Speech feature to add closed captions?",
        "options": ["Profanity filtering", "SRT file support", "Confidence scoring", "Batching"],
        "answer": 1,
        "explanation": "Genera subtítulos estándar."},
    {
        "id": 20,
        "question": "Guiding principles for trustworthy AI?",
        "options": ["Lawful, ethical, robust", "Fast, unbiased, autonomous", "Cheap, scalable, easy", "Independent, self-learning, fast"],
        "answer": 0,
        "explanation": "Marco de confianza: legal, ética, robusta."},
    {
        "id": 21,
        "question": "Primary function of inference in ML?",
        "options": ["Label training data", "Predict new data outcomes", "Adjust weights", "Collect datasets"],
        "answer": 1,
        "explanation": "Generar predicciones en datos nuevos."},
    {
        "id": 22,
        "question": "How does Select AI generate SQL?",
        "options": ["Uses templates", "Needs manual params", "Connects to LLM infers intent", "Only works predefined SQL"],
        "answer": 2,
        "explanation": "Mapea NL a SQL mediante LLM."},
    {
        "id": 23,
        "question": "Select AI enhances interaction with Autonomous DB by?",
        "options": ["Improving network security", "Natural language prompts instead of SQL", "Removing need for DBAs", "Adding visualization"],
        "answer": 1,
        "explanation": "Permite prompts en lenguaje natural."},
    {
        "id": 24,
        "question": "NOT part of OCI AI Infrastructure?",
        "options": ["OCI Storage", "RDMA Network", "NVIDIA GPUs", "OCI Vault"],
        "answer": 3,
        "explanation": "Vault gestiona llaves, no cómputo AI."},
    {
        "id": 25,
        "question": "GPU for massive-scale HPC AI workloads?",
        "options": ["H100", "GB200", "A10", "A100"],
        "answer": 1,
        "explanation": "Grace Blackwell para exascala."},
    {
        "id": 26,
        "question": "GPU for small/medium scale training/inference?",
        "options": ["GB200", "H200", "A100", "A10"],
        "answer": 2,
        "explanation": "A100 balance rendimiento/memoria."},
    {
        "id": 27,
        "question": "Prompt technique giving explicit examples?",
        "options": ["Chain-of-thought", "Zero-shot", "Few-shot", "Self-supervised"],
        "answer": 2,
        "explanation": "Ejemplos en prompt para guía."},
    {
        "id": 28,
        "question": "Role of tokens in LLMs?",
        "options": ["Define architecture", "Represent model params", "Determine memory size", "Minimal text units processed"],
        "answer": 3,
        "explanation": "Segmentación a unidades básicas."},
    {
        "id": 29,
        "question": "Model to complete poem lines?",
        "options": ["GAN", "RNN", "CNN", "VAE"],
        "answer": 1,
        "explanation": "Secuencias lingüísticas -> RNN."},
    {
        "id": 30,
        "question": "Generative AI pretraining does?",
        "options": ["Requires RLHF only", "Memorizes exact examples", "Needs labeled mapping", "Learns patterns w/o labeled data"],
        "answer": 3,
        "explanation": "Auto-supervisión sobre corpora grandes."},
    {
        "id": 31,
        "question": "Purpose of hidden layer in ANN?",
        "options": ["Pass data only", "Final outputs", "Apply filters to images", "Transform inputs via weights & activations"],
        "answer": 3,
        "explanation": "Representaciones internas no lineales."},
    {
        "id": 32,
        "question": "Feature to label vehicles & plates?",
        "options": ["Image classification", "Object detection", "Speech-to-text", "Document classification"],
        "answer": 1,
        "explanation": "Bounding boxes sobre objetos múltiples."},
    {
        "id": 33,
        "question": "AI subset for image classification?",
        "options": ["Reinforcement Learning", "Machine Learning", "Deep Learning", "NLP"],
        "answer": 2,
        "explanation": "CNN y modelos profundos predominan."},
    {
        "id": 34,
        "question": "Role of target variable?",
        "options": ["Feature selection", "Input data", "Split dataset", "Desired output labels"],
        "answer": 3,
        "explanation": "Ground truth para calcular pérdida."},
    {
        "id": 35,
        "question": "Feature to categorize news articles?",
        "options": ["Language detection", "Text classification", "Sentiment analysis", "NER"],
        "answer": 1,
        "explanation": "Clasifica en categorías temáticas."},
    {
        "id": 36,
        "question": "Limitation of RNNs on long sequences?",
        "options": ["Process only numbers", "Vanishing gradient long dependencies", "Parallel word processing inefficiency", "Only first words understood"],
        "answer": 1,
        "explanation": "Gradiente se atenúa en secuencias largas."},
    {
        "id": 37,
        "question": "DB 23ai uses pretrained models for vector search by?",
        "options": ["Restricting to Oracle APIs", "Storing raw images", "Manual SQL conversion", "Loading ONNX models directly"],
        "answer": 3,
        "explanation": "Se cargan ONNX y generan embeddings."},
    {
        "id": 38,
        "question": "Network best for face recognition?",
        "options": ["Autoencoder", "CNN", "FNN", "RNN"],
        "answer": 1,
        "explanation": "CNN extrae rasgos espaciales."},
    {
        "id": 39,
        "question": "Technique for spam filtering?",
        "options": ["Reinforcement Learning", "NLP", "Deep Learning", "Machine Learning"],
        "answer": 3,
        "explanation": "Clasificación supervisada ML."},
    {
        "id": 40,
        "question": "Data type predicting stock prices?",
        "options": ["Sequential", "Text", "Time series", "Image"],
        "answer": 2,
        "explanation": "Serie temporal indexada por tiempo."},
]

LETTER_MAP = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
REV_LETTER_MAP = {v: k for k, v in LETTER_MAP.items()}


def format_question(q):
    wrapped = textwrap.fill(q['question'], width=80)
    lines = [f"Q{q['id']}: {wrapped}"]
    for idx, opt in enumerate(q['options']):
        letter = LETTER_MAP[idx]
        lines.append(f"  {letter}. {opt}")
    return "\n".join(lines)


def ask_question(q):
    print(format_question(q))
    while True:
        user = input("Tu respuesta (A-D, 'x' para ver explicación y saltar): ").strip().upper()
        if user == 'X':
            print(f"Explicación: {q['explanation']} (Respuesta correcta: {LETTER_MAP[q['answer']]})\n")
            return False
        if user in REV_LETTER_MAP:
            chosen = REV_LETTER_MAP[user]
            correct = (chosen == q['answer'])
            if correct:
                print("✔ Correcto\n")
    def choose_bank():
        print("Selecciona banco de preguntas:")
        print("  1. Oficiales (40)")
        print("  2. Opcionales (9)")
        print("  3. Ambas (49)")
        while True:
            c = input("Opción (1/2/3): ").strip()
            if c == '1':
                return QUESTIONS_OFFICIAL[:]
            if c == '2':
                return QUESTIONS_OPTIONAL[:]
            if c == '3':
                return QUESTIONS_OFFICIAL[:] + QUESTIONS_OPTIONAL[:]
            print("Entrada inválida. Usa 1, 2 o 3.")

            else:
                print(f"✘ Incorrecto. Correcta: {LETTER_MAP[q['answer']]}\nExplicación: {q['explanation']}\n")
            return correct
        else:
            print("Entrada inválida. Usa A, B, C, D o X.")


def run_quiz(mode='random'):
    if mode == 'sequential':
        order = QUESTIONS[:]
    else:
        order = QUESTIONS[:]
        random.shuffle(order)
    score = 0
    wrong = []
    for q in order:
        correct = ask_question(q)
        if correct:
            score += 1
        else:
            wrong.append(q)
    print(f"Resultado: {score}/{len(order)} correctas ({score/len(order)*100:.1f}%).")
    if wrong:
        print("Preguntas falladas:
")
        for q in wrong:
            print(f"  Q{q['id']} -> {q['question']} (Correcta: {LETTER_MAP[q['answer']]})")
    else:
        print("¡Excelente! Sin errores.")
    def review_wrong_only(bank=None):

def review_wrong_only():
    # Modo para repasar solo fallos previos guardados en archivo temporal
    try:
        import json, os
        if not os.path.exists('last_wrong.json'):
            print("No hay registro de errores previos.")
            return
            source = bank if bank is not None else (QUESTIONS_OFFICIAL + QUESTIONS_OPTIONAL)
            subset = [q for q in source if q['id'] in data.get('wrong_ids', [])]
            data = json.load(f)
        subset = [q for q in QUESTIONS if q['id'] in data.get('wrong_ids', [])]
        if not subset:
            print("No hay preguntas en la lista de fallos.")
            return
        print(f"Repasando {len(subset)} preguntas falladas previamente...\n")
        score = 0
        new_wrong = []
        for q in subset:
            correct = ask_question(q)
            if correct:
                score += 1
            else:
                new_wrong.append(q)
        print(f"Resultado: {score}/{len(subset)} correctas.")
        with open('last_wrong.json','w',encoding='utf-8') as f:
            json.dump({'wrong_ids':[q['id'] for q in new_wrong]}, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error en review_wrong_only: {e}")


def main():
    print("=== OCI Foundations AI Quiz ===")
    print("Modos disponibles:")
    print("  1. Aleatorio")
    print("  2. Secuencial")
    print("  3. Repasar solo últimas falladas")
    choice = input("Selecciona modo (1/2/3): ").strip()
    if choice == '3':
        review_wrong_only()
        return
    mode = 'random' if choice != '2' else 'sequential'
    order = QUESTIONS[:]
    if mode == 'random':
        random.shuffle(order)
    score = 0
    wrong = []
    for q in order:
        correct = ask_question(q)
        if correct:
            score += 1
        else:
            wrong.append(q)
    print(f"\nResultado final: {score}/{len(order)} correctas ({score/len(order)*100:.1f}%).")
    if wrong:
        print("Preguntas falladas:")
        for q in wrong:
            print(f"  Q{q['id']} -> {q['question']} (Correcta: {LETTER_MAP[q['answer']]})")
        # Guardar para repaso
        try:
            import json
            with open('last_wrong.json','w',encoding='utf-8') as f:
                json.dump({'wrong_ids':[q['id'] for q in wrong]}, f, ensure_ascii=False, indent=2)
            print("Lista de fallos guardada en last_wrong.json")
        except Exception as e:
            print(f"No se pudo guardar lista de fallos: {e}")
    else:
        print("¡Perfecto! Sin errores.")

if __name__ == '__main__':
    main()
