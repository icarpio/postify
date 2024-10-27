from django.db import models
from cloudinary.models import CloudinaryField

class Post(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title