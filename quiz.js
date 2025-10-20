// OCI Foundations AI Quiz - Web Version (limpio y sincronizado)

// Preguntas oficiales (Q1=KNN, Q2=RNN) usando campos compactos:
// id, q (question), o (options), a (answer index), e (explanation)
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

// Preguntas opcionales (IDs 101+)
const QUESTIONS_OPTIONAL = [
  {id:101,q:"Domain sentiment & translation?",o:["Computer Vision","Speech Processing","Natural Language Processing","Anomaly Detection"],a:2,e:"NLP cubre análisis de sentimiento y traducción."},
  {id:102,q:"Model training involves?",o:["Write full program","Relate inputs to outputs","Deploy endpoint","Run inference"],a:1,e:"Ajustar parámetros mapeo entrada-salida."},
  {id:103,q:"Primary purpose CNN?",o:["Sequential data","Patterns in images","Music generation","Store labels"],a:1,e:"Patrones espaciales en imágenes."},
  {id:104,q:"Generative vs supervised?",o:["Only classification","Model data distribution create new","Needs labeled pairs","No training"],a:1,e:"Genera muestras nuevas."},
  {id:105,q:"Advantage Superclusters?",o:["Social integration","High performance complex AI","Cheapest always","Only simple scripts"],a:1,e:"Escalado GPU + red RDMA."},
  {id:106,q:"In-context learning means?",o:["Weight change","Examples in prompt","Zero-shot","Manual features"],a:1,e:"Ejemplos en prompt sin ajustar pesos."},
  {id:107,q:"OCI Speech offers?",o:["Transcribe speech","Classify docs","Generate images","Detect faces"],a:0,e:"Audio -> texto."},
  {id:108,q:"Document Understanding cannot?",o:["Generate audio transcript","Extract tables","Classify documents","Extract text"],a:0,e:"No transcribe audio."},
  {id:109,q:"Interactive coding environment?",o:["Model Catalog","Conda Pack","Notebook Sessions","ADS Jobs"],a:2,e:"Notebook Sessions para desarrollo interactivo."},
  // Nuevas preguntas O110–O134
  {id:110,q:"Generative AI typical task?",o:["Detect credit card fraud","Count words","Identify article topic","Write themed poem"],a:3,e:"Produce contenido nuevo (poema)."},
  {id:111,q:"Learning for autonomous driving decisions?",o:["Supervised","Unsupervised","Reinforcement","NLP"],a:2,e:"Agente optimiza recompensa acumulada."},
  {id:112,q:"NOT core Computer Vision exam task?",o:["Facial recognition","Image classification","Object detection","Repair damaged images"],a:3,e:"Restauración no es foco principal."},
  {id:113,q:"Find patterns without labels?",o:["Supervised","Unsupervised","Reinforcement","Regression"],a:1,e:"Descubre estructura inherente."},
  {id:114,q:"App that typically NO ML?",o:["Password validation","Spam detection","Customer segmentation","Stock prediction"],a:0,e:"Reglas determinísticas suficientes."},
  {id:115,q:"Activation used in logistic regression?",o:["Identity","Step","Sigmoid","Gaussian"],a:2,e:"Sigmoid mapea a probabilidad (0,1)."},
  {id:116,q:"Seq2Seq translation architecture?",o:["One-to-One","One-to-Many","Many-to-One","Many-to-Many"],a:3,e:"Entrada y salida ambas secuencias."},
  {id:117,q:"Handle long-range dependencies best?",o:["Simple RNN","CNN","LSTM","MLP"],a:2,e:"Puertas mitigan vanishing gradient."},
  {id:118,q:"Component weighted sum + activation?",o:["Neuron","Bias","Classifier","Iterator"],a:0,e:"Neurona aplica w·x+b y activación."},
  {id:119,q:"When can skip LLM fine-tuning?",o:["Needs task-specific adaptation","Bias mitigation","Domain vocab","Latency optimization"],a:0,e:"Si no hay adaptación específica basta prompting."},
  {id:120,q:"NOT ideal seq model use?",o:["Time series","Image classification","Translation","Speech recognition"],a:1,e:"Imágenes mejor con CNN/ViT."},
  {id:121,q:"Factor impacting LLM capability/cost?",o:["Interface buttons","Programming language","Model size/parameters","Concurrent users"],a:2,e:"Parámetros definen capacidad y coste."},
  {id:122,q:"Datatype for embeddings DB 23ai?",o:["ARRAY","VECTOR","STRING","BOOLEAN"],a:1,e:"VECTOR almacena representaciones densas."},
  {id:123,q:"Repeatable ML tasks infra?",o:["Conda Packs","Jobs","Compartments","Notebook Sessions"],a:1,e:"Jobs orquestan ejecuciones reproducibles."},
  {id:124,q:"Expose model via HTTP?",o:["Model Catalog","Model Deployments","Jobs","Artifacts"],a:1,e:"Deployments crean endpoint inferencia."},
  {id:125,q:"NOT OCI AI service?",o:["Vision","Speech","Language","Translator"],a:3,e:"Translator no listado como servicio standalone."},
  {id:126,q:"Chat vs Embedding models?",o:["Ambos generan texto","Chat texto; Embedding vectores","Embedding texto; Chat vectores","Embedding sólo imágenes"],a:1,e:"Embeddings = representación semántica."},
  {id:127,q:"Generative AI Playground purpose?",o:["Optimize GPU hardware","Test models visually no code","Create VCNs","Convert images to audio"],a:1,e:"Explorar prompts y respuestas."},
  {id:128,q:"Primary role model endpoints?",o:["Scale storage","Serve fine-tuned model inference","Billing metrics","Translate SQL"],a:1,e:"Inferencia gestionada versión-controlada."},
  {id:129,q:"Resource needed fine-tune domain LLM?",o:["Shared tenancy","Object Storage only","Dedicated AI Cluster","Dashboard"],a:2,e:"Cluster dedicado para ajuste parámetros."},
  {id:130,q:"Language assumed NOT supported (example)?",o:["English","Spanish","Portuguese","Mandarin"],a:3,e:"Mandarín marcado como no soportado en ejemplo."},
  {id:131,q:"Extract structured tables PDFs?",o:["Language","Speech","Document Understanding","Object Storage"],a:2,e:"DU reconstruye estructura tabular."},
  {id:132,q:"Language service capability?",o:["Object detection","Sentiment analysis","Speech to text","Compile code"],a:1,e:"Sentiment incluido en Language."},
  {id:133,q:"Algorithm updating weights ANN?",o:["Random Forest","SVM","Backpropagation","K-Means"],a:2,e:"Backprop calcula gradientes para optimización."},
  {id:134,q:"Self-attention achieves?",o:["Focus only last tokens","Same importance every token","Contextual weighting tokens","Replace embeddings with rules"],a:2,e:"Asigna pesos contextuales por relevancia."},
];

