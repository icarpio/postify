from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', transformation=[
        {'width': 800, 'height': 600, 'crop': 'fill'}
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    