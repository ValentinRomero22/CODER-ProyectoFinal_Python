from multiprocessing import context
from shutil import register_unpack_format
from django.shortcuts import render
from django.http import HttpResponse

from productos.models import *
from productos.forms import product_form



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

def crear_producto(request):
    if request.method == 'GET':
        form = product_form
        context = {'form':form}
        return render(request, 'crear_producto.html', context = context)
    else:
        form = product_form(request.POST)
        if form.is_valid():
            new_product = Producto.objects.create(
                name = form.cleaned_data['name'],
                descripcion = form.cleaned_data['descripcion'],
                precio = form.cleaned_data['precio'],
                SKU = form.cleaned_data['SKU'],
                activo = form.cleaned_data['activo'],
            )
            context = {'new_product':new_product}
        return render(request, 'crear_producto.html', context = context)

def search_product_view(request):
    products = Producto.objects.filter(name = request.GET["search"])
    context = {"products":products}
    return render(request, "search_product.html", context = context)