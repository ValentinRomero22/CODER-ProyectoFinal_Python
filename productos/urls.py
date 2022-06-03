from django.urls import path
from views import *

urlpatterns = [
    path('', index_view, name = 'index'),
    path('productos/', producto_view, name = 'productos'),
    path('categorias/', categoria_view, name = 'categorias'),
    path('locales/', local_view, name = 'locales')
]