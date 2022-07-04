from statistics import median_grouped
from django import forms
from productos.models import ImagenProducto

class product_form(forms.Form):
    name = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=100)
    precio = forms.FloatField()
    SKU = forms.CharField(max_length=20)
    activo = forms.BooleanField()

class AgregarImagen(forms.ModelForm):

    class Meta: 
        model = ImagenProducto
        fields = ['producto', 'imagen']