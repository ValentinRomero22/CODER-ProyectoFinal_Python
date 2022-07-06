from email.policy import default
from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    SKU = models.CharField(max_length=20, unique=True)
    activo = models.BooleanField()
    category = models.ForeignKey("Categoria", on_delete=models.CASCADE, related_name="productos")
    imagen = models.ImageField(upload_to = 'productos', blank = True, null = True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        
    def __str__(self):
        return self.name

class Categoria(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        
    def __str__(self):
        return self.name

class Local(models.Model):
    direccion = models.CharField(max_length=50, unique=True)
    barrio = models.CharField(max_length=30)
    apertura = models.TimeField()
    cierre = models.TimeField()
    imagen = models.ImageField(upload_to = 'locales', blank = True, null = True, default="../static/sin_imagen.png")

    class Meta:
        verbose_name = 'local'
        verbose_name_plural = 'locales'
