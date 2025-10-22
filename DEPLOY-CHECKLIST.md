# ✅ Checklist de Deploy a GitHub Pages

## Pre-Deploy

### Archivos Esenciales
- [x] `index.html` - Página principal
- [x] `quiz.js` - Lógica del quiz (con preguntas integradas)
- [x] `exam-loader.js` - Cargador de exámenes externos
- [x] `style.css` - Estilos
- [x] `exams-catalog.json` - Catálogo de exámenes
- [x] `README.md` - Documentación
- [x] `.gitignore` - Exclusiones de Git

### Carpetas
- [x] `Nuevos/` - 6 archivos markdown con 309 preguntas
- [x] `FUNCIONA/` - Backup del código base (opcional para deploy)

### Archivos Opcionales (no necesarios para producción)
- [ ] `test-loader.html` - Solo para testing local
- [ ] `process_exams.ps1` - Solo para desarrollo
- [ ] `process_exams.py` - Solo para desarrollo
- [ ] `IMPLEMENTACION.md` - Documentación técnica
- [ ] `Otros examenes/` - Archivos originales sin procesar

## Verificación de Funcionalidad

### Pruebas Locales
1. [ ] Abrir `index.html` en navegador
2. [ ] Verificar que carga sin errores de consola
3. [ ] Probar "Preguntas integradas" (75 preguntas)
   - [ ] Modo Aleatorio funciona
   - [ ] Modo Secuencial funciona
   - [ ] Modo Repasar falladas funciona
4. [ ] Probar "Exámenes externos"
   - [ ] Selector se llena con 6 exámenes
   - [ ] Cargar examen de AI (OCI AI Foundations)
   - [ ] Cargar examen de Database (MySQL)
   - [ ] Cargar examen de Infrastructure (OCI Foundations)
5. [ ] Verificar timer funciona (cuenta atrás)
6. [ ] Verificar que se pueden responder preguntas
7. [ ] Verificar explicaciones se muestran
8. [ ] Verificar resumen final aparece

### Verificación de Archivos
```powershell
# Ejecutar estos comandos para verificar
Get-ChildItem "c:\Github\Nuevos" | Measure-Object
# Debe mostrar: Count = 6

Get-Content "c:\Github\exams-catalog.json" | ConvertFrom-Json | Select-Object -ExpandProperty exams | Measure-Object
# Debe mostrar: Count = 6

Get-Content "c:\Github\index.html" | Select-String "exam-loader.js"
# Debe encontrar: <script src="exam-loader.js"></script>
```

## Deploy a GitHub

### Paso 1: Crear Repositorio
```bash
cd c:\Github
git init
git add .
git commit -m "Initial commit: Multi-exam quiz system"
```

### Paso 2: Conectar con GitHub
```bash
# Crear repo en GitHub web interface primero
git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
git branch -M main
git push -u origin main
```

### Paso 3: Activar GitHub Pages
1. Ir a repositorio en GitHub
2. Settings > Pages
3. Source: "Deploy from a branch"
4. Branch: `main` / `root`
5. Save
6. Esperar ~1 minuto

### Paso 4: Verificar Deploy
- [ ] Acceder a `https://TU-USUARIO.github.io/TU-REPO`
- [ ] Verificar que carga sin errores
- [ ] Probar funcionalidad básica
- [ ] Verificar que exámenes externos cargan

## Post-Deploy

### Verificaciones en Producción
- [ ] Abrir DevTools > Console (no debe haber errores rojos)
- [ ] Abrir DevTools > Network (verificar que archivos .md cargan)
- [ ] Probar en diferentes navegadores:
  - [ ] Chrome/Edge
  - [ ] Firefox
  - [ ] Safari (si disponible)
- [ ] Probar en móvil (responsive)
- [ ] Verificar localStorage funciona (modo repasar falladas)

### Métricas
```
Total archivos esenciales: 8
Total archivos markdown: 6
Peso total (sin Otros examenes): ~250 KB
Preguntas disponibles: 384
Tiempo de carga esperado: <2 segundos
```

## Troubleshooting

### Error: "Failed to load exam"
- **Causa**: CORS o ruta incorrecta
- **Solución**: Verificar que archivos están en `Nuevos/` y que rutas en `exams-catalog.json` son correctas

### Error: "exam-loader.js no está cargado"
- **Causa**: Orden de scripts incorrecto en HTML
- **Solución**: Verificar que `exam-loader.js` está ANTES de `quiz.js` en index.html

### Exámenes externos no aparecen
- **Causa**: `exams-catalog.json` no carga
- **Solución**: Verificar sintaxis JSON, usar validador online

### Timer no funciona
- **Causa**: Conflicto de variables
- **Solución**: Revisar consola, verificar que no hay errores JS

## Mejoras Opcionales Post-Deploy

### SEO y Metadata
```html
<!-- Añadir en <head> de index.html -->
<meta name="description" content="Sistema de quiz para certificaciones Oracle - 384 preguntas">
<meta name="keywords" content="Oracle, OCI, MySQL, Quiz, Certificación">
<meta property="og:title" content="OCI Quiz System">
<meta property="og:description" content="Sistema multi-examen para certificaciones Oracle">
```

### Analytics (Opcional)
- [ ] Google Analytics
- [ ] Plausible (privacidad-friendly)
- [ ] Simple Analytics

### Performance
- [ ] Minificar quiz.js (opcional)
- [ ] Comprimir CSS (opcional)
- [ ] Lazy load de archivos markdown grandes

## ✅ Checklist Mínimo para Deploy

**Para un deploy rápido, necesitas mínimo:**

1. ✅ `index.html`
2. ✅ `quiz.js`
3. ✅ `exam-loader.js`
4. ✅ `style.css`
5. ✅ `exams-catalog.json`
6. ✅ Carpeta `Nuevos/` con los 6 archivos .md
7. ✅ `README.md` (buena práctica)

**Total: 7 archivos + 1 carpeta = LISTO PARA DEPLOY**

---

## 🎉 ¡Listo para Producción!

Una vez completado este checklist, tu sistema estará funcionando perfectamente en GitHub Pages.

**URL final**: `https://tu-usuario.github.io/tu-repo/`

**Tiempo estimado de deploy**: 5-10 minutos
