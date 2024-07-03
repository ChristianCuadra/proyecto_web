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
    path('salir/', views.salir, name="salir"),
    path('modificar/<str:username>/', views.modificar, name="modificar"),
    path('eliminar/<str:username>/', views.eliminar_usuario, name="eliminar"),
    path('administrar/', views.administrar_productos, name="administrar"),
    path('modificar_prod/<int:id_producto>/', views.modificar_prod, name='modprod'),
    path('agregar_productos/', view.agregar_productos, name='agregar')
]