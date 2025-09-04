from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    #TODO: file validation
    before_image = models.ImageField(upload_to="before/")
    #TODO: file validation
    after_image = models.ImageField(upload_to="after/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
