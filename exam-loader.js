// exam-loader.js - Módulo para cargar exámenes desde archivos markdown

/**
 * Parsea un archivo markdown de examen y extrae las preguntas
 * Formato esperado:
 * #### Q1. [pregunta]
 * - [ ] opción incorrecta
 * - [x] opción correcta ✅
 * > explicación (opcional)
 */
function parseMarkdownExam(markdownText) {
    const questions = [];
    const lines = markdownText.split('\n');
    
    let currentQuestion = null;
    let currentOptions = [];
    let correctIndex = -1;
    let explanation = '';
    let questionId = 1;
    
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();
        
        // Nueva pregunta
        if (line.startsWith('#### Q')) {
            // Guardar pregunta anterior si existe
            if (currentQuestion && currentOptions.length > 0) {
                questions.push({
                    id: questionId++,
                    q: currentQuestion,
                    o: currentOptions,
                    a: correctIndex,
                    e: explanation || 'Sin explicación disponible'
                });
            }
            
            // Iniciar nueva pregunta
            currentQuestion = line.replace(/^#### Q\d+\.\s*/, '').trim();
            currentOptions = [];
            correctIndex = -1;
            explanation = '';
        }
        // Opción de respuesta
        else if (line.startsWith('- [')) {
            const isCorrect = line.startsWith('- [x]') || line.startsWith('- [X]');
            const optionText = line.replace(/^- \[[xX ]?\]\s*/, '')
                                   .replace(/✅/g, '')
                                   .replace(/❌/g, '')
                                   .trim();
            
            if (isCorrect) {
                correctIndex = currentOptions.length;
            }
            currentOptions.push(optionText);
        }
        // Explicación (blockquote)
        else if (line.startsWith('>')) {
            explanation += line.replace(/^>\s*/, '').trim() + ' ';
        }
    }
    
    // Guardar última pregunta
    if (currentQuestion && currentOptions.length > 0) {
        questions.push({
            id: questionId++,
            q: currentQuestion,
            o: currentOptions,
            a: correctIndex,
            e: explanation.trim() || 'Sin explicación disponible'
        });
    }
    
    return questions;
}

/**
 * Parsea un examen en formato JSON.
 * Formato esperado (por pregunta):
 * {
 *   id: number,
 *   question: string,
 *   answers: [{ key: "A", text: "..." }, ...],
 *   correctKeys: ["B", "C"]
 * }
 */
function parseJsonExam(jsonData) {
    if (!Array.isArray(jsonData)) return [];

    return jsonData
        .map((item, index) => {
            const questionText = (item && typeof item.question === 'string') ? item.question.trim() : '';
            const answers = Array.isArray(item && item.answers) ? item.answers : [];
            const correctKeys = Array.isArray(item && item.correctKeys) ? item.correctKeys : [];

            const orderedAnswers = answers
                .map(a => ({
                    key: (a && a.key != null) ? String(a.key).trim() : '',
                    text: (a && typeof a.text === 'string') ? a.text.trim() : ''
                }))
                .filter(a => a.key && a.text)
                .sort((a, b) => a.key.localeCompare(b.key));

            const options = orderedAnswers.map(a => a.text);

            const keyToIndex = new Map(orderedAnswers.map((a, i) => [a.key.toUpperCase(), i]));
            const correctIndices = correctKeys
                .map(k => keyToIndex.get(String(k).trim().toUpperCase()))
                .filter(i => typeof i === 'number');

            // a puede ser number (una correcta) o array (múltiples correctas)
            let a;
            if (correctIndices.length <= 1) {
                a = (correctIndices.length === 1) ? correctIndices[0] : -1;
            } else {
                a = Array.from(new Set(correctIndices)).sort((x, y) => x - y);
            }

            return {
                id: (item && typeof item.id === 'number') ? item.id : (index + 1),
                q: questionText,
                o: options,
                a,
                e: (item && typeof item.explanation === 'string' && item.explanation.trim())
                    ? item.explanation.trim()
                    : 'Sin explicación disponible'
            };
        })
        .filter(q => q.q && Array.isArray(q.o) && q.o.length);
}

/**
 * Carga un examen desde un archivo markdown
 */
async function loadExam(filePath) {
    try {
        const response = await fetch(filePath);
        if (!response.ok) {
            throw new Error(`Error al cargar ${filePath}: ${response.status}`);
        }
        const isJson = /\.json(\?.*)?$/i.test(filePath);
        const questions = isJson
            ? parseJsonExam(await response.json())
            : parseMarkdownExam(await response.text());
        
        console.log(`✅ Cargado: ${filePath} (${questions.length} preguntas)`);
        return questions;
    } catch (error) {
        console.error(`❌ Error cargando ${filePath}:`, error);
        return [];
    }
}

/**
 * Carga el catálogo de exámenes
 */
async function loadExamsCatalog() {
    try {
        const response = await fetch('exams-catalog.json');
        if (!response.ok) {
            throw new Error(`Error al cargar catálogo: ${response.status}`);
        }
        const catalog = await response.json();
        console.log(`✅ Catálogo cargado: ${catalog.exams.length} exámenes disponibles`);
        return catalog;
    } catch (error) {
        console.error('❌ Error cargando catálogo:', error);
        return null;
    }
}

// Exportar funciones
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { parseMarkdownExam, parseJsonExam, loadExam, loadExamsCatalog };
}
