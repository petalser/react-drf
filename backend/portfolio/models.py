from django.db import models
from .validators import validate_file_size
from .utils import make_upload_path

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    before_image = models.ImageField(upload_to=make_upload_path("before"), validators=[validate_file_size])
    after_image = models.ImageField(upload_to=make_upload_path("after"), validators=[validate_file_size])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
