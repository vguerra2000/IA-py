from fastapi import APIRouter, HTTPException
from pathlib import Path
from docx import Document
import PyPDF2

from app.python.config.config import UPLOAD_DIR
from app.python.utils.text_utils import TextProcessor

router = APIRouter(tags=["Extracción de texto"])

print(f"[EXTRACT] UPLOAD_DIR on import: {UPLOAD_DIR}")

def extract_text_from_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def extract_text_from_pdf(path: Path) -> str:
    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(path: Path) -> str:
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

@router.get("/extract/{file_id}", summary="Extrae y procesa el texto de un documento", response_model=dict)
async def extract_text(file_id: str):
    print(f"[EXTRACT] Intentando extraer texto para ID: {file_id}")
    print(f"[EXTRACT] UPLOAD_DIR: {UPLOAD_DIR}")

    matching_files = list(UPLOAD_DIR.glob(f"{file_id}.*"))
    print(f"[EXTRACT] Archivos encontrados: {matching_files}")

    if not matching_files:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")

    file_path = matching_files[0]
    ext = file_path.suffix.lower()
    print(f"[EXTRACT] Procesando archivo: {file_path} con extensión {ext}")

    # Extraer texto según extensión
    if ext == ".txt":
        raw_text = extract_text_from_txt(file_path)
    elif ext == ".pdf":
        raw_text = extract_text_from_pdf(file_path)
    elif ext == ".docx":
        raw_text = extract_text_from_docx(file_path)
    else:
        raise HTTPException(status_code=415, detail=f"Tipo de archivo no compatible: {ext}")

    print(f"[EXTRACT] Texto crudo extraído (longitud {len(raw_text)} caracteres)")

    # Limpieza del texto
    cleaned_text = TextProcessor.clean(raw_text)
    print(f"[EXTRACT] Texto limpio (longitud {len(cleaned_text)} caracteres)")

    # Fragmentación
    fragments = TextProcessor.fragment(cleaned_text)
    print(f"[EXTRACT] Número de fragmentos generados: {len(fragments)}")

    return {
        "document_id": file_id,
        "cleaned_text": cleaned_text,
        "fragments": fragments
    }
