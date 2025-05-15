import json
from pathlib import Path
from typing import Dict, List

FRAGMENTS_FILE = Path.cwd() / "app" / "python" / "resources" / "storage" / "fragments.json"


def load_all_fragments() -> Dict[str, List[str]]:
    """Carga y devuelve el dict completo de fragments desde el JSON."""
    FRAGMENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not FRAGMENTS_FILE.exists():
        FRAGMENTS_FILE.write_text("{}", encoding="utf-8")
    try:
        with FRAGMENTS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            else:
                return {}
    except json.JSONDecodeError:
        FRAGMENTS_FILE.write_text("{}", encoding="utf-8")
        return {}
    except Exception as e:
        print(f"[STORAGE] Error al cargar fragments.json: {e}")
        return {}


def save_fragments(data: Dict[str, List[str]]) -> None:
    """Sobrescribe el JSON con el dict completo."""
    FRAGMENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        with FRAGMENTS_FILE.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[STORAGE] Error al guardar fragments.json: {e}")
