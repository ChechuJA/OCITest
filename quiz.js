// OCI Foundations AI Quiz - Web Version
// Lógica del quiz: bancos, modos, flujo, almacenamiento de fallos.

const QUESTIONS_OFFICIAL = [
  {id:1,q:"Which algorithm is a non-parametric approach for supervised learning?",o:["Linear Regression","K-Nearest Neighbors (KNN)","Random Forest","Decision Trees"],a:1,e:"KNN almacena los datos y usa distancias; no ajusta parámetros internos."},
  {id:2,q:"Deep Learning - Key feature of RNNs?",o:["Parallel processing","Used for images","Feedback loop retains info across time steps","No internal state"],a:2,e:"RNN conserva estado temporal mediante estado oculto."},
  {id:3,q:"Oracle AI Vector Search primary use?",o:["Store business data","Manage security","Keyword queries","Semantic queries"],a:3,e:"Busqueda semántica vía embeddings."},
  {id:4,q:"What is overfitting?",o:["Model too simple","Model memorizes training data and fails to generalize","Model ignores input","No output"],a:1,e:"Memoriza datos de entrenamiento y generaliza mal."},
  {id:5,q:"Purpose of Model Catalog?",o:["Store raw datasets","Deploy endpoints","Real-time engine","Repository to store, track, manage ML models"],a:3,e:"Gestión y versionado de modelos."},
  {id:6,q:"Technique to predict house price?",o:["Regression","Time Series Analysis","Classification","Clustering"],a:0,e:"Precio es variable continua -> regresión."},
  {id:7,q:"OCI service to deploy trained model?",o:["Object Storage","OCI Language","OCI Data Science","OCI Speech"],a:2,e:"Data Science permite endpoints de inferencia."},
  {id:8,q:"NOT an unsupervised ML application?",o:["Spam detection","Outlier detection","Targeted marketing","Customer segmentation"],a:0,e:"Spam detection es supervisado."},
  {id:9,q:"Vision feature invoice/receipt/resume?",o:["Table extraction","Image classification","Document classification","OCR"],a:2,e:"Clasificación documental."},
  {id:10,q:"T-Few reduces cost because?",o:["Manual config","Train from scratch","Updates fraction of weights","No customization"],a:2,e:"Actualiza pocos parámetros."},
  {id:11,q:"Data type suited for deep learning?",o:["Human-interpretable","Complex non-human interpretable","Only time series","Only strings"],a:1,e:"Datos complejos (imagen, audio)."},
  {id:12,q:"Normalization in Speech does?",o:["Translates","Lowercases","Standardizes numbers/dates/URLs","Removes filler"],a:2,e:"Estandariza formatos."},
  {id:13,q:"Profanity option mark retain?",o:["Tagging","Removing","Normalization","Masking"],a:0,e:"Etiqueta sin eliminar."},
  {id:14,q:"Vision extract merchant/date/amount?",o:["OCR","Document classification","Key-value extraction","Table extraction"],a:2,e:"Extrae pares clave:valor."},
  {id:15,q:"Difference LLM vs traditional ML?",o:["LLM pretraining large corpus","LLM fewer params","Traditional ML better language","LLM heavy feature eng."],a:0,e:"Preentrenado masivo multitarea."},
  {id:16,q:"Concept self-driving car scenario?",o:["Artificial Intelligence","Deep Learning","NLP","Optimization"],a:0,e:"AI es paraguas general."},
  {id:17,q:"Speech feature per-word certainty?",o:["Confidence scoring","Normalization","Batch support","Masking"],a:0,e:"Confianza por palabra."},
  {id:18,q:"NN best generating music sequences?",o:["FNN","RNN","CNN","Autoencoder"],a:1,e:"RNN maneja secuencias."},
  {id:19,q:"Speech feature closed captions?",o:["Profanity filtering","SRT file support","Confidence scoring","Batching"],a:1,e:"Archivos SRT para subtítulos."},
  {id:20,q:"Principles trustworthy AI?",o:["Lawful, ethical, robust","Fast, unbiased, autonomous","Cheap, scalable, easy","Independent, self-learning, fast"],a:0,e:"Legal, ética y robusta."},
  {id:21,q:"Primary function inference?",o:["Label training data","Predict new data outcomes","Adjust weights","Collect datasets"],a:1,e:"Generar predicciones."},
  {id:22,q:"Select AI generate SQL?",o:["Templates","Manual params","LLM infers intent","Predefined only"],a:2,e:"Inferencia NL -> SQL."},
  {id:23,q:"Select AI enhances DB by?",o:["Improving security","Natural language prompts","Removing DBAs","Adding visualization"],a:1,e:"Prompts en lenguaje natural."},
  {id:24,q:"NOT part OCI AI Infra?",o:["OCI Storage","RDMA Network","NVIDIA GPUs","OCI Vault"],a:3,e:"Vault = gestión de llaves, no infraestructura AI."},
  {id:25,q:"GPU massive-scale HPC?",o:["H100","GB200","A10","A100"],a:1,e:"Grace Blackwell GB200."},
  {id:26,q:"GPU small/medium scale?",o:["GB200","H200","A100","A10"],a:2,e:"A100 balance rendimiento."},
  {id:27,q:"Prompt technique explicit examples?",o:["Chain-of-thought","Zero-shot","Few-shot","Self-supervised"],a:2,e:"Few-shot incluye ejemplos."},
  {id:28,q:"Role tokens LLMs?",o:["Define architecture","Represent params","Determine memory","Minimal text units"],a:3,e:"Unidades mínimas de texto."},
  {id:29,q:"Model complete poem lines?",o:["GAN","RNN","CNN","VAE"],a:1,e:"Secuencias -> RNN."},
  {id:30,q:"Generative AI pretraining does?",o:["Needs RLHF only","Memorizes examples","Needs labeled mapping","Learns patterns w/o labeled"],a:3,e:"Auto-supervisión."},
  {id:31,q:"Purpose hidden layer ANN?",o:["Pass data only","Final outputs","Apply filters","Transform inputs"],a:3,e:"Transformación no lineal interna."},
  {id:32,q:"Label vehicles & plates?",o:["Image classification","Object detection","Speech-to-text","Document classification"],a:1,e:"Detección de objetos."},
  {id:33,q:"AI subset image classification?",o:["Reinforcement","Machine Learning","Deep Learning","NLP"],a:2,e:"Deep Learning (CNN/ViT)."},
  {id:34,q:"Role target variable?",o:["Feature selection","Input data","Split dataset","Desired output labels"],a:3,e:"Ground truth para entrenar."},
  {id:35,q:"Categorize news articles?",o:["Language detection","Text classification","Sentiment analysis","NER"],a:1,e:"Clasificación de texto."},
  {id:36,q:"Limitation RNN long sequences?",o:["Only numbers","Vanishing gradient","Parallel inefficiency","Only first words"],a:1,e:"Gradiente que se desvanece."},
  {id:37,q:"DB 23ai pretrained models vector?",o:["Restrict Oracle APIs","Store raw images","Manual SQL conversion","Loading ONNX models"],a:3,e:"Carga modelos ONNX."},
  {id:38,q:"Network face recognition?",o:["Autoencoder","CNN","FNN","RNN"],a:1,e:"CNN para rasgos espaciales."},
  {id:39,q:"Technique spam filtering?",o:["Reinforcement","NLP","Deep Learning","Machine Learning"],a:3,e:"Clasificación supervisada ML."},
  {id:40,q:"Data type predicting stock prices?",o:["Sequential","Text","Time series","Image"],a:2,e:"Serie temporal indexada."},
  {id:41,q:"Primary role of a loss function during training?",o:["Generate new samples","Measure prediction error to guide optimization","Increase dataset size","Store model weights"],a:1,e:"Cuantifica el error para guiar la optimización y ajuste de pesos."},
];

