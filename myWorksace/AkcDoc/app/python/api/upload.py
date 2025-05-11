import os
import uuid
from fastapi import APIRouter, File, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse
from aiofiles import open as aio_open
from pathlib import Path
from app.python.config.config import UPLOAD_DIR, MAX_FILE_SIZE_MB, ALLOWED_EXTENSIONS

router = APIRouter(tags=["Carga de documentos"])
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload", summary="sube un documento PDF", response_model=dict, response_description="ID y nombre del archivo")
async def upload_document(file: UploadFile = File(...)):
    # 1) Validar extensión
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Formato no soportado: {ext}"
        )

    # 2) Leer un chunk para comprobar tamaño
    content = await file.read((MAX_FILE_SIZE_MB * 1024 * 1024) + 1)
    if len(content) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"Tamaño máximo permitido: {MAX_FILE_SIZE_MB} MB"
        )

    # 3) Guardar con UUID
    document_id = str(uuid.uuid4())
    dest_path = UPLOAD_DIR / f"{document_id}{ext}"
    async with aio_open(dest_path, "wb") as out_file:
        await out_file.write(content)

    # 4) Responder JSON
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "document_id": document_id,
            "filename": file.filename
        }
    )