// Referencias DOM
const bankSelect = document.getElementById('bankSelect');
const examSelect = document.getElementById('examSelect');
const modeSelect = document.getElementById('modeSelect');
const startBtn = document.getElementById('startBtn');
const quizEl = document.getElementById('quiz');
const progressTextEl = document.getElementById('progressText');
const progressFillEl = document.getElementById('progressFill');
const timeRemainingEl = document.getElementById('timeRemaining');
const questionContainer = document.getElementById('questionContainer');
const optionsEl = document.getElementById('options');
const feedbackEl = document.getElementById('feedback');
const explainBtn = document.getElementById('explainBtn');
const skipBtn = document.getElementById('skipBtn');
const markBtn = document.getElementById('markBtn');
const nextBtn = document.getElementById('nextBtn');
const summaryEl = document.getElementById('summary');
const extendedToggle = document.getElementById('extendedToggle');
// Modal elements
const openDocsBtn = document.getElementById('openDocsBtn');
const docsModal = document.getElementById('docsModal');
const closeModalBtn = document.getElementById('closeModalBtn');
const glossSearch = document.getElementById('glossSearch');
const glossaryResults = document.getElementById('glossaryResults');
const docsContent = document.getElementById('docsContent');
const docsIndex = document.getElementById('docsIndex');
const glossCategory = document.getElementById('glossCategory');
const searchCount = document.getElementById('searchCount');

// Glossary raw terms (mirroring documentacion.md table)
const GLOSSARY = [
  {term:'Embedding', def:'Vector semántico denso de texto/imagen', cat:'ML'},
  {term:'Token', def:'Unidad mínima de entrada LLM', cat:'Prompting'},
  {term:'Endpoint de Inferencia', def:'API que expone predicciones', cat:'ML'},
  {term:'OCR', def:'Extracción de texto en imágenes', cat:'ML'},
  {term:'Key-Value Extraction', def:'Pares estructurados (doc)', cat:'ML'},
  {term:'Few-Shot', def:'Pocos ejemplos en prompt', cat:'Prompting'},
  {term:'In-Context Learning', def:'Adaptación sin reentrenar', cat:'Prompting'},
  {term:'Vanishing Gradient', def:'Gradiente que se extingue en secuencias largas', cat:'ML'},
  {term:'T-Few', def:'Fine-tuning eficiente', cat:'Prompting'},
  {term:'RDMA', def:'Red de baja latencia', cat:'Infra'},
  {term:'Loss Function', def:'Mide error para optimización', cat:'ML'}
];

function openModal(){
  docsModal.hidden = false;
  docsModal.setAttribute('aria-hidden','false');
  // Load documentation (fetch local markdown)
  fetch('documentacion.md')
    .then(r=>r.text())
    .then(md=>{ 
      const rendered = renderMarkdownRich(md); 
      docsContent.innerHTML = rendered.html; 
      buildDocsIndex(rendered.headings);
      attachScrollSync(rendered.headings);
    })
    .catch(()=>{ docsContent.textContent='No se pudo cargar la documentación.'; });
  renderGlossary();
  glossSearch.focus();
}
function closeModal(){
  docsModal.hidden = true;
  docsModal.setAttribute('aria-hidden','true');
}
openDocsBtn?.addEventListener('click', openModal);
closeModalBtn?.addEventListener('click', closeModal);
docsModal?.addEventListener('click', e=>{ if(e.target === docsModal) closeModal(); });
document.addEventListener('keydown', e=>{ if(e.key==='Escape' && docsModal.getAttribute('aria-hidden')==='false') closeModal(); });

function renderGlossary(filter=''){ 
  const f = filter.trim().toLowerCase();
  const cat = glossCategory.value;
  let items = GLOSSARY;
  if (cat) items = items.filter(it=> it.cat === cat);
  if (f) items = items.filter(it=> it.term.toLowerCase().includes(f) || it.def.toLowerCase().includes(f));
  searchCount.textContent = `${items.length} término(s)`;
  glossaryResults.innerHTML = '<h3>Glosario</h3>' + (items.map(it=>{
    const highlightedTerm = highlight(it.term, f);
    const highlightedDef = highlight(it.def, f);
    return `<div class="gloss-item"><strong>${highlightedTerm}</strong><span class="category-tag">${it.cat}</span><br>${highlightedDef}<button class="copy-btn" data-term="${it.term}">Copiar</button></div>`;
  }).join('') || '<p>Sin coincidencias.</p>');
  glossaryResults.querySelectorAll('.copy-btn').forEach(btn=>{
    btn.addEventListener('click',()=>{
      const t = btn.getAttribute('data-term');
      navigator.clipboard.writeText(t).then(()=>{ btn.textContent='Copiado'; setTimeout(()=>btn.textContent='Copiar',1200); });
    });
  });
}
function highlight(text, f){
  if(!f) return text;
  const re = new RegExp(`(${escapeRegExp(f)})`,'gi');
  return text.replace(re,'<mark>$1</mark>');
}
function escapeRegExp(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
glossSearch?.addEventListener('input', ()=> renderGlossary(glossSearch.value));
glossCategory?.addEventListener('change', ()=> renderGlossary(glossSearch.value));

// Rich markdown renderer: headings, paragraphs, emphasis, inline code, fenced code, tables, lists
function renderMarkdownRich(md){
  const esc = (s)=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  const lines = md.split(/\r?\n/);
  const out = [];
  const headings = [];
  let inCode = false, codeLang='';
  let tableBuffer = [];
  let listBuffer = [];
  function flushTable(){
    if(!tableBuffer.length) return;
    // Build table
    const rows = tableBuffer.map(r=> r.split('|').slice(1,-1).map(c=>c.trim()));
    const header = rows[0];
    const body = rows.slice(2); // skip separator
    const htmlRows = body.map(r=> `<tr>${r.map((c,i)=>`<td>${formatInline(c)}</td>`).join('')}</tr>`).join('');
    out.push(`<table><thead><tr>${header.map(h=>`<th>${formatInline(h)}</th>`).join('')}</tr></thead><tbody>${htmlRows}</tbody></table>`);
    tableBuffer=[];
  }
  function flushList(){
    if(!listBuffer.length) return;
    const items = listBuffer.map(li=> `<li>${formatInline(li.replace(/^[*\-+]\s+/,'').trim())}</li>`).join('');
    out.push(`<ul>${items}</ul>`); listBuffer=[];
  }
  function formatInline(text){
    // Bold **text** / Italic *text* / inline code `code`
    let t = esc(text);
    t = t.replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>');
    t = t.replace(/(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)/g,'<em>$1</em>');
    t = t.replace(/`([^`]+)`/g,'<code>$1</code>');
    return t;
  }
  lines.forEach(line=>{
    if(/^```/.test(line)){ // fenced code
      if(!inCode){ inCode=true; codeLang=line.replace(/```/,'').trim(); out.push(`<pre class="code-block" data-lang="${esc(codeLang)}">`); }
      else { inCode=false; codeLang=''; out.push('</pre>'); }
      return;
    }
    if(inCode){ out.push(esc(line)+'\n'); return; }
    if(/^#{1,6} /.test(line)){
      flushTable(); flushList();
      const level = line.match(/^#+/)[0].length;
      const content = line.replace(/^#{1,6} /,'').trim();
      const id = content.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');
      headings.push({id, level, text:content});
      out.push(`<h${level} id="${id}">${formatInline(content)}</h${level}>`);
      return;
    }
    if(line.startsWith('|')){ tableBuffer.push(line); return; }
    if(/^[*\-+]\s+/.test(line)){ listBuffer.push(line); return; }
    if(line.trim()===''){ flushTable(); flushList(); return; }
    flushTable(); flushList();
    out.push(`<p>${formatInline(line)}</p>`);
  });
  flushTable(); flushList();
  return {html: out.join('\n'), headings};
}
function buildDocsIndex(headings){
  if(!docsIndex) return;
  const links = headings.filter(h=>h.level<=3).map(h=>`<a href="#${h.id}" data-id="${h.id}">${h.text}</a>`).join('');
  docsIndex.innerHTML = `<strong>Índice</strong>${links}`;
}
function attachScrollSync(headings){
  const contentEl = docsContent;
  const obs = new IntersectionObserver(entries=>{
    entries.forEach(en=>{
      if(en.isIntersecting){
        const id = en.target.id;
        docsIndex.querySelectorAll('a').forEach(a=> a.classList.toggle('active', a.dataset.id===id));
      }
    });
  },{root:contentEl, threshold:0.3});
  headings.forEach(h=>{ const el = document.getElementById(h.id); if(el) obs.observe(el); });
  // Smooth scroll behavior
  docsIndex.querySelectorAll('a').forEach(a=>{
    a.addEventListener('click', e=>{ e.preventDefault(); const target=document.getElementById(a.dataset.id); if(target){ target.scrollIntoView({behavior:'smooth'}); } });
  });
}

// Estado
let currentIndex = 0;
let order = [];
let score = 0;
let wrong = [];
let skipped = [];
let marked = [];
let answered = false;
let secondPass = false;
const totalTimeSeconds = 7200; // 2 horas
let remainingSeconds = totalTimeSeconds;
let timerInterval = null;
let EXTENDED_MAP = null; // id -> extended HTML block
let extendedLoaded = false;
// Bancos externos cacheados { rutaMarkdown: [preguntas] }
const EXTERNAL_BANKS = {};
const ENABLE_DEDUP = true; // desactivar si se quiere ver duplicados

// Restaurar preferencias guardadas
function restorePreferences(){
  const savedExam = localStorage.getItem('examSelect');
  if(savedExam && examSelect) examSelect.value = savedExam;
  const savedBank = localStorage.getItem('bankSelect');
  if(savedBank && bankSelect) bankSelect.value = savedBank;
  const savedExt = localStorage.getItem('extendedMode');
  if(savedExt && extendedToggle) extendedToggle.value = savedExt;
}
restorePreferences();
examSelect?.addEventListener('change',()=> localStorage.setItem('examSelect', examSelect.value));
bankSelect?.addEventListener('change',()=> localStorage.setItem('bankSelect', bankSelect.value));
extendedToggle?.addEventListener('change',()=> localStorage.setItem('extendedMode', extendedToggle.value));

// Cargar y preparar mapa de enunciados extendidos
function loadExtended(){
  if (extendedLoaded) return Promise.resolve();
  return fetch('preguntas_extendidas.md')
    .then(r=>r.text())
    .then(txt=>{
      EXTENDED_MAP = buildExtendedMap(txt);
      extendedLoaded = true;
    })
    .catch(()=>{EXTENDED_MAP={}; extendedLoaded=true;});
}

// Heurística: asociar bloques por palabras clave presentes en pregunta corta.
function buildExtendedMap(md){
  const map={};
  // Split by headings ### to isolate blocks
  const parts = md.split(/\n### /).slice(1).map(p=>'### '+p.trim());
  // Define keyword patterns for official IDs
  const patterns = [
    {id:1, r:/\bK-Nearest Neighbors|non-parametric\b/i},
    {id:2, r:/\bRNN\b/i},
    {id:3, r:/Vector Search/i},
    {id:4, r:/overfitting/i},
    {id:5, r:/Model Catalog/i},
    {id:6, r:/Regression\b/i},
    {id:7, r:/deploy trained model|OCI Data Science service/i},
    {id:8, r:/Document Understanding NOT/i},
    {id:9, r:/invoice|receipt|resume/i},
    {id:10,r:/T-Few/i},
    {id:11,r:/deep learning data type/i},
    {id:12,r:/Normalization in Speech/i},
    {id:13,r:/Profanity|Tagging/i},
    {id:14,r:/merchant|key-value extraction/i},
    {id:15,r:/LLMs vs traditional|large corpus/i},
    {id:16,r:/self-driving car/i},
    {id:17,r:/per-word certainty|Confidence scoring/i},
    {id:18,r:/music sequences/i},
    {id:19,r:/SRT|closed captions/i},
    {id:20,r:/trustworthy AI/i},
    {id:21,r:/inference function/i},
    {id:22,r:/Select AI enhance|generate SQL/i},
    {id:23,r:/Select AI prompts/i},
    {id:24,r:/OCI Vault no es compute|NOT part of OCI AI Infrastructure/i},
    {id:25,r:/Superclusters|GB200/i},
    {id:26,r:/A100/i},
    {id:27,r:/Few-shot prompting/i},
    {id:28,r:/Tokens role/i},
    {id:29,r:/complete poem/i},
    {id:30,r:/Pretraining generative/i},
    {id:31,r:/Hidden layer purpose/i},
    {id:32,r:/vehicles and license plates|Object detection scenario/i},
    {id:33,r:/image classification software|Deep Learning/i},
    {id:34,r:/target variable/i},
    {id:35,r:/Categorize news articles/i},
    {id:36,r:/Vanishing gradient/i},
    {id:37,r:/ONNX models/i},
    {id:38,r:/face recognition|CNN/i},
    {id:39,r:/spam filtering/i},
    {id:40,r:/stock prices|time series/i},
    {id:41,r:/loss function/i},
  ];
  parts.forEach(block=>{
    patterns.forEach(p=>{ if(p.r.test(block)){ if(!map[p.id]) map[p.id]=sanitizeExtended(block); } });
  });
  return map;
}

function sanitizeExtended(block){
  // Remove leading ### heading, keep content structured, escape HTML minimal then allow formatting markers
  const lines = block.split(/\n/);
  // Convert to simple HTML paragraphs preserving bullets
  const html = lines.map(l=>{
    if(/^### /.test(l)) return `<h3 class="ext-heading">${l.replace(/^### /,'')}</h3>`;
    if(/^\s*[-•@O]/.test(l)) return `<p class="ext-line">${l}</p>`;
    return `<p class="ext-line">${l}</p>`;
  }).join('');
  return html;
}

function getSelectedBank(){
  // Si se selecciona fuente externa, ignorar select interno (salvo modo none)
  if(examSelect && examSelect.value !== 'none'){
    return buildExternalComposite(examSelect.value);
  }
  if (bankSelect.value === 'official') return [...QUESTIONS_OFFICIAL];
  if (bankSelect.value === 'optional') return [...QUESTIONS_OPTIONAL];
  if (bankSelect.value === 'both' || bankSelect.value === 'complete') return [...QUESTIONS_OFFICIAL, ...QUESTIONS_OPTIONAL];
  return [...QUESTIONS_OFFICIAL];
}

// Mapping from exam keys to file arrays (shared by buildExternalComposite and ensureExternalBanks)
const EXTERNAL_FILE_MAP = {
  'oci-foundations': ['Nuevos/Oracle Exam 1Z0-1085-25 Dump.md'],
  'ai-oficial': ['Nuevos/Oracle Exam 1Z0-1122-25 Dump.md'],
  'ai-practice': ['Nuevos/Practice Exam_ OCI AI Foundations Associate Certification.md'],
  'ai-skill': ['Nuevos/Skill Check_ OCI AI Foundations.md'],
  'ai-all': [
    'Nuevos/Oracle Exam 1Z0-1122-25 Dump.md',
    'Nuevos/Practice Exam_ OCI AI Foundations Associate Certification.md',
    'Nuevos/Skill Check_ OCI AI Foundations.md'
  ],
  'vector-pro': ['Nuevos/Oracle Exam 1Z0-184-25 Dump.md'],
  'all-exams': [
    'Nuevos/Oracle Exam 1Z0-1085-25 Dump.md',
    'Nuevos/Oracle Exam 1Z0-1122-25 Dump.md',
    'Nuevos/Practice Exam_ OCI AI Foundations Associate Certification.md',
    'Nuevos/Skill Check_ OCI AI Foundations.md',
    'Nuevos/Oracle Exam 1Z0-184-25 Dump.md'
  ]
};

function buildExternalComposite(key){
  const files = EXTERNAL_FILE_MAP[key]||[];
  const banks = files.map(f=> EXTERNAL_BANKS[f]||[]).flat();
  return dedupQuestions(banks);
}

function dedupQuestions(list){
  if(!ENABLE_DEDUP) return list.slice();
  const seen = new Map();
  const out = [];
  list.forEach(q=>{
    const norm = normalizeQuestionText(q.q);
    if(!seen.has(norm)){ seen.set(norm,true); out.push(q); }
  });
  return out;
}
function normalizeQuestionText(t){
  return t.toLowerCase().replace(/[^a-z0-9 ]+/g,'').replace(/\s+/g,' ').trim();
}

async function ensureExternalBanks(){
  const selected = examSelect?.value;
  if(!selected || selected==='none') return;
  const fileSets = {
    'oci-foundations': ['Nuevos/Oracle Exam 1Z0-1085-25 Dump.md'],
    'ai-oficial': ['Nuevos/Oracle Exam 1Z0-1122-25 Dump.md'],
    'ai-practice': ['Nuevos/Practice Exam_ OCI AI Foundations Associate Certification.md'],
    'ai-skill': ['Nuevos/Skill Check_ OCI AI Foundations.md'],
    'ai-all': [
      'Nuevos/Oracle Exam 1Z0-1122-25 Dump.md',
      'Nuevos/Practice Exam_ OCI AI Foundations Associate Certification.md',
      'Nuevos/Skill Check_ OCI AI Foundations.md'
    ],
    'vector-pro': ['Nuevos/Oracle Exam 1Z0-184-25 Dump.md'],
    'all-exams': [
      'Nuevos/Oracle Exam 1Z0-1085-25 Dump.md',
      'Nuevos/Oracle Exam 1Z0-1122-25 Dump.md',
      'Nuevos/Practice Exam_ OCI AI Foundations Associate Certification.md',
      'Nuevos/Skill Check_ OCI AI Foundations.md',
      'Nuevos/Oracle Exam 1Z0-184-25 Dump.md'
    ]
  };
  const files = fileSets[selected]||[];
  await Promise.all(files.map(f=> loadExternalMarkdown(f)));
}

async function loadExternalMarkdown(path){
  if(EXTERNAL_BANKS[path]) return;
  try {
    const txt = await fetch(path).then(r=> r.ok ? r.text() : '');
    EXTERNAL_BANKS[path] = parseMarkdownExam(txt, path);
    runSecurityScan(path, txt);
  } catch(e){ EXTERNAL_BANKS[path] = []; }
}

function parseMarkdownExam(md, source){
  if(!md) return [];
  const blocks = md.split(/\n#### /).slice(1).map(b=>'#### '+b.trim());
  const questions = [];
  const maxOfficialId = Math.max(0, ...QUESTIONS_OFFICIAL.map(q => q.id));
  let idCounter = maxOfficialId + 1; // IDs externos empiezan después del máximo oficial
  blocks.forEach(b=>{
    const lines = b.split(/\n/);
    const qLine = lines[0].replace(/^####\s*Q\.?\s*/,'').trim();
    const opts = [];
    let answerIndex = -1;
    lines.slice(1).forEach(l=>{
      const m = /^- \[(x| )\]\s*(.+)$/i.exec(l.trim());
      if(m){
        const correct = m[1].toLowerCase()==='x';
        const text = m[2].replace(/✅|\u2705/g,'').trim();
        opts.push(text);
        if(correct) answerIndex = opts.length-1;
      }
    });
    if(!qLine || !opts.length || answerIndex<0) return;
    const explanation = extractInlineExplanation(lines);
    questions.push({id:idCounter++, q:qLine, o:opts, a:answerIndex, e:explanation||'Sin explicación.', exam:source, raw:b});
  });
  return questions;
}

function extractInlineExplanation(lines){
  const expl = lines.filter(l=>/^>\s*/.test(l)).map(l=> l.replace(/^>\s*/,'').trim()).join(' ');
  return expl || '';
}

function runSecurityScan(path, txt){
  const findings = [];
  if(/<script\b/i.test(txt)) findings.push('Etiqueta <script>');
  const longBase64 = txt.match(/[A-Za-z0-9+\/]{80,}=*/g);
  if(longBase64) findings.push('Cadena base64 larga');
  if(/javascript:|onerror=|onload=/i.test(txt)) findings.push('Atributo JS inline');
  if(findings.length){ console.warn('Scan seguridad', path, findings); }
}

function startQuiz(){
  score = 0; wrong = []; skipped = []; marked = []; currentIndex = 0; answered = false; secondPass = false;
  const mode = modeSelect.value;
  let externalLoad = Promise.resolve();
  if(examSelect && examSelect.value !== 'none') externalLoad = ensureExternalBanks();
  externalLoad.then(()=>{
    let bank = getSelectedBank();
    if (mode === 'review'){
      const stored = JSON.parse(localStorage.getItem('lastWrongIds')||'[]');
      bank = bank.filter(q=> stored.includes(q.id));
      if (!bank.length){
        alert('No hay preguntas previas falladas para repaso en este banco.');
        return;
      }
    }
    order = [...bank];
    if (mode === 'random') shuffle(order);
    remainingSeconds = totalTimeSeconds;
    clearInterval(timerInterval);
    startTimer();
    quizEl.hidden = false;
    summaryEl.hidden = true;
    renderCurrent();
  });
}

function shuffle(arr){for(let i=arr.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[arr[i],arr[j]]=[arr[j],arr[i]];}}

function renderCurrent(){
  nextBtn.disabled = true; answered = false;
  const q = order[currentIndex];
  const answeredCount = currentIndex;
  const percent = ((answeredCount/order.length)*100).toFixed(1);
  const stats = `Correctas: ${score} | Incorrectas: ${wrong.length} | Skipped: ${skipped.length} | Marcadas: ${marked.length}`;
  progressTextEl.textContent = `Progreso: ${answeredCount}/${order.length} (${percent}%)${secondPass ? ' (2ª ronda)' : ''}`;
  progressFillEl.style.width = `${percent}%`;
  // Extended handling
  let extendedHTML = '';
  const extMode = extendedToggle ? extendedToggle.value : 'auto';
  if (EXTENDED_MAP && EXTENDED_MAP[q.id] && extMode !== 'off'){
    extendedHTML = `<div class="extended-block"><details open><summary>Enunciado extendido</summary>${EXTENDED_MAP[q.id]}</details></div>`;
  }
  questionContainer.innerHTML = `${extendedHTML}<div class="question-short">Q${q.id}: ${q.q}${q.exam?` <span class="badge exam-badge" title="Fuente externa">${shortExamName(q.exam)}</span>`:''}</div>`;
  optionsEl.innerHTML='';
  q.o.forEach((opt,idx)=>{
    const li=document.createElement('li');
    const btn=document.createElement('button');
    btn.textContent=`${String.fromCharCode(65+idx)}. ${opt}`;
    btn.addEventListener('click',()=>selectOption(idx));
    li.appendChild(btn); optionsEl.appendChild(li);
  });
  feedbackEl.className='feedback'; feedbackEl.textContent=stats;
}

function selectOption(idx){
  if (answered) return;
  const q = order[currentIndex];
  answered = true; nextBtn.disabled = false;
  if (idx === q.a){
    score++; feedbackEl.textContent='✔ Correcto'; feedbackEl.classList.add('correct');
  } else {
    wrong.push(q);
    feedbackEl.textContent=`✘ Incorrecto. Correcta: ${String.fromCharCode(65+q.a)}\n${q.e}`;
    feedbackEl.classList.add('incorrect');
  }
}

// Explicación y salto (X)
explainBtn.addEventListener('click',()=>{
  if (answered) return;
  const q = order[currentIndex];
  skipped.push(q); answered = true; nextBtn.disabled = false;
  feedbackEl.textContent=`Explicación: ${q.e} (Correcta: ${String.fromCharCode(65+q.a)})`;
  feedbackEl.className='feedback incorrect';
});
// Saltar sin explicación (S)
skipBtn.addEventListener('click',()=>{
  if (answered) return;
  const q = order[currentIndex];
  skipped.push(q); answered = true; nextBtn.disabled = false;
  feedbackEl.textContent=`Saltada.`;
  feedbackEl.className='feedback';
});
// Marcar (M)
markBtn.addEventListener('click',()=>{
  if (answered) return;
  const q = order[currentIndex];
  marked.push(q); answered = true; nextBtn.disabled = false;
  feedbackEl.textContent=`Marcada para segunda ronda.`;
  feedbackEl.className='feedback';
});

nextBtn.addEventListener('click',()=>{
  if (!answered) return;
  currentIndex++;
  if (currentIndex >= order.length){
    if (!secondPass && marked.length){
      secondPass = true;
      order = [...marked];
      currentIndex = 0;
      marked = [];
      renderCurrent();
    } else {
      finishQuiz();
    }
  } else {
    renderCurrent();
  }
});

function finishQuiz(){
  quizEl.hidden = true; summaryEl.hidden = false; clearInterval(timerInterval);
  const totalResponded = score + wrong.length + skipped.length;
  const pct = totalResponded?((score/totalResponded)*100).toFixed(1):'0.0';
  summaryEl.innerHTML = `<h2>Resumen</h2>
    <p>Correctas: ${score} | Incorrectas: ${wrong.length} | Skipped: ${skipped.length}</p>
    <p>Puntuación efectiva: <strong>${score}/${totalResponded}</strong> (${pct}%).</p>`;
  if (wrong.length){
    const ids = wrong.map(q=>q.id); localStorage.setItem('lastWrongIds', JSON.stringify(ids));
    const list = wrong.map(q=>`<li>Q${q.id} - ${q.q} <span class="badge">Correcta: ${String.fromCharCode(65+q.a)}</span></li>`).join('');
    summaryEl.innerHTML += `<h3>Incorrectas</h3><ul>${list}</ul><p>Guardadas para repaso.</p>`;
  } else {
    localStorage.setItem('lastWrongIds','[]'); summaryEl.innerHTML += '<p>¡Perfecto! Sin errores.</p>';
  }
  if (skipped.length){
    const listS = skipped.map(q=>`<li>Q${q.id} - ${q.q}</li>`).join('');
    summaryEl.innerHTML += `<h3>Skipped</h3><ul>${listS}</ul>`;
  }
  summaryEl.innerHTML += '<p><button id="restartBtn">Reiniciar</button></p>';
  document.getElementById('restartBtn').addEventListener('click',()=>{quizEl.hidden=true; summaryEl.hidden=true; score=0; wrong=[]; skipped=[]; marked=[];});
}

startBtn.addEventListener('click', startQuiz);
startBtn.focus();

// Cargar extended inicialmente
loadExtended();

function startTimer(){ updateTimerDisplay(); timerInterval=setInterval(()=>{remainingSeconds--; if(remainingSeconds<=0){remainingSeconds=0; updateTimerDisplay(); clearInterval(timerInterval); alert('Tiempo agotado. Se cerrará el examen.'); finishQuiz(); return;} updateTimerDisplay();},1000); }

function updateTimerDisplay(){
  const h=Math.floor(remainingSeconds/3600);
  const m=Math.floor((remainingSeconds%3600)/60);
  const s=remainingSeconds%60;
  const pad=v=>v.toString().padStart(2,'0');
  timeRemainingEl.textContent=`Tiempo restante: ${pad(h)}:${pad(m)}:${pad(s)}`;
  if (remainingSeconds<=600){ timeRemainingEl.id='timeWarning'; } else { timeRemainingEl.id=''; }
}
