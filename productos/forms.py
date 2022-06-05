from django import forms

class product_form(forms.Form):
    name = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=100)
    precio = forms.FloatField()
    SKU = forms.CharField(max_length=20)
    activo = forms.BooleanField()