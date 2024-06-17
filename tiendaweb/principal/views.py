from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from django.db import IntegrityError


def index(request):
    return render(request , 'index.html')


def productos(request):
    return render(request , 'productos.html')

def perfil(request):
    usuario = get_user_model('username')
    nombre = get_user_model('first_name')
    apellido = get_user_model('last_name')
    correo = get_user_model('email')
    return render(request , 'perfil_usuario.html', {'usuario': usuario},{'nombre':nombre},{'apellido':apellido},{'correo':correo} )

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
            try:
                user = get_user_model(username=usuario)
            except user.DoesNotExist:
                return render(request, 'login.html', {'mensaje': 'Usuario no existe'})
            if user is None:
                user = None
            elif user is not None:
                user = authenticate(request, username=usuario, password=password)
                login(request, user)
                return render(request, 'perfil_usuario.html')
            else:
                return render(request, 'login.html',{'mensaje': 'Contraseña incorrecta'})
        elif request.method == 'GET':
            return render(request, 'login.html')
    except Exception as error:
        print(error)

