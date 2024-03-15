# backend/services/audio_service.py

import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'m4a', 'wav', 'mp3'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_audio_file(file, upload_folder):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return file_path
    return None

def delete_audio_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False