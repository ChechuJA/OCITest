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
 * Carga un examen desde un archivo markdown
 */
async function loadExam(filePath) {
    try {
        const response = await fetch(filePath);
        if (!response.ok) {
            throw new Error(`Error al cargar ${filePath}: ${response.status}`);
        }
        const text = await response.text();
        const questions = parseMarkdownExam(text);
        
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
    module.exports = { parseMarkdownExam, loadExam, loadExamsCatalog };
}
