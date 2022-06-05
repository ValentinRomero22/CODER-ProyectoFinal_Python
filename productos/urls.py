from django.urls import path
from productos.views import producto_view, categoria_view, local_view, index_view, crear_producto

urlpatterns = [
    path('', index_view, name = 'index'),
    path('productos/', producto_view, name = 'productos'),
    path('categorias/', categoria_view, name = 'categorias'),
    path('locales/', local_view, name = 'locales'),
    path('productos/crear_producto/', crear_producto, name = 'crear_producto'),
]