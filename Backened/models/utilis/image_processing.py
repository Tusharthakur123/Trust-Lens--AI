import os

def save_image(file):
    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)
    path = os.path.join(upload_folder, file.filename)
    file.save(path)
    return path
