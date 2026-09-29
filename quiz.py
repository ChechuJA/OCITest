import random
import textwrap
import json
import os

"""CLI Quiz for OCI Foundations AI exam practice.

Features:
 - Official bank extended to 41 questions (Q41 added).
 - Optional bank (9 extra practice questions).
 - Dynamic selection of bank (official / optional / both).
 - Distinguish answer outcomes: correct, wrong, skipped, marked.
 - Controls:
     A-D  -> responder
     X    -> ver explicación y saltar (cuenta como skipped)
     S    -> saltar sin explicación (skipped)
     M    -> marcar para segunda ronda (no puntúa todavía)
 - Segunda ronda automática para las preguntas marcadas.
 - Persistencia de IDs incorrectos finales en last_wrong.json.
"""

# Banco de preguntas oficiales (Q1–Q41)
QUESTIONS_OFFICIAL = [
    {"id":1,"question":"Which algorithm is a non-parametric approach for supervised learning?","options":["Linear Regression","K-Nearest Neighbors (KNN)","Random Forest","Decision Trees"],"answer":1,"explanation":"KNN no aprende parámetros internos; almacena datos y usa distancias. Único hiperparámetro: K."},
    {"id":2,"question":"Deep Learning - Key feature of RNNs?","options":["Parallel processing","Used for images","Feedback loop retains info across time steps","No internal state"],"answer":2,"explanation":"Conexiones recurrentes mantienen estado temporal."},
    {"id":3,"question":"Oracle AI Vector Search primary use?","options":["Store business data","Manage security","Keyword queries","Semantic queries"],"answer":3,"explanation":"Búsqueda semántica mediante embeddings."},
    {"id":4,"question":"What is overfitting?","options":["Model too simple","Model memorizes training data and fails to generalize","Model ignores input","No output"],"answer":1,"explanation":"Memoriza entrenamiento y falla en generalizar."},
    {"id":5,"question":"Purpose of Model Catalog?","options":["Store raw datasets","Deploy endpoints","Real-time engine","Repository to store, track, manage ML models"],"answer":3,"explanation":"Versionado y gobernanza modelos."},
    {"id":6,"question":"Technique to predict house price?","options":["Regression","Time Series Analysis","Classification","Clustering"],"answer":0,"explanation":"Precio = variable continua."},
    {"id":7,"question":"OCI service to deploy trained model for real-time predictions?","options":["Object Storage","OCI Language","OCI Data Science","OCI Speech"],"answer":2,"explanation":"Data Science endpoints inferencia."},
    {"id":8,"question":"NOT an unsupervised ML application?","options":["Spam detection","Outlier detection","Targeted marketing","Customer segmentation"],"answer":0,"explanation":"Spam es supervisado."},
    {"id":9,"question":"Vision feature to identify invoice/receipt/resume?","options":["Table extraction","Image classification","Document classification","OCR"],"answer":2,"explanation":"Clasifica tipo documental."},
    {"id":10,"question":"T-Few fine-tuning reduces cost because it...","options":["Manually config layers","Trains entire model from scratch","Selectively updates fraction of weights","No customization"],"answer":2,"explanation":"Actualiza pocos parámetros."},
    {"id":11,"question":"Data type suited for deep learning?","options":["Human-interpretable simple","Complex non-human interpretable","Only time series","Only strings"],"answer":1,"explanation":"Datos complejos (imagen/audio)."},
    {"id":12,"question":"Normalization in Speech does?","options":["Translates languages","Lowercases all","Standardizes numbers/dates/URLs","Removes filler words"],"answer":2,"explanation":"Estandariza formatos."},
    {"id":13,"question":"Profanity option to retain words and mark them?","options":["Tagging","Removing","Normalization","Masking"],"answer":0,"explanation":"Etiqueta sin eliminar."},
    {"id":14,"question":"Vision feature to extract merchant/date/amount?","options":["OCR","Document classification","Key-value extraction","Table extraction"],"answer":2,"explanation":"Extrae pares clave:valor."},
    {"id":15,"question":"Difference LLM vs traditional ML?","options":["LLM pretraining on large corpus","LLM fewer params","Traditional ML better at language","LLM needs heavy feature engineering"],"answer":0,"explanation":"Preentrenado masivo multi-tarea."},
    {"id":16,"question":"Concept applied in self-driving car scenario?","options":["Artificial Intelligence","Deep Learning","NLP","Optimization"],"answer":0,"explanation":"Concepto amplio: AI."},
    {"id":17,"question":"Speech feature for per-word certainty?","options":["Confidence scoring","Normalization","Batch support","Masking"],"answer":0,"explanation":"Puntuación por palabra."},
    {"id":18,"question":"NN best for generating music sequences?","options":["FNN","RNN","CNN","Autoencoder"],"answer":1,"explanation":"Secuencias -> RNN."},
    {"id":19,"question":"Speech feature to add closed captions?","options":["Profanity filtering","SRT file support","Confidence scoring","Batching"],"answer":1,"explanation":"Archivos SRT."},
    {"id":20,"question":"Guiding principles for trustworthy AI?","options":["Lawful, ethical, robust","Fast, unbiased, autonomous","Cheap, scalable, easy","Independent, self-learning, fast"],"answer":0,"explanation":"Legal, ética y robusta."},
    {"id":21,"question":"Primary function of inference in ML?","options":["Label training data","Predict new data outcomes","Adjust weights","Collect datasets"],"answer":1,"explanation":"Predice nuevos casos."},
    {"id":22,"question":"How does Select AI generate SQL?","options":["Uses templates","Needs manual params","Connects to LLM infers intent","Only works predefined SQL"],"answer":2,"explanation":"Mapea NL a SQL."},
    {"id":23,"question":"Select AI enhances interaction with Autonomous DB by?","options":["Improving network security","Natural language prompts instead of SQL","Removing need for DBAs","Adding visualization"],"answer":1,"explanation":"Prompts en lenguaje natural."},
    {"id":24,"question":"NOT part of OCI AI Infrastructure?","options":["OCI Storage","RDMA Network","NVIDIA GPUs","OCI Vault"],"answer":3,"explanation":"Vault gestiona llaves."},
    {"id":25,"question":"GPU for massive-scale HPC AI workloads?","options":["H100","GB200","A10","A100"],"answer":1,"explanation":"Grace Blackwell exascala."},
    {"id":26,"question":"GPU for small/medium scale training/inference?","options":["GB200","H200","A100","A10"],"answer":2,"explanation":"A100 equilibrio rendimiento/memoria."},
    {"id":27,"question":"Prompt technique giving explicit examples?","options":["Chain-of-thought","Zero-shot","Few-shot","Self-supervised"],"answer":2,"explanation":"Ejemplos guían salida."},
    {"id":28,"question":"Role of tokens in LLMs?","options":["Define architecture","Represent model params","Determine memory size","Minimal text units processed"],"answer":3,"explanation":"Unidad mínima de texto."},
    {"id":29,"question":"Model to complete poem lines?","options":["GAN","RNN","CNN","VAE"],"answer":1,"explanation":"RNN maneja contexto secuencial."},
    {"id":30,"question":"Generative AI pretraining does?","options":["Requires RLHF only","Memorizes exact examples","Needs labeled mapping","Learns patterns w/o labeled data"],"answer":3,"explanation":"Auto-supervisión."},
    {"id":31,"question":"Purpose of hidden layer in ANN?","options":["Pass data only","Final outputs","Apply filters to images","Transform inputs via weights & activations"],"answer":3,"explanation":"Transformación no lineal interna."},
    {"id":32,"question":"Feature to label vehicles & plates?","options":["Image classification","Object detection","Speech-to-text","Document classification"],"answer":1,"explanation":"Object detection crea bounding boxes."},
    {"id":33,"question":"AI subset for image classification?","options":["Reinforcement Learning","Machine Learning","Deep Learning","NLP"],"answer":2,"explanation":"Deep Learning (CNN/ViT)."},
    {"id":34,"question":"Role of target variable?","options":["Feature selection","Input data","Split dataset","Desired output labels"],"answer":3,"explanation":"Ground truth para pérdida."},
    {"id":35,"question":"Feature to categorize news articles?","options":["Language detection","Text classification","Sentiment analysis","NER"],"answer":1,"explanation":"Clasificación temática."},
    {"id":36,"question":"Limitation of RNNs on long sequences?","options":["Process only numbers","Vanishing gradient long dependencies","Parallel word processing inefficiency","Only first words understood"],"answer":1,"explanation":"Vanishing gradient."},
    {"id":37,"question":"DB 23ai uses pretrained models for vector search by?","options":["Restricting to Oracle APIs","Storing raw images","Manual SQL conversion","Loading ONNX models directly"],"answer":3,"explanation":"Carga modelos ONNX."},
    {"id":38,"question":"Network best for face recognition?","options":["Autoencoder","CNN","FNN","RNN"],"answer":1,"explanation":"CNN rasgos espaciales."},
    {"id":39,"question":"Technique for spam filtering?","options":["Reinforcement Learning","NLP","Deep Learning","Machine Learning"],"answer":3,"explanation":"Clasificación supervisada ML."},
    {"id":40,"question":"Data type predicting stock prices?","options":["Sequential","Text","Time series","Image"],"answer":2,"explanation":"Serie temporal indexada."},
    {"id":41,"question":"Primary role of a loss function during training?","options":["Generate new samples","Measure prediction error to guide optimization","Increase dataset size","Store model weights"],"answer":1,"explanation":"La función de pérdida cuantifica el error entre predicción y verdad; el optimizador la minimiza ajustando pesos."},
]

