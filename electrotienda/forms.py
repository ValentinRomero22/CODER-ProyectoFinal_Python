from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Formulario_registro_usuario(UserCreationForm):
    email = forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text='')
    password2: forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)
    help_texts = {
        "password1": None,
        "password2": None,
    }

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label = 'Modificar E-mail')
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text='')
    password2: forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)
    help_texts = {
        "password1": None,
        "password2": None,
    }

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}