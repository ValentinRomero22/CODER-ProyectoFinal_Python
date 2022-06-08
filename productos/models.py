from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    SKU = models.CharField(max_length=20, unique=True)
    activo = models.BooleanField()

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

class Categoria(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

class Local(models.Model):
    direccion = models.CharField(max_length=50, unique=True)
    barrio = models.CharField(max_length=30)
    apertura = models.TimeField()
    cierre = models.TimeField()

    class Meta:
        verbose_name = 'local'
        verbose_name_plural = 'locales'