const QUESTIONS_OPTIONAL = [
  {id:101,q:"Primary task of a discriminator in a GAN?",o:["Generate new data samples","Distinguish between real and generated data","Optimize generator loss","Encode input features"],a:1,e:"Discriminador clasifica si la muestra es real o generada."},
  {id:102,q:"Process of adding randomness to data to protect sensitive information?",o:["Data augmentation","Differential privacy","Feature engineering","Batch normalization"],a:1,e:"Differential Privacy agrega ruido para proteger privacidad."},
  {id:103,q:"Transformer attention allows model to focus on?",o:["Fixed context window","Entire sequence regardless of distance","Adjacent tokens only","Previous sentence only"],a:1,e:"Attention captura relaciones en toda la secuencia."},
  {id:104,q:"Primary function of the encoder in a transformer?",o:["Generate output tokens","Map input sequence to context","Decode sequences","Normalize embeddings"],a:1,e:"El encoder genera representaciones contextuales de la entrada."},
  {id:105,q:"RLHF aligns model outputs with?",o:["Training data statistics","Human preferences and values","Predefined templates","Random sampling"],a:1,e:"RLHF usa feedback humano para alinear salidas a valores deseados."},
  {id:106,q:"Regularization in ML primarily helps?",o:["Speed up training","Prevent overfitting","Increase model size","Generate synthetic data"],a:1,e:"Regularización reduce sobreajuste penalizando complejidad."},
  {id:107,q:"Common application of contrastive learning?",o:["Time series forecasting","Self-supervised representation learning","Classification only","Data augmentation"],a:1,e:"Aprendizaje contrastivo aprende representaciones sin etiquetas."},
  {id:108,q:"Batch normalization in neural networks does?",o:["Regularizes weights","Stabilizes training by normalizing layer inputs","Generates data samples","Reduces learning rate"],a:1,e:"Batch Norm normaliza activaciones para estabilizar entrenamiento."},
  {id:109,q:"Role of activation functions in a neural network?",o:["Store parameters","Introduce non-linearity","Compute loss","Initialize weights"],a:1,e:"Funciones de activación permiten redes aprender relaciones no lineales."},
  {id:110,q:"Which of the following is a key task for Generative AI?",o:["Data encryption","Data classification","Content generation","Data migration"],a:2,e:"Generative AI crea contenido nuevo (texto, imágenes, etc.)."},
  {id:111,q:"In reinforcement learning, what is the agent's goal?",o:["Minimize loss function","Maximize cumulative reward","Label training data","Reduce dimensionality"],a:1,e:"El agente busca maximizar la recompensa acumulada."},
  {id:112,q:"What is a common use case for computer vision?",o:["Text sentiment analysis","Object detection in images","Time series forecasting","Speech synthesis"],a:1,e:"Computer vision detecta y clasifica objetos en imágenes."},
  {id:113,q:"Which algorithm is commonly used for unsupervised learning?",o:["Logistic regression","K-Means clustering","Linear regression","Decision trees"],a:1,e:"K-Means es un algoritmo de clustering no supervisado."},
  {id:114,q:"What is a common password validation approach?",o:["Regular expressions","Neural networks","K-means","PCA"],a:0,e:"Regex valida patrones de formato de contraseñas."},
  {id:115,q:"What does the softmax activation function do?",o:["Converts outputs to probabilities","Introduces sparsity","Reduces dimensionality","Normalizes inputs"],a:0,e:"Softmax convierte logits en distribución de probabilidad."},
  {id:116,q:"Which model architecture is best suited for sequence-to-sequence tasks?",o:["Feedforward NN","Encoder-Decoder (Seq2Seq)","Decision Tree","K-NN"],a:1,e:"Seq2Seq (ej. Transformers) mapea secuencias a secuencias."},
  {id:117,q:"What is a key advantage of LSTM over standard RNN?",o:["Faster training","Mitigates vanishing gradient problem","Requires less data","Smaller model size"],a:1,e:"LSTM con gates maneja mejor gradientes de largo plazo."},
  {id:118,q:"What does a neuron in a neural network compute?",o:["Weighted sum + activation","Only the loss","Data normalization","Gradient descent"],a:0,e:"Neurona calcula suma ponderada y aplica función de activación."},
  {id:119,q:"What is the purpose of fine-tuning a pre-trained model?",o:["Increase model size","Adapt model to specific task/domain","Remove all weights","Train from scratch"],a:1,e:"Fine-tuning adapta un modelo preentrenado a un dominio específico."},
  {id:120,q:"Which factor most directly impacts the cost of an LLM inference?",o:["Model size and input length","Color of the logo","Number of developers","Office location"],a:0,e:"Tamaño del modelo y longitud de input afectan cómputo/costo."},
  {id:121,q:"What is an embedding in NLP?",o:["A type of regularization","A dense vector representation of text","A loss function","A data augmentation technique"],a:1,e:"Embedding representa palabras/tokens como vectores densos."},
  {id:122,q:"What is OCI Data Science Jobs used for?",o:["Storing data","Running batch ML workloads","Real-time inference","Data visualization only"],a:1,e:"Jobs ejecuta trabajos batch (entrenamiento, procesamiento)."},
  {id:123,q:"What is the purpose of OCI Data Science Model Deployment?",o:["Store datasets","Serve models via API endpoints","Train models","Visualize data"],a:1,e:"Model Deployment expone modelos como endpoints HTTP."},
  {id:124,q:"What is the OCI Generative AI Playground used for?",o:["Production deployment","Experimenting with prompts and models","Storing training data","Managing security policies"],a:1,e:"Playground permite probar prompts y modelos generativos."},
  {id:125,q:"Which OCI service provides pre-built AI models for language tasks?",o:["OCI Compute","OCI Object Storage","OCI Language","OCI Vault"],a:2,e:"OCI Language ofrece NER, sentiment, clasificación, etc."},
  {id:126,q:"What languages does OCI Language service support?",o:["Only English","Multiple languages including Spanish","Only programming languages","Only Asian languages"],a:1,e:"OCI Language soporta múltiples idiomas (inglés, español, etc.)."},
  {id:127,q:"What is OCI Document Understanding used for?",o:["Managing databases","Extracting text, tables, and structure from documents","Training custom models","Real-time video streaming"],a:1,e:"Document Understanding extrae texto, tablas y estructura."},
  {id:128,q:"What is a key feature of OCI Vision service?",o:["Speech recognition","Image classification and object detection","Time series analysis","Data warehousing"],a:1,e:"Vision clasifica imágenes y detecta objetos."},
  {id:129,q:"What does OCI Anomaly Detection service do?",o:["Encrypts data","Detects unusual patterns in time series data","Generates synthetic data","Translates languages"],a:1,e:"Anomaly Detection identifica patrones anómalos en series temporales."},
  {id:130,q:"What is sentiment analysis?",o:["Detecting objects in images","Determining emotional tone of text","Clustering data","Dimensionality reduction"],a:1,e:"Sentiment analysis clasifica el tono emocional (positivo/negativo/neutro)."},
  {id:131,q:"What is the role of backpropagation in neural networks?",o:["Initialize weights","Compute gradients for weight updates","Generate outputs","Normalize inputs"],a:1,e:"Backpropagation calcula gradientes para ajustar pesos."},
  {id:132,q:"What does self-attention in transformers compute?",o:["Loss function","Relevance of each token to others in sequence","Learning rate","Batch size"],a:1,e:"Self-attention pondera la relevancia entre tokens de la secuencia."},
  {id:133,q:"Which metric is commonly used to evaluate classification models?",o:["Mean Squared Error","Accuracy, Precision, Recall, F1","R-squared","Mean Absolute Error"],a:1,e:"Clasificación usa accuracy, precision, recall, F1."},
  {id:134,q:"What is transfer learning?",o:["Moving data between servers","Using a pre-trained model as starting point for new task","Training multiple models simultaneously","Deleting old models"],a:1,e:"Transfer learning reutiliza conocimiento de un modelo preentrenado."},
];

