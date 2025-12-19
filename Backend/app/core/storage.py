import os
import uuid
from fastapi import UploadFile

BASE_AUDIO_DIR = "storage/audio"


def ensure_storage_dir():
    os.makedirs(BASE_AUDIO_DIR, exist_ok=True)


def save_audio_file(file: UploadFile) -> str:
    """
    Saves uploaded audio file locally and returns file path
    """
    ensure_storage_dir()
    print("upload file=======",file)

    file_ext = os.path.splitext(file.filename)[-1]
    file_name = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(BASE_AUDIO_DIR, file_name)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
        print(file.file.read())

    return file_path
