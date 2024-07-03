from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.db import IntegrityError
from .models import Productos


def productos(request):
    datos = Productos.objects.all()
    contexto={'Productos': datos}
    return render(request,'productos.html', contexto)


def index(request):
    datos = Productos.objects.all()
    contexto={'Productos': datos}
    return render(request,'index.html', contexto)


def perfil(request):
    usuario = request.user.username
    nombre = request.user.first_name
    apellido = request.user.last_name
    correo = request.user.email
    return render(request , 'perfil_usuario.html', {'usuario': usuario,'nombre':nombre,'apellido':apellido,'correo':correo} )

def vista_producto(request):
    return render(request , 'vista_producto.html')

def carrito(request):
    return render(request , 'carrito.html')



def registro(request):
    try:
        if request.method == "POST":
            nombre = request.POST.get('nombre1')
            apellido = request.POST.get('apellido1')
            usuario = request.POST.get('usuario')
            correo = request.POST.get('email1')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if nombre=="" or apellido=="" or usuario=="" or correo=="" or password1=="" or password2=="": 
                return render(request, 'registro.html', {'mensaje': 'Los campos no deben estar vacios'})
            else:
                if password1==password2:
                    user = User.objects.create_user(first_name=nombre, last_name=apellido, username=usuario, email=correo, password=password1)
                    user.save()
                    return render(request, 'index.html', {'mensaje': 'Usuario creado correctamente'})
                else:
                    return render(request, 'registro.html', {'mensaje': 'Las contraseñas no coinciden'})
        elif request.method=='GET':
            return render(request, 'registro.html')

    except IntegrityError:
        return render(request,'registro.html',{'mensaje':'Usuario ya existe'})
    except ValueError:
        return render(request,'registro.html',{'mensaje':'Dato no válido'})
    except Exception as error:
        print(error)

def iniciar_sesion(request):
    try:
        if request.method == "POST":
            usuario = request.POST.get('usuario')
            password = request.POST.get('password1')
            User = get_user_model()
            try:
                user = User.objects.get(username=usuario)
            except User.DoesNotExist:
                user = None
            if user is None:
                return render(request,'login.html', {'mensaje': 'El usuario ingresado no existe'})
            else:
                user = authenticate(request, username=usuario, password=password)
                if user is not None:
                    login(request, user)
                    return render(request, 'perfil_usuario.html')
                else:
                    return render(request, 'login.html',{'mensaje': 'Contraseña incorrecta'})
        elif request.method == 'GET':
            return render(request, 'login.html')
    except Exception as error:
        print(error)


def salir(request):
    logout(request)
    return render(request,'index.html')



def modificar(request, username):
    try:
        user = get_object_or_404(User, username=username)
        nombre = request.POST.get('nombre1')
        apellido = request.POST.get('apellido1')
        usuario = request.POST.get('usuario')
        correo = request.POST.get('email1')
        password1 = request.POST.get('password1')
        if request.user.is_authenticated:
            if request.method == 'POST':
                if nombre:
                    user.first_name = nombre
                    user.save()
                if apellido:
                    user.last_name = apellido
                    user.save()
                if usuario:
                    user.username = usuario
                    user.save()
                if correo:
                    user.email = correo
                    user.save()
                return redirect('perfil')
            return render(request, 'modificar.html')
    except Exception as error:
        print(error)


def eliminar_usuario(request, username):
    usuario = get_object_or_404(User, username=username)
    usuario.delete()
    return redirect('inicio')



def administrar_productos(request):
    datos = Productos.objects.all()
    contexto={'Productos': datos}
    return render(request, 'productos_admin.html', contexto)


def modificar_prod(request, id_producto):
    try:
        producto = get_object_or_404(Productos, id_producto=id_producto)
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        if request.method == 'POST':
            if nombre:
                producto.nombre = nombre
                producto.save()
            if categoria:
                producto.categoria = categoria
                producto.save()
            if precio:
                producto.precio = precio
                producto.save()
            if descripcion:
                producto.descripcion = descripcion
                producto.save()
            return redirect('administrar')
        elif request.method == 'GET':
            return render(request, 'modificar_prod.html')
    except Exception as error:
        print(error)


def agregar_productos(request):
        try:
        if request.method == "POST":
            id_prod = request.POST.get('id')
            nombre = request.POST.get('nombre')
            categoria = request.POST.get('categoria')
            precio = request.POST.get('precio')
            descripcion = request.POST.get('descripcion')
            if id_prod=="" or nombre=="" or categoria=="" or precio=="" or descripcion=="": 
                return render(request, 'agregar_prod.html', {'mensaje': 'Los campos no deben estar vacios'})
            else:
                    producto = Productos.objects.create_user(nombre=nombre, categoria=categoria, id_producto=id_prod, precio=precio, descripcion=descripcion)
                    producto.save()
                    return render(request, 'productos_admin.html', {'mensaje': 'Producto creado correctamente'})
        elif request.method=='GET':
            return render(request, 'registro.html')

    except IntegrityError:
        return render(request,'registro.html',{'mensaje':'Producto ya existe'})
    except ValueError:
        return render(request,'registro.html',{'mensaje':'Dato no válido'})
    except Exception as error:
        print(error)