const bankSelect = document.getElementById('bankSelect');
const modeSelect = document.getElementById('modeSelect');
const startBtn = document.getElementById('startBtn');
const quizEl = document.getElementById('quiz');
const progressEl = document.getElementById('progress');
const progressTextEl = document.getElementById('progressText');
const progressFillEl = document.getElementById('progressFill');
const timeRemainingEl = document.getElementById('timeRemaining');
const questionContainer = document.getElementById('questionContainer');
const optionsEl = document.getElementById('options');
const feedbackEl = document.getElementById('feedback');
const skipBtn = document.getElementById('skipBtn');
const nextBtn = document.getElementById('nextBtn');
const summaryEl = document.getElementById('summary');

let currentIndex = 0;
let currentBank = [];
let order = [];
let score = 0;
let wrong = [];
let answered = false;
let totalTimeSeconds = 7200; // 2 horas
let remainingSeconds = totalTimeSeconds;
let timerInterval = null;

function getBank() {
  if (bankSelect.value === 'official') return [...QUESTIONS_OFFICIAL];
  if (bankSelect.value === 'optional') return [...QUESTIONS_OPTIONAL];
  return [...QUESTIONS_OFFICIAL, ...QUESTIONS_OPTIONAL];
}

function getReviewBank() {
  try {
    const stored = JSON.parse(localStorage.getItem('lastWrongIds') || '[]');
    if (!stored.length) return [];
    const all = [...QUESTIONS_OFFICIAL, ...QUESTIONS_OPTIONAL];
    return all.filter(q => stored.includes(q.id));
  } catch (e) { return []; }
}

