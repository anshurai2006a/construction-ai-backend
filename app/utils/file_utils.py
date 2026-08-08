import os
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "uploads"

def ensure_upload_dir():
    os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_upload_file(file: UploadFile, subfolder: str = "") -> str:
    """Saves an uploaded file to disk with a unique name, returns the saved path."""
    ensure_upload_dir()
    folder = os.path.join(UPLOAD_DIR, subfolder) if subfolder else UPLOAD_DIR
    os.makedirs(folder, exist_ok=True)

    ext = os.path.splitext(file.filename)[1]
    unique_name = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(folder, unique_name)

    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)

    return file_path

def delete_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)