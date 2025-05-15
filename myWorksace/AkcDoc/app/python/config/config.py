from pathlib import Path

UPLOAD_DIR = Path.cwd() / "app" / "python" / "resource" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}
MAX_FILE_SIZE_MB = 10
