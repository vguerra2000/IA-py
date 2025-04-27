# Proyecto “AskDoc” – Visión General

## 1. Nombre y Descripción
- **Nombre del proyecto**: AskDoc  
- **Descripción**: Gestor de documentos con IA para análisis y consulta inteligente de contenido. Inicialmente ofrecerá análisis de documentos cargados y responderá consultas basadas en ellos. 

## 2. Objetivos Fase 1
- Implementar carga y gestión básica de documentos.  
- Procesar y extraer información clave de cada documento.  
- Permitir al usuario realizar preguntas sobre el contenido y obtener respuestas generadas por IA.

## 3. Arquitectura inicial y estructura de carpetas
```plaintext
AskDoc/
├── app/             # Código de la aplicación web
│   ├── python/
│   │   ├── class/   # Modelos, clases de negocio
│   │   ├── config/  # Configuración y variables de entorno
│   │   └── page/    # Plantillas HTML y recursos estáticos
│   │       ├── index.html
│   │       └── __init__.py
│   ├── app.py       # Punto de entrada FastAPI
│   └── __init__.py
├── AskDoc.md        # Documentación general del proyecto
└── requirements.txt # Dependencias pip
```
## 4. Tech Stack
- Backend: FastAPI (uvicorn)
- Templates: Jinja2
- Manejo de archivos: python-multipart, aiofiles

## 5. Estado Actual
- Servidor FastAPI con endpoint / que devuelve index.html desde app/python/page/.
- Fichero requirements.txt inicializado con dependencias básicas.

## 6. Próximos pasos
- Diseñar el flujo de subida de documentos (endpoint y frontend).
- Integrar lectura y almacenamiento temporal de archivos con aiofiles.
- Investigar librería de IA para extracción de texto (por ejemplo, LangChain, OpenAI).
- Definir modelo de datos para almacenar metadatos de documentos.

## 7. Organización y Seguimiento
- A medida que avances, documentar:
- Nuevas funcionalidades añadidas.
- Cambios en la arquitectura y dependencias.
- Puntos abiertos y bloqueos.