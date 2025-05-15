"""
Script de prueba: prueba.py
Sube un documento, extrae texto limpio y fragmentos.
"""
import requests
import os

def main():
    # Configuración de endpoints
    BASE_URL = "http://127.0.0.1:8000"
    UPLOAD_ENDPOINT = f"{BASE_URL}/api/upload"
    EXTRACT_ENDPOINT = f"{BASE_URL}/api/extract/{{}}"

    # Ruta al archivo local que vamos a subir
    file_path = r"C:\Users\TECDATA ENGINEERING\Documents\workspace IA-py\IA-py\myWorksace\AkcDoc\app\python\resource\CV 2025 victor guerra rubio.pdf"
    if not os.path.exists(file_path):
        print(f"Error: no existe el archivo: {file_path}")
        return

    # 1) Subida de archivo
    print(f"Subiendo archivo: {file_path}")
    with open(file_path, "rb") as f:
        files = {"file": f}
        resp = requests.post(UPLOAD_ENDPOINT, files=files)

    print(f"Upload status: {resp.status_code}")
    if resp.status_code != 201:
        print("Error en la subida:", resp.status_code, resp.text)
        return

    data = resp.json()
    document_id = data.get("document_id")
    print(f"Documento subido correctamente. ID: {document_id}\n")

    # 2) Extracción y procesamiento
    extract_url = EXTRACT_ENDPOINT.format(document_id)
    print(f"Extrayendo texto de: {extract_url}")
    resp2 = requests.get(extract_url)
    print(f"Extract status: {resp2.status_code}")

    if resp2.status_code != 200:
        print("Error al extraer texto:", resp2.status_code, resp2.text)
        return

    result = resp2.json()
    cleaned_text = result.get("cleaned_text", "")
    fragments = result.get("fragments", [])

    # 3) Mostrar resultados
    print("\n--- Texto limpio (primeros 500 caracteres) ---")
    print(cleaned_text[:500])

    print(f"\n--- Número de fragmentos: {len(fragments)} ---")
    # Mostrar primeros 3 fragmentos
    for i, frag in enumerate(fragments[:3], start=1):
        print(f"\n--- Fragmento {i} (longitud {len(frag)}) ---")
        print(frag)
    if len(fragments) > 3:
        print("\n... (más fragmentos disponibles) ...")

if __name__ == "__main__":
    main()
