# Fase 1 – AskDoc

En la Fase 1 desarrollaremos un MVP que permita cargar documentos, extraer su contenido y responder consultas básicas. Se desglosa en seis bloques principales:

## 1. Gestión de carga de documentos

- **Funcionalidad**: Endpoint REST `/upload` en FastAPI para recibir archivos PDF, DOCX y TXT.  
- **Tareas técnicas**:  
  - Configurar `python-multipart` y `aiofiles` para subida y almacenamiento temporal.  
  - Validar tipo y tamaño de archivo (máx. 10 MB).  
- **Criterios de aceptación**:  
  - El endpoint devuelve un JSON con `{ document_id, filename }` al subir con éxito.  
  - Rechaza otros formatos con código HTTP 415.

## 2. Extracción y preprocesamiento de texto

- **Funcionalidad**: Leer contenido de los documentos y normalizarlo para posterior análisis.  
- **Tareas técnicas**:  
  - Implementar `DocumentParser` con `pdfplumber` para PDF y `python-docx` para DOCX.  
  - Limpiar saltos de línea excesivos y caracteres especiales.  
  - Dividir el texto en fragmentos de tamaño óptimo (p. ej. 1 000 tokens).  
- **Criterios de aceptación**:  
  - Cada `document_id` asocia una lista de fragmentos de texto.  
  - Registro de errores si falla el parseo.

## 3. Indexación y almacenamiento de vectores

- **Funcionalidad**: Generar embeddings de los fragmentos para búsquedas semánticas.  
- **Tareas técnicas**:  
  - Integrar con la API de OpenAI para obtener embeddings.  
  - Configurar una base de vectores local (FAISS) para indexar y consultar.  
  - Diseñar esquema de metadatos (`document_id`, `chunk_index`, `embedding`).  
- **Criterios de aceptación**:  
  - Embeddings generados y almacenados en FAISS sin errores.  
  - Capacidad de recobrar los top-k fragmentos más relevantes.

## 4. Búsqueda y consulta

- **Funcionalidad**: Endpoint `/query` que reciba una pregunta y devuelva respuesta generada por IA usando el contexto.  
- **Tareas técnicas**:  
  - Lógica de búsqueda por similitud sobre embeddings (k=5 por defecto).  
  - Concatenar fragmentos recuperados y enviar prompt a OpenAI Chat Completion.  
  - Estructurar la respuesta JSON con `{ answer, source_chunks }`.  
- **Criterios de aceptación**:  
  - Respuestas coherentes que citan fragmentos de origen.  
  - Latencia de consulta < 2 s en dataset de prueba (100 docs).

## 5. Interfaz de usuario básica

- **Funcionalidad**: Página web con formularios para subir documentos y realizar preguntas.  
- **Tareas técnicas**:  
  - Plantilla Jinja2 para formularios y visualización de respuestas.  
  - Llamadas AJAX a los endpoints `/upload` y `/query`.  
  - Manejo de estados (cargando, error, éxito).  
- **Criterios de aceptación**:  
  - El usuario puede subir un documento y hacer al menos una pregunta en la misma sesión.  
  - La UI muestra la respuesta e indicación de fragmentos usados.

## 6. Pruebas y validación

- **Funcionalidad**: Asegurar calidad y robustez de la Fase 1.  
- **Tareas técnicas**:  
  - Escribir pruebas unitarias con Pytest: carga, parseo, indexación y consulta.  
  - Simular carga de distintos formatos y preguntas frecuentes.  
  - Documentar resultados y errores detectados.  
- **Criterios de aceptación**:  
  - Cobertura de tests ≥ 80 % en módulos críticos.  
  - Informe de pruebas generado en CI.
