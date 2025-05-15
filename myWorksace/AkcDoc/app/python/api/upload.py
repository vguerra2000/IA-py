import os
import uuid
from pathlib import Path
from fastapi import APIRouter, File, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse
from app.python.config.config import UPLOAD_DIR, MAX_FILE_SIZE_MB, ALLOWED_EXTENSIONS

print("[DEBUG] __file__:", __file__)
print("[DEBUG] cwd():", Path.cwd())
print("[DEBUG] abs path:", os.path.abspath(__file__))

router = APIRouter(tags=["Carga de documentos"])

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post(
    "/upload",
    summary="Sube un documento PDF, DOCX o TXT",
    response_model=dict,
    response_description="ID y nombre del archivo"
)
async def upload_document(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix.lower()
    print(f"[UPLOAD] Recibido archivo: {file.filename} con extensión {ext}")

    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Formato no soportado: {ext}"
        )
    content = await file.read((MAX_FILE_SIZE_MB * 1024 * 1024) + 1)
    if len(content) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"Tamaño máximo permitido: {MAX_FILE_SIZE_MB} MB"
        )
    document_id = str(uuid.uuid4())
    dest_path = UPLOAD_DIR / f"{document_id}{ext}"
    print(f"[UPLOAD] UPLOAD_DIR: {UPLOAD_DIR}")
    print(f"[UPLOAD] Guardando archivo como: {dest_path}")

    with open(dest_path, "wb") as out_file:
        out_file.write(content)
    exists = Path(dest_path).exists()
    print(f"[UPLOAD] ¿Archivo existe realmente? {exists}")
    if not exists:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al guardar el archivo"
        )

    print(f"[UPLOAD] Archivo guardado correctamente con ID: {document_id}")

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "document_id": document_id,
            "filename": file.filename
        }
    )