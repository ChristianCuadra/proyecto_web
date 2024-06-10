from django.shortcuts import render

def index(request):
    return render(request , 'index.html')


def productos(request):
    return render(request , 'productos.html')

def perfil(request):
    return render(request , 'perfil_usuario.html')

def vista_producto(request):
    return render(request , 'vista_producto.html')

def carrito(request):
    return render(request , 'carrito.html')