import uuid

class UploadToPath:
    def __init__(self, folder):
        self.folder = folder

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        return f"{self.folder}/{uuid.uuid4()}.{ext}"
