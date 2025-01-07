from django import forms
from .models import MessageApp
from django.contrib.auth import get_user_model

class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageApp
        fields = ['content']
        
class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name'] 