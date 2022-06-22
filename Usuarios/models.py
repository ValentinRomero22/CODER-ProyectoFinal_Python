from django.db import models
from django.contrib.auth.models import User

class Perfil_Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_usuario')
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
