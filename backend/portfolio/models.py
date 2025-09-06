from django.db import models
from .validators import validate_file_size
from .utils import UploadToPath

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    before_image = models.ImageField(upload_to=UploadToPath("before"), validators=[validate_file_size])
    after_image = models.ImageField(upload_to=UploadToPath("after"), validators=[validate_file_size])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