function startQuiz() {
  score = 0; wrong = []; answered = false; feedbackEl.textContent = '';
  const mode = modeSelect.value;
  currentBank = mode === 'review' ? getReviewBank() : getBank();
  if (mode === 'review' && currentBank.length === 0) {
    alert('No hay preguntas previas falladas almacenadas.');
    return;
  }
  order = [...currentBank];
  if (mode === 'random') shuffle(order);
  currentIndex = 0;
  // Reiniciar timer
  clearInterval(timerInterval);
  remainingSeconds = totalTimeSeconds;
  startTimer();
  quizEl.hidden = false;
  summaryEl.hidden = true;
  renderCurrent();
}

function shuffle(arr){for(let i=arr.length-1;i>0;i--){const j=Math.floor(Math.random()* (i+1));[arr[i],arr[j]]=[arr[j],arr[i]];}}

function renderCurrent() {
  nextBtn.disabled = true;
  answered = false;
  const q = order[currentIndex];
  progressEl.textContent = '';
  const answeredCount = currentIndex; // antes de responder actual
  const percent = ((answeredCount / order.length) * 100).toFixed(1);
  progressTextEl.textContent = `Progreso: ${answeredCount}/${order.length} (${percent}%)`;
  progressFillEl.style.width = `${percent}%`;
  questionContainer.textContent = `Q${q.id}: ${q.q}`;
  optionsEl.innerHTML = '';
  q.o.forEach((opt,idx)=>{
    const li = document.createElement('li');
    const btn = document.createElement('button');
    btn.textContent = `${String.fromCharCode(65+idx)}. ${opt}`;
    btn.addEventListener('click', ()=> selectOption(idx));
    li.appendChild(btn);
    optionsEl.appendChild(li);
  });
  feedbackEl.className = 'feedback';
  feedbackEl.textContent = '';
}