# Preguntas opcionales
QUESTIONS_OPTIONAL = [
    {"id":101,"question":"Domain sentiment & translation?","options":["Computer Vision","Speech Processing","Natural Language Processing","Anomaly Detection"],"answer":2,"explanation":"NLP cubre ambas tareas."},
    {"id":102,"question":"Model training involves?","options":["Write full program","Relate inputs to outputs","Deploy endpoint","Run inference"],"answer":1,"explanation":"Ajuste parámetros entrada-salida."},
    {"id":103,"question":"Primary purpose CNN?","options":["Sequential data","Patterns in images","Music generation","Store labels"],"answer":1,"explanation":"Patrones espaciales."},
    {"id":104,"question":"Generative vs supervised?","options":["Only classification","Model data distribution create new","Needs labeled pairs","No training"],"answer":1,"explanation":"Genera ejemplos nuevos."},
    {"id":105,"question":"Advantage Superclusters?","options":["Social integration","High performance complex AI","Cheapest always","Only simple scripts"],"answer":1,"explanation":"Escalado GPU + RDMA."},
    {"id":106,"question":"In-context learning means?","options":["Weight change","Examples in prompt","Zero-shot","Manual features"],"answer":1,"explanation":"Ejemplos sin reentrenar."},
    {"id":107,"question":"OCI Speech offers?","options":["Transcribe speech","Classify docs","Generate images","Detect faces"],"answer":0,"explanation":"Audio -> texto."},
    {"id":108,"question":"Document Understanding cannot?","options":["Generate audio transcript","Extract tables","Classify documents","Extract text"],"answer":0,"explanation":"No transcribe audio."},
    {"id":109,"question":"Interactive coding environment?","options":["Model Catalog","Conda Pack","Notebook Sessions","ADS Jobs"],"answer":2,"explanation":"Sesiones de notebook."},
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
    prompt = "Tu respuesta (A-D | X explicación+skip | S skip | M marcar): "
    while True:
        user = input(prompt).strip().upper()
        if user == 'X':
            print(f"Explicación: {q['explanation']} (Correcta: {LETTER_MAP[q['answer']]})\n")
            return {'status': 'skipped'}
        if user == 'S':
            print("Saltada.\n")
            return {'status': 'skipped'}
        if user == 'M':
            print("Marcada para segunda ronda.\n")
            return {'status': 'marked'}
        if user in REV_LETTER_MAP:
            chosen = REV_LETTER_MAP[user]
            if chosen == q['answer']:
                print("✔ Correcto\n")
                return {'status': 'correct'}
            else:
                print(f"✘ Incorrecto. Correcta: {LETTER_MAP[q['answer']]}\nExplicación: {q['explanation']}\n")
                return {'status': 'wrong'}
        print("Entrada inválida. Opciones: A B C D X S M")

def choose_bank():
    print("Selecciona banco de preguntas:")
    print(f"  1. Oficiales ({len(QUESTIONS_OFFICIAL)})")
    print(f"  2. Opcionales ({len(QUESTIONS_OPTIONAL)})")
    print(f"  3. Ambas ({len(QUESTIONS_OFFICIAL)+len(QUESTIONS_OPTIONAL)})")
    while True:
        c = input("Opción (1/2/3): ").strip()
        if c == '1':
            return QUESTIONS_OFFICIAL[:]
        if c == '2':
            return QUESTIONS_OPTIONAL[:]
        if c == '3':
            return QUESTIONS_OFFICIAL[:] + QUESTIONS_OPTIONAL[:]
        print("Entrada inválida. Usa 1, 2 o 3.")

def review_wrong_only(bank=None):
    try:
        import json, os
        if not os.path.exists('last_wrong.json'):
            print("No hay registro de errores previos.")
            return
        with open('last_wrong.json','r',encoding='utf-8') as f:
            data = json.load(f)
        source = bank if bank is not None else (QUESTIONS_OFFICIAL + QUESTIONS_OPTIONAL)
        subset = [q for q in source if q['id'] in data.get('wrong_ids', [])]
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
            import json
            json.dump({'wrong_ids':[q['id'] for q in new_wrong]}, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error en review_wrong_only: {e}")

def run_quiz(mode='random', bank=None):
    if bank is None:
        bank = QUESTIONS_OFFICIAL[:]
    order = bank[:]
    if mode == 'random':
        random.shuffle(order)

    # Primera ronda
    results = []
    for q in order:
        res = ask_question(q)
        results.append((q, res['status']))

    # Segunda ronda para marcadas
    marked = [q for (q, st) in results if st == 'marked']
    if marked:
        print(f"\n=== Segunda ronda: {len(marked)} preguntas marcadas ===\n")
        second_pass = []
        for q in marked:
            res = ask_question(q)
            second_pass.append((q['id'], res['status']))
        updated = []
        for q, st in results:
            if st == 'marked':
                new_st = next((nst for qid, nst in second_pass if qid == q['id']), 'marked')
                updated.append((q, new_st))
            else:
                updated.append((q, st))
        results = updated

    total = len(results)
    correct = [q for q, st in results if st == 'correct']
    wrong = [q for q, st in results if st == 'wrong']
    skipped = [q for q, st in results if st == 'skipped']
    still_marked = [q for q, st in results if st == 'marked']
    pct = (len(correct) / total * 100) if total else 0.0
    print(f"\nResultado final: {len(correct)}/{total} correctas ({pct:.1f}%).")
    print(f"Incorrectas: {len(wrong)} | Skipped: {len(skipped)} | Marcadas sin responder: {len(still_marked)}")

    if wrong:
        print("\nPreguntas incorrectas:")
        for q in wrong:
            print(f"  Q{q['id']} -> {q['question']} (Correcta: {LETTER_MAP[q['answer']]})")
    if skipped:
        print("\nPreguntas saltadas:")
        for q in skipped:
            print(f"  Q{q['id']} -> {q['question']}")
    if still_marked:
        print("\nPreguntas marcadas no respondidas:")
        for q in still_marked:
            print(f"  Q{q['id']} -> {q['question']}")

    try:
        with open('last_wrong.json','w',encoding='utf-8') as f:
            json.dump({'wrong_ids':[q['id'] for q in wrong]}, f, ensure_ascii=False, indent=2)
        if wrong:
            print("Lista de fallos guardada en last_wrong.json")
    except Exception as e:
        print(f"No se pudo guardar lista de fallos: {e}")

def main():
    print("=== OCI Foundations AI Quiz ===")
    print("Controles: A-D responder | X explicación y saltar | S saltar | M marcar para segunda ronda")
    bank = choose_bank()
    print("Modos disponibles:")
    print("  1. Aleatorio")
    print("  2. Secuencial")
    print("  3. Repasar solo últimas falladas")
    choice = input("Selecciona modo (1/2/3): ").strip()
    if choice == '3':
        # repaso usa banco seleccionado para filtrar
        try:
            if not os.path.exists('last_wrong.json'):
                print("No hay registro de errores previos.")
                return
            with open('last_wrong.json','r',encoding='utf-8') as f:
                data = json.load(f)
            subset = [q for q in bank if q['id'] in data.get('wrong_ids', [])]
            if not subset:
                print("No hay preguntas en la lista de fallos para este banco.")
                return
            print(f"Repasando {len(subset)} preguntas falladas previamente...\n")
            final_wrong = []
            correct_count = 0
            for q in subset:
                res = ask_question(q)
                if res['status'] == 'correct':
                    correct_count += 1
                elif res['status'] == 'wrong':
                    final_wrong.append(q)
            print(f"Resultado: {correct_count}/{len(subset)} correctas.")
            with open('last_wrong.json','w',encoding='utf-8') as f:
                json.dump({'wrong_ids':[q['id'] for q in final_wrong]}, f, ensure_ascii=False, indent=2)
            if final_wrong:
                print("Lista de fallos actualizada en last_wrong.json")
        except Exception as e:
            print(f"Error en modo repaso: {e}")
        return
    mode = 'random' if choice != '2' else 'sequential'
    run_quiz(mode=mode, bank=bank)

if __name__ == '__main__':
    main()
    {
        "id": 2,
        if __name__ == '__main__':
            main()
        "options": ["Artificial Intelligence", "Deep Learning", "NLP", "Optimization"],
