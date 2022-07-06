from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from productos.models import *
from productos.forms import *

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

#Productos
def producto_view(request):
    productos = Producto.objects.all()

    if productos.exists():
        context = {'productos':productos}
    else:
        context = {'error': 'No se existen productos registrados.'}

    return render(request, 'productos.html', context = context)

def search_product_view(request):
    productos = Producto.objects.filter(name__icontains = request.GET["search"])
    
    if productos.exists():
        context = {"productos":productos}
    else:
        context = {'error': 'No se encontró ningún producto.'}

    return render(request, "search_product.html", context = context)

class CrearProducto(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'crear_producto.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_producto', kwargs = {'pk':self.object.pk})  

class DetalleProducto(DetailView):
    model = Producto
    template_name= 'detalle_producto.html'

class ActualizarProducto(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'actualizar_producto.html'
    fields = ['name', 'descripcion', 'precio', 'activo', 'imagen']

    def get_success_url(self):
        return reverse('detalle_producto', kwargs = {'pk':self.object.pk})

class EliminarProducto(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'

    def get_success_url(self):
        return reverse('productos')

#Categorias
def categoria_view(request):
    categorias = Categoria.objects.all()

    if categorias.exists():
        context = {'categorias':categorias}
    else:
        context = {'error': 'No existen categorías registradas.'}

    return render(request, 'categorias.html', context = context)

class CrearCategoria(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'crear_categoria.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_categoria', kwargs = {'pk':self.object.pk})  

class DetalleCategoria(DetailView):
    model = Categoria
    template_name= 'detalle_categoria.html'

class ActualizarCategoria(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = 'actualizar_categoria.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('detalle_categoria', kwargs = {'pk':self.object.pk})

class EliminarCategoria(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'eliminar_categoria.html'

    def get_success_url(self):
        return reverse('categorias')

#Locales
def local_view(request):
    locales = Local.objects.all()

    if locales.exists():
        context = {'locales': locales}
    else:
        context = {'error': 'No existen locales registrados.'}

    return render(request, 'locales.html', context = context)
    
class CrearLocal(LoginRequiredMixin, CreateView):
    model = Local
    template_name = 'crear_local.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_local', kwargs = {'pk':self.object.pk})  

class DetalleLocal(DetailView):
    model = Local
    template_name= 'detalle_local.html'

class ActualizarLocal(LoginRequiredMixin, UpdateView):
    model = Local
    template_name = 'actualizar_local.html'
    fields = ['direccion', 'barrio', 'apertura', 'cierre', 'imagen']

    def get_success_url(self):
        return reverse('detalle_local', kwargs = {'pk':self.object.pk})

class EliminarLocal(LoginRequiredMixin, DeleteView):
    model = Local
    template_name = 'eliminar_local.html'

    def get_success_url(self):
        return reverse('locales')