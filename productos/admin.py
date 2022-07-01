from tkinter import Image
from django.contrib import admin
from productos.models import Categoria, Local, Producto, ImagenProducto
from productos import *

# Register your models here.
class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["name", "precio", "SKU", "activo", "category"]
    inlines = [ImagenProductoAdmin]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["name"]

class LocalAdmin(admin.ModelAdmin):
    list_display = ["direccion", "barrio", "apertura", "cierre"]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Local, LocalAdmin)
