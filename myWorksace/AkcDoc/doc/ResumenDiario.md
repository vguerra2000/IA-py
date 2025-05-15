# Resumen Diario – 11 de Mayo de 2025

Hoy (11/05/2025) hemos implementado la **Gestión de carga de documentos**, creando el endpoint `POST /api/upload` en FastAPI con validaciones de extensión (`.pdf`, `.docx`, `.txt`) y tamaño (10 MB máximo), y guardando los archivos en la carpeta `uploads/` con identificadores UUID. También instalamos y configuramos `python-multipart` y `aiofiles`, organizamos la estructura de paquetes (`api/`, `config/` y registros de enrutamiento en `app.py`) y probamos la ruta con Swagger UI, `curl.exe` e `Invoke-RestMethod` en PowerShell.  

**Próximo paso para mañana**: empezar la **Extracción y preprocesamiento de texto** (lectura de PDF/DOCX, limpieza y fragmentado de contenido).  

**Archivos creados hoy**:
- `app/python/api/upload.py`  
- `app/python/config/config.py`  
- Carpeta `uploads/` (destino de almacenamiento)

# Resumen Diario – 15 de Mayo de 2025

**Hoy (15/05/2025) hemos avanzado en la Fase 1, bloque 2 “Extracción y preprocesamiento de texto”:**

- Creamos el módulo **`text_utils.py`** con la clase `TextProcessor` que:
  - Normaliza saltos de línea, espacios y caracteres de control (`clean`).
  - Fragmenta el texto en bloques de ~1 000 caracteres con solapamiento configurable (`fragment`).

- Actualizamos **`extract.py`** para que, tras extraer el texto crudo de PDF/DOCX/TXT:
  1. Limpie el texto con `TextProcessor.clean`.
  2. Lo fragmente con `TextProcessor.fragment`.
  3. Devuelva en la respuesta JSON tanto `cleaned_text` como la lista de `fragments`.

- Introdujimos persistencia de fragments en JSON:
  - Creamos **`storage_utils.py`** con `load_all_fragments()` y `save_fragments()`.
  - Tras fragmentar en el endpoint de extracción, cargamos el fichero `fragments.json`, actualizamos la entrada bajo la clave `document_id` y lo guardamos de nuevo.

**Archivos creados/actualizados hoy**

- `app/python/utils/text_utils.py`
- `app/python/utils/storage_utils.py`
- `app/python/api/extract.py`
- `app/python/storage/fragments.json`

---

**Próximo paso para mañana (16/05/2025):**

terminar y probar el storage

### 3. Indexación y almacenamiento de vectores

- Integrar la API de OpenAI para generar embeddings de cada fragmento.
- Configurar un índice FAISS local para almacenar y consultar esos embeddings.
- Definir esquema de metadatos (`document_id`, `chunk_index`, `embedding`).
- Verificar que podemos recuperar los top-k fragmentos más relevantes.



