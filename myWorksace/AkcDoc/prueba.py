import requests

## prueba de update file
url = "http://127.0.0.1:8000/api/upload"
files = {
    "file": open(r"C:\Users\TECDATA ENGINEERING\Documents\workspace IA-py\IA-py\myWorksace\AkcDoc\CV 2025 victor guerra rubio.pdf", "rb")
}
resp = requests.post(url, files=files)
print(resp.status_code)
print(resp.json())