function selectOption(idx){
  if (answered) return;
  const q = order[currentIndex];
  answered = true;
  nextBtn.disabled = false;
  if (idx === q.a){
    score++;
    feedbackEl.textContent = '✔ Correcto';
    feedbackEl.classList.add('correct');
  } else {
    wrong.push(q);
    feedbackEl.textContent = `✘ Incorrecto. Correcta: ${String.fromCharCode(65+q.a)}\n${q.e}`;
    feedbackEl.classList.add('incorrect');
  }
}

skipBtn.addEventListener('click', ()=>{
  if (answered) return; // si ya respondió no se salta
  const q = order[currentIndex];
  wrong.push(q); // contar como incorrecta
  answered = true;
  nextBtn.disabled = false;
  feedbackEl.textContent = `Explicación: ${q.e} (Correcta: ${String.fromCharCode(65+q.a)})`;
  feedbackEl.className = 'feedback incorrect';
});

nextBtn.addEventListener('click', ()=>{
  if (!answered) return;
  currentIndex++;
  if (currentIndex >= order.length){
    finishQuiz();
  } else {
    renderCurrent();
  }
});

function finishQuiz(){
  quizEl.hidden = true;
  summaryEl.hidden = false;
  const total = order.length;
  const pct = ((score/total)*100).toFixed(1);
  clearInterval(timerInterval);
  summaryEl.innerHTML = `<h2>Resumen</h2>
    <p>Puntuación: <strong>${score}/${total}</strong> (${pct}%).</p>`;
  if (wrong.length){
    const ids = wrong.map(q=>q.id);
    localStorage.setItem('lastWrongIds', JSON.stringify(ids));
    const list = wrong.map(q=>`<li>Q${q.id} - ${q.q} <span class="badge">Correcta: ${String.fromCharCode(65+q.a)}</span></li>`).join('');
    summaryEl.innerHTML += `<h3>Preguntas falladas</h3><ul>${list}</ul><p>Guardadas para repaso.</p>`;
  } else {
    localStorage.setItem('lastWrongIds', '[]');
    summaryEl.innerHTML += '<p>¡Perfecto! Sin errores.</p>';
  }
  summaryEl.innerHTML += '<p><button id="restartBtn">Reiniciar</button></p>';
  document.getElementById('restartBtn').addEventListener('click', ()=>{
    quizEl.hidden = true; summaryEl.hidden = true; score=0; wrong=[]; });
}

startBtn.addEventListener('click', startQuiz);

