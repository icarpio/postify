from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Username",  # Cambia la etiqueta
        help_text="Required",
        widget=forms.TextInput(attrs={'placeholder': 'Tu nombre de usuario'})
    )
    password1 = forms.CharField(
        label="Password",
        help_text="Debe tener al menos 8 caracteres, no ser común y no ser completamente numérica.",
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        help_text="Repeat Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']  # Campos del formulario
        
    
