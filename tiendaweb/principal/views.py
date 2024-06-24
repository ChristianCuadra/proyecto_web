from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.db import IntegrityError


def index(request):
    return render(request , 'index.html')


def productos(request):
    return render(request , 'productos.html')

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
            try:
                user = User.objects.get(username=usuario)
                print(user)
            except User.DoesNotExist:
                user = None
            if user is None:
                return render(request,'login.html', {'mensaje': 'Usuario no existe'})
            else:

                if user is not None:
                    user = authenticate(request, username=usuario, password=password)
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
        usuario = get_object_or_404(User, username=username)
        if request.user.is_authenticated:
            user = request.user.first_name
            print(f"Esta validado {user}")
            if request.method == 'POST':
                user = User.objects.get(username=usuario)
                user.first_name = request.POST.get("nombre1")
                user.username = request.POST.get("usuario")
                user.last_name = request.POST.get("apellido1")
                user.email = request.POST.get("email1")
                
                user.save()

                return redirect('perfil') 
            elif request.method =='GET':
                return render(request, 'modificar.html')
    except Exception as error:
        print(error)


def eliminar_usuario(request, username):
    usuario = get_object_or_404(User, username=username)
    usuario.delete()
    return redirect('inicio')