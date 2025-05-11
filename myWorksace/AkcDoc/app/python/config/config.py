from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # .../app
UPLOAD_DIR = BASE_DIR / "uploads"
MAX_FILE_SIZE_MB = 10
ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}