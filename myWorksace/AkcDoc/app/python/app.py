from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path
from app.python.api.upload import router as upload_router

app = FastAPI(title="AskDoc")

app.include_router(upload_router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # __file__ apunta a .../app/python/app.py
    base_dir = Path(__file__).resolve().parent  # .../app/python
    file_path = base_dir / "page" / "index.html"
    return FileResponse(str(file_path), media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn app.python.app:app --reload --host 127.0.0.1 --port 8000