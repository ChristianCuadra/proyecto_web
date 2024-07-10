from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'inicio'),
    path('productos', views.productos, name= 'productos'),
    path('perfil', views.perfil, name= 'perfil'),
    path('vista_productos', views.vista_producto, name= 'vista_productos'),
    path('registro/',views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('salir/', views.salir, name="salir"),
    path('modificar/<str:username>/', views.modificar, name="modificar"),
    path('eliminar/<str:username>/', views.eliminar_usuario, name="eliminar"),
    path('administrar/', views.administrar_productos, name="administrar"),
    path('modificar_prod/<int:id_producto>/', views.modificar_prod, name='modprod'),
    path('agregar_productos/', views.agregar_productos, name='agregar'),
    path('eliminar_prod/<int:id_producto>/', views.eliminar_prod, name="eliminar_prod"),
    path('productos_vision/<int:id_producto>/', views.producto_vision, name= 'prodvis'),
    path('agregar_carrito/<int:id_producto>/', views.agregar_carrito, name='agregar_carrito'),
    path('mostrar_carrito/', views.mostrar_carrito, name='mostrar_carrito'),
    path('eliminar_item/<int:id>/', views.eliminar_item, name='eliminar_item'),
    path('informacion_pago/', views.informacion_pago, name='informacion_pago'),
    path('mostrar_pedido/',views.mostrar_pedido, name='mostrar_pedido' ),
    path('boleta/', views.boleta, name='boleta'),
    path('comprar_producto/<int:id_producto>/', views.comprar_producto, name='comprar_producto'),
    path('listar_producto/', views.listar_productos, name='listar_prod'),
    
]