from django.contrib import admin
from .models import Productos, Carrito, CarritoItem, InformacionUsuario
# Register your models here.
admin.site.register(Productos)
admin.site.register(Carrito)
admin.site.register(CarritoItem)
admin.site.register(InformacionUsuario)
