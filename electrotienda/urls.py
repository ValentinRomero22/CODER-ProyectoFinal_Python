"""electrotienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unittest.mock import patch
from django.contrib import admin
from django.urls import path
from productos.views import *
from electrotienda.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name = 'index'),
    path("contacto/", contacto_view, name = "contacto"),

    #productos
    path('productos/', producto_view, name = 'productos'),
    path("productos/search-product/", search_product_view, name = "search_product_view"),
    path('productos/crear_producto/', CrearProducto.as_view() , name = 'crear_producto'),
    path('productos/detalle_producto/<int:pk>/', DetalleProducto.as_view(), name = 'detalle_producto'),
    path('productos/actualizar_producto/<int:pk>/', ActualizarProducto.as_view(), name = 'actualizar_producto'),
    path('productos/eliminar_producto/<int:pk>/', EliminarProducto.as_view(), name = 'eliminar_producto'),
    
    #categorias
    path('categorias/', categoria_view, name = 'categorias'),
    path('productos/crear_categoria/', CrearCategoria.as_view(), name = 'crear_categoria'),
    path('productos/detalle_categoria/<int:pk>/', DetalleCategoria.as_view(), name = 'detalle_categoria'),
    path('productos/actualizar_categoria/<int:pk>/', ActualizarCategoria.as_view(), name = 'actualizar_categoria'),
    path('productos/eliminar_categoria/<int:pk>/', EliminarCategoria.as_view(), name = 'eliminar_categoria'),

    #locales
    path('locales/', local_view, name = 'locales'),
    path('productos/crear_local/', CrearLocal.as_view(), name = 'crear_local'),
    path('productos/detalle_local/<int:pk>/', DetalleLocal.as_view(), name = 'detalle_local'),
    path('productos/actualizar_local/<int:pk>/', ActualizarLocal.as_view(), name = 'actualizar_local'),
    path('productos/eliminar_local/<int:pk>/', EliminarLocal.as_view(), name = 'eliminar_local'),

    #Usuarios
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', registro_view, name = 'register'),
]
