// OCI Foundations AI Quiz - Web Version
// Lógica del quiz: bancos, modos, flujo, almacenamiento de fallos.

const QUESTIONS_OFFICIAL = [
  {id:1,q:"Deep Learning - Key feature of RNNs?",o:["Parallel processing","Used for images","Feedback loop retains info across time steps","No internal state"],a:2,e:"RNN conserva estado histórico para secuencias."},
  {id:2,q:"Oracle AI Vector Search primary use?",o:["Store business data","Manage security","Keyword queries","Semantic queries"],a:3,e:"Comparación de embeddings para significado semántico."},
  {id:3,q:"What is overfitting?",o:["Model too simple","Model memorizes training data and fails to generalize","Model ignores input","No output"],a:1,e:"Memoriza datos y pierde generalización."},
  {id:4,q:"Non-parametric supervised algorithm?",o:["Linear Regression","K-Nearest Neighbors (KNN)","Random Forest","Decision Trees"],a:1,e:"KNN no ajusta parámetros internos."},
  {id:5,q:"Purpose of Model Catalog?",o:["Store raw datasets","Deploy endpoints","Real-time engine","Repository to store, track, manage ML models"],a:3,e:"Versionado y gobierno de modelos."},
  {id:6,q:"Technique to predict house price?",o:["Regression","Time Series Analysis","Classification","Clustering"],a:0,e:"Variable continua -> regresión."},
  {id:7,q:"OCI service to deploy trained model?",o:["Object Storage","OCI Language","OCI Data Science","OCI Speech"],a:2,e:"Data Science despliega endpoints."},
  {id:8,q:"NOT an unsupervised ML application?",o:["Spam detection","Outlier detection","Targeted marketing","Customer segmentation"],a:0,e:"Spam es supervisado."},
  {id:9,q:"Vision feature invoice/receipt/resume?",o:["Table extraction","Image classification","Document classification","OCR"],a:2,e:"Clasifica tipo de documento."},
  {id:10,q:"T-Few reduces cost because?",o:["Manual config","Train from scratch","Updates fraction of weights","No customization"],a:2,e:"Ajusta pocos parámetros."},
  {id:11,q:"Data type suited for deep learning?",o:["Human-interpretable","Complex non-human interpretable","Only time series","Only strings"],a:1,e:"Imágenes/audio/video complejos."},
  {id:12,q:"Normalization in Speech does?",o:["Translates","Lowercases","Standardizes numbers/dates/URLs","Removes filler"],a:2,e:"Uniformiza formatos."},
  {id:13,q:"Profanity option mark retain?",o:["Tagging","Removing","Normalization","Masking"],a:0,e:"Marca sin eliminar."},
  {id:14,q:"Vision extract merchant/date/amount?",o:["OCR","Document classification","Key-value extraction","Table extraction"],a:2,e:"Pares clave:valor."},
  {id:15,q:"Difference LLM vs traditional ML?",o:["LLM pretraining large corpus","LLM fewer params","Traditional ML better language","LLM heavy feature eng."],a:0,e:"Preentrenado masivo."},
  {id:16,q:"Concept self-driving car scenario?",o:["Artificial Intelligence","Deep Learning","NLP","Optimization"],a:0,e:"Concepto amplio AI."},
  {id:17,q:"Speech feature per-word certainty?",o:["Confidence scoring","Normalization","Batch support","Masking"],a:0,e:"Certeza por palabra."},
  {id:18,q:"NN best generating music sequences?",o:["FNN","RNN","CNN","Autoencoder"],a:1,e:"Secuencias -> RNN."},
  {id:19,q:"Speech feature closed captions?",o:["Profanity filtering","SRT file support","Confidence scoring","Batching"],a:1,e:"Archivos SRT."},
  {id:20,q:"Principles trustworthy AI?",o:["Lawful, ethical, robust","Fast, unbiased, autonomous","Cheap, scalable, easy","Independent, self-learning, fast"],a:0,e:"Marco legal/ético/robusto."},
  {id:21,q:"Primary function inference?",o:["Label training data","Predict new data outcomes","Adjust weights","Collect datasets"],a:1,e:"Predice casos nuevos."},
  {id:22,q:"Select AI generate SQL?",o:["Templates","Manual params","LLM infers intent","Predefined only"],a:2,e:"Mapea NL a SQL."},
  {id:23,q:"Select AI enhances DB by?",o:["Improving security","Natural language prompts","Removing DBAs","Adding visualization"],a:1,e:"Prompts NL."},
  {id:24,q:"NOT part OCI AI Infra?",o:["OCI Storage","RDMA Network","NVIDIA GPUs","OCI Vault"],a:3,e:"Vault = llaves."},
  {id:25,q:"GPU massive-scale HPC?",o:["H100","GB200","A10","A100"],a:1,e:"Grace Blackwell."},
  {id:26,q:"GPU small/medium scale?",o:["GB200","H200","A100","A10"],a:2,e:"A100 equilibrio."},
  {id:27,q:"Prompt technique explicit examples?",o:["Chain-of-thought","Zero-shot","Few-shot","Self-supervised"],a:2,e:"Ejemplos guían."},
  {id:28,q:"Role tokens LLMs?",o:["Define architecture","Represent params","Determine memory","Minimal text units"],a:3,e:"Unidades básicas."},
  {id:29,q:"Model complete poem lines?",o:["GAN","RNN","CNN","VAE"],a:1,e:"Secuencia -> RNN."},
  {id:30,q:"Generative AI pretraining does?",o:["Needs RLHF only","Memorizes examples","Needs labeled mapping","Learns patterns w/o labeled"],a:3,e:"Auto-supervisión."},
  {id:31,q:"Purpose hidden layer ANN?",o:["Pass data only","Final outputs","Apply filters","Transform inputs"],a:3,e:"Transformación no lineal."},
  {id:32,q:"Label vehicles & plates?",o:["Image classification","Object detection","Speech-to-text","Document classification"],a:1,e:"Bounding boxes."},
  {id:33,q:"AI subset image classification?",o:["Reinforcement","Machine Learning","Deep Learning","NLP"],a:2,e:"DL para imágenes."},
  {id:34,q:"Role target variable?",o:["Feature selection","Input data","Split dataset","Desired output labels"],a:3,e:"Ground truth."},
  {id:35,q:"Categorize news articles?",o:["Language detection","Text classification","Sentiment analysis","NER"],a:1,e:"Asignar categorías."},
  {id:36,q:"Limitation RNN long sequences?",o:["Only numbers","Vanishing gradient","Parallel inefficiency","Only first words"],a:1,e:"Gradiente se atenúa."},
  {id:37,q:"DB 23ai pretrained models vector?",o:["Restrict Oracle APIs","Store raw images","Manual SQL conversion","Loading ONNX models"],a:3,e:"Modelos ONNX."},
  {id:38,q:"Network face recognition?",o:["Autoencoder","CNN","FNN","RNN"],a:1,e:"CNN rasgos espaciales."},
  {id:39,q:"Technique spam filtering?",o:["Reinforcement","NLP","Deep Learning","Machine Learning"],a:3,e:"Clasificación supervisada."},
  {id:40,q:"Data type predicting stock prices?",o:["Sequential","Text","Time series","Image"],a:2,e:"Serie temporal."},
];

const QUESTIONS_OPTIONAL = [
  {id:101,q:"Domain sentiment & translation?",o:["Computer Vision","Speech Processing","Natural Language Processing","Anomaly Detection"],a:2,e:"NLP cubre ambas tareas."},
  {id:102,q:"Model training involves?",o:["Write full program","Relate inputs to outputs","Deploy endpoint","Run inference"],a:1,e:"Ajuste parámetros relación entrada-salida."},
  {id:103,q:"Primary purpose CNN?",o:["Sequential data","Patterns in images","Music generation","Store labels"],a:1,e:"Patrones espaciales."},
  {id:104,q:"Generative vs supervised?",o:["Only classification","Model data distribution create new","Needs labeled pairs","No training"],a:1,e:"Genera ejemplos nuevos."},
  {id:105,q:"Advantage Superclusters?",o:["Social integration","High performance complex AI","Cheapest always","Only simple scripts"],a:1,e:"Escalado GPU + RDMA."},
  {id:106,q:"In-context learning means?",o:["Weight change","Examples in prompt","Zero-shot","Manual features"],a:1,e:"Ejemplos sin reentrenar."},
  {id:107,q:"OCI Speech offers?",o:["Transcribe speech","Classify docs","Generate images","Detect faces"],a:0,e:"Audio -> texto."},
  {id:108,q:"Document Understanding cannot?",o:["Generate audio transcript","Extract tables","Classify documents","Extract text"],a:0,e:"No transcribe audio."},
  {id:109,q:"Interactive coding environment?",o:["Model Catalog","Conda Pack","Notebook Sessions","ADS Jobs"],a:2,e:"Sesiones de notebook."},
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
