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
];

// Referencias DOM
const bankSelect = document.getElementById('bankSelect');
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

function openModal(mdFile = 'documentacion.md'){
  docsModal.hidden = false;
  docsModal.setAttribute('aria-hidden','false');
  // Load documentation (fetch local markdown)
  fetch(mdFile)
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
openDocsBtn?.addEventListener('click', () => openModal('documentacion.md'));
closeModalBtn?.addEventListener('click', closeModal);
docsModal?.addEventListener('click', e=>{ if(e.target === docsModal) closeModal(); });
document.addEventListener('keydown', e=>{ if(e.key==='Escape' && docsModal.getAttribute('aria-hidden')==='false') closeModal(); });

// Event listeners for navigation links
const readmeLink = document.getElementById('readmeLink');
const documentacionLink = document.getElementById('documentacionLink');
const bancoOficialLink = document.getElementById('bancoOficialLink');
readmeLink?.addEventListener('click', (e) => { e.preventDefault(); openModal('README.md'); });
documentacionLink?.addEventListener('click', (e) => { e.preventDefault(); openModal('documentacion.md'); });
bancoOficialLink?.addEventListener('click', (e) => { e.preventDefault(); openModal('preguntas_oficiales.md'); });

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

function getSelectedBank(){
  if (bankSelect.value === 'official') return [...QUESTIONS_OFFICIAL];
  if (bankSelect.value === 'optional') return [...QUESTIONS_OPTIONAL];
  return [...QUESTIONS_OFFICIAL, ...QUESTIONS_OPTIONAL];
}

function startQuiz(){
  score = 0; wrong = []; skipped = []; marked = []; currentIndex = 0; answered = false; secondPass = false;
  const mode = modeSelect.value;
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
  questionContainer.textContent = `Q${q.id}: ${q.q}`;
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

function startTimer(){ updateTimerDisplay(); timerInterval=setInterval(()=>{remainingSeconds--; if(remainingSeconds<=0){remainingSeconds=0; updateTimerDisplay(); clearInterval(timerInterval); alert('Tiempo agotado. Se cerrará el examen.'); finishQuiz(); return;} updateTimerDisplay();},1000); }

function updateTimerDisplay(){
  const h=Math.floor(remainingSeconds/3600);
  const m=Math.floor((remainingSeconds%3600)/60);
  const s=remainingSeconds%60;
  const pad=v=>v.toString().padStart(2,'0');
  timeRemainingEl.textContent=`Tiempo restante: ${pad(h)}:${pad(m)}:${pad(s)}`;
  if (remainingSeconds<=600){ timeRemainingEl.id='timeWarning'; } else { timeRemainingEl.id=''; }
}
