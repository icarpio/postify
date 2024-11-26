from django import forms
from .models import Post, CommentPost
from cloudinary.forms import CloudinaryFileField

class PostForm(forms.ModelForm):
    image = CloudinaryFileField()
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']
        
class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Escribe tu comentario aquí...'}),
        label='Escribe tu comentario:',  # Si aún deseas usar un label
    )
    class Meta:
        model = CommentPost
        fields = ['text']
        
        