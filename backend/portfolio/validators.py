from django.core.exceptions import ValidationError
from PIL import Image

def validate_file_size(file):
    limit_mb = 5
    if file.size > limit_mb * 1024 * 1024:
        raise ValidationError(f"File too large. Max {limit_mb} MB.")
