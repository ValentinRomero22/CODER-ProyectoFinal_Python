""" from django.urls import path
from productos.views import producto_view, categoria_view, local_view, index_view, CrearProducto, DetalleProducto

urlpatterns = [
    path('', index_view, name = 'index'),
    path('productos/', producto_view, name = 'productos'),
    path('productos/crear_producto/', CrearProducto.as_view() , name = 'crear_producto'),
    path('productos/detalle_producto/<int:id>', DetalleProducto.as_view(), name = 'detalle_producto'),
    path('categorias/', categoria_view, name = 'categorias'),
    path('locales/', local_view, name = 'locales'),
] """