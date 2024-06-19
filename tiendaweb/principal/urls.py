from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'inicio'),
    path('productos', views.productos, name= 'productos'),
    path('perfil', views.perfil, name= 'perfil'),
    path('vista_productos', views.vista_producto, name= 'vista_productos'),
    path('carrito', views.carrito, name= 'carrito'),
    path('registro/',views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('salir/', views.salir, name="salir")

]