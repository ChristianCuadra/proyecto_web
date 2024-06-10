from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'inicio'),
    path('productos', views.productos, name= 'productos'),
    path('perfil', views.perfil, name= 'perfil'),
    path('vista_productos', views.vista_producto, name= 'vista_productos'),
    path('carrito', views.carrito, name= 'carrito')

]