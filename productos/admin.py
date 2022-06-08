from django.contrib import admin
from productos.models import Categoria, Local, Producto
from productos import *

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["name", "precio", "SKU"]
    
    
admin.site.register(Categoria)
admin.site.register(Local)
