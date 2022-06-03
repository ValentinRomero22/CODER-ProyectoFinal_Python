from multiprocessing import context
from shutil import register_unpack_format
from django.shortcuts import render
from productos.models import *

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def producto_view(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'productos.html', context = context)

def categoria_view(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'categorias.html', context = context)

def local_view(request):
    locales = Local.objects.all()
    context = {'locales': locales}
    return render(request, 'locales.html', context = context)