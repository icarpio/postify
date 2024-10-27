from django import forms
from .models import Post
from cloudinary.forms import CloudinaryFileField

class PostForm(forms.ModelForm):
    
    image = CloudinaryFileField()
    class Meta:
        model = Post
        fields = '__all__'