from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError


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