// Accesibilidad teclado para opciones (ya son botones)
// Foco inicial al iniciar
startBtn.focus();

function startTimer(){
  updateTimerDisplay();
  timerInterval = setInterval(()=>{
    remainingSeconds--;
    if (remainingSeconds <= 0){
      remainingSeconds = 0;
      updateTimerDisplay();
      clearInterval(timerInterval);
      alert('Tiempo agotado. Se cerrará el examen.');
      finishQuiz();
      return;
    }
    updateTimerDisplay();
  },1000);
}

function updateTimerDisplay(){
  const h = Math.floor(remainingSeconds/3600);
  const m = Math.floor((remainingSeconds%3600)/60);
  const s = remainingSeconds%60;
  const pad = v => v.toString().padStart(2,'0');
  timeRemainingEl.textContent = `Tiempo restante: ${pad(h)}:${pad(m)}:${pad(s)}`;
  if (remainingSeconds <= 600){ // últimos 10 minutos
    timeRemainingEl.id = 'timeWarning';
  } else {
    timeRemainingEl.id = '';
  }
}

// ============================================================================
// GESTIÓN DE EXÁMENES EXTERNOS
// ============================================================================

let examsCatalog = null;
let currentExternalQuestions = [];

// Referencias a nuevos elementos DOM
const examSourceEl = document.getElementById('examSource');
const builtinBankEl = document.getElementById('builtinBank');
const externalExamEl = document.getElementById('externalExam');
const examSelectEl = document.getElementById('examSelect');

// Cargar catálogo al iniciar
async function initializeExamsCatalog() {
  examsCatalog = await loadExamsCatalog();
  
  if (!examsCatalog) {
    console.warn('No se pudo cargar el catálogo de exámenes');
    examSourceEl.disabled = true;
    return;
  }
  
  // Poblar selector de exámenes por categoría
  examSelectEl.innerHTML = '<option value="">-- Seleccione un examen --</option>';
  
  // Agrupar por categoría
  const categories = {};
  examsCatalog.exams.forEach(exam => {
    if (!categories[exam.category]) {
      categories[exam.category] = [];
    }
    categories[exam.category].push(exam);
  });
  
  // Crear optgroups
  Object.keys(categories).sort().forEach(category => {
    const optgroup = document.createElement('optgroup');
    optgroup.label = category;
    
    categories[category].forEach(exam => {
      const option = document.createElement('option');
      option.value = exam.file;
      option.textContent = `${exam.title} (${exam.questions} preguntas)`;
      optgroup.appendChild(option);
    });
    
    examSelectEl.appendChild(optgroup);
  });
  
  console.log('✅ Catálogo de exámenes inicializado');
}

// Manejar cambio de fuente
examSourceEl.addEventListener('change', () => {
  const isExternal = examSourceEl.value === 'external';
  builtinBankEl.hidden = isExternal;
  externalExamEl.hidden = !isExternal;
});

// Inicializar al cargar la página
if (typeof loadExamsCatalog === 'function') {
  initializeExamsCatalog();
} else {
  console.warn('exam-loader.js no está cargado. Funcionalidad de exámenes externos deshabilitada.');
  examSourceEl.disabled = true;
}

// Modificar startQuiz para soportar exámenes externos
const originalStartQuiz = startQuiz;
startQuiz = async function() {
  // Si es examen externo, cargar preguntas primero
  if (examSourceEl.value === 'external') {
    const selectedFile = examSelectEl.value;
    
    if (!selectedFile) {
      alert('Por favor selecciona un examen');
      return;
    }
    
    // Mostrar loading
    startBtn.disabled = true;
    startBtn.textContent = 'Cargando...';
    
    // Cargar examen
    currentExternalQuestions = await loadExam(selectedFile);
    
    if (currentExternalQuestions.length === 0) {
      alert('Error al cargar el examen. Verifica la consola para más detalles.');
      startBtn.disabled = false;
      startBtn.textContent = 'Comenzar';
      return;
    }
    
    console.log(`✅ Examen externo cargado: ${currentExternalQuestions.length} preguntas`);
    
    // Usar preguntas externas
    pool = currentExternalQuestions.slice();
    
    // Continuar con el flujo normal
    startBtn.textContent = 'Comenzar';
    startBtn.disabled = false;
  } else {
    // Usar preguntas integradas (comportamiento original)
    currentExternalQuestions = [];
  }
  
  // Llamar a la función original
  originalStartQuiz();
};
