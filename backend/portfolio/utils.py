import uuid

def make_upload_path(folder):
    def upload_to(instance, filename):
        ext = filename.split('.')[-1]
        return f"{folder}/{uuid.uuid4()}.{ext}"
    return upload_to
