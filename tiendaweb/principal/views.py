from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.db import IntegrityError
from django.db.models import Q
from .models import Productos, Carrito, CarritoItem, InformacionUsuario
from django.http import JsonResponse


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
    except IntegrityError:
        return render(request, 'modificar.html',{'mensaje':'Nombre de usuario ya existe'})
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
        imagen  = request.FILES.get('imagen')
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
            if imagen:
                producto.imagen = imagen
                producto.save()
            return redirect('administrar')
        elif request.method == 'GET':
            return render(request, 'modificar_prod.html')
    except Exception as error:
        print(error)



def agregar_productos(request):
    if request.method == "POST":
        try:
                id_prod = request.POST.get('id')
                nombre = request.POST.get('nombre')
                categoria = request.POST.get('categoria')
                precio = request.POST.get('precio')
                descripcion = request.POST.get('descripcion')
                imagen  = request.FILES.get('imagen')
                if id_prod=="" or nombre=="" or categoria=="" or precio=="" or descripcion=="" or imagen is None: 
                    return render(request, 'agregar_prod.html', {'mensaje': 'Los campos no deben estar vacios'})
                else:
                        producto = Productos.objects.create(nombre=nombre, categoria=categoria, id_producto=id_prod, precio=precio, descripcion=descripcion, imagen=imagen)
                        producto.save()
                        return redirect('administrar')

        except IntegrityError:
            return render(request,'agregar_prod.html',{'mensaje':'Producto ya existe'})
        except ValueError:
            return render(request,'agregar_prod.html',{'mensaje':'Dato no válido'})
        except Exception as error:
            print(error)
    
    elif request.method=='GET':
            return render(request, 'agregar_prod.html')
        
def eliminar_prod(request, id_producto):
    producto = get_object_or_404(Productos, id_producto=id_producto)
    producto.delete()
    return redirect('administrar')

def producto_vision(request, id_producto):
    producto = get_object_or_404(Productos, id_producto=id_producto)
    return render(request, 'vista_producto.html', {'producto': producto})


#def listar_productos(request):
    #busqueda = request.GET.get('buscar')
    #producto = Productos.objects.all()
    #contexto={'Productos': producto}
    
    #if busqueda:
     #   producto = Productos.objects.filter(
      #      Q(nombre__icontains = busqueda ) |
       #     Q(categoria__icontains = busqueda) |
        #    Q(precio__icontains = busqueda)
        #).distinct()
    #else:
     #   producto = Productos.objects.all()
    
    #return render (request, 'navbar.html', contexto)
    
    
def agregar_carrito(request, id_producto):
    producto = get_object_or_404(Productos, id_producto=id_producto)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not created:
        carrito_item.cantidad += 1
        return redirect('mostrar_carrito')
    
    carrito_item.save()
    
    return redirect('mostrar_carrito')

def mostrar_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    carrito_item = CarritoItem.objects.filter(carrito=carrito)
    total_carrito = sum(item.producto.precio * item.cantidad for item in carrito_item)
    
    return render(request, 'carrito.html', {'carrito_item':carrito_item, 'total_carrito':total_carrito})

def eliminar_item(request, id):
    carrito_item= get_object_or_404(CarritoItem, id=id)
    carrito_item.delete()
    return redirect('mostrar_carrito')

def informacion_pago(request):
        try:
            
            informacion = InformacionUsuario.objects.get(usuario=request.user)
            return redirect('mostrar_pedido')
        
        except InformacionUsuario.DoesNotExist:
            if request.method == "POST":
                usuario = request.user
                tarjeta = request.POST.get('tarjeta')
                mes = request.POST.get('mes')
                anno = request.POST.get('año')
                codigo = request.POST.get('codigo')
                direccion = request.POST.get('direccion')
                if tarjeta=="" or mes=="" or anno=="" or codigo=="" or  direccion =="" : 
                    return render(request, 'pago.html', {'mensaje': 'Los campos no deben estar vacios'})
                else:
                        informacion = InformacionUsuario.objects.create(usuario= usuario, nro_tarjeta=tarjeta, codigo_seg=codigo, fecha_venc_mes=mes, fecha_venc_anno=anno, direccion=direccion)
                        informacion .save()
                        return redirect('mostrar_pedido')
            elif request.method=='GET':
                return render(request, 'pago.html')

        except IntegrityError:
            return render(request,'pago.html',{'mensaje':'Información ya agregada'})
        except ValueError:
            return render(request,'pago.html',{'mensaje':'Dato no válido'})
        except Exception as error:
            print(error)


def mostrar_pedido(request):
    informacion = get_object_or_404(InformacionUsuario, usuario=request.user)
    usuario = get_object_or_404(User, username=request.user.username)
    carrito = Carrito.objects.get(usuario=request.user)
    carrito_item = CarritoItem.objects.filter(carrito=carrito)
    total_carrito = sum(item.producto.precio * item.cantidad for item in carrito_item)
    tarjeta = informacion.nro_tarjeta
    direccion = informacion.direccion
    correo = usuario.email
    return render(request, 'info_pedido.html', 
                  {'carrito_item':carrito_item, 
                   'total_carrito':total_carrito, 
                   'tarjeta':tarjeta, 
                   'direccion':direccion, 
                   'correo':correo})


def borrar_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    CarritoItem.objects.filter(carrito=carrito).delete()
    
    return render (request, 'boleta.html')

def comprar_producto(request, id_producto):
    producto = get_object_or_404(Productos, id_producto=id_producto)
    usuario = request.user

    carrito, created = Carrito.objects.get_or_create(usuario=usuario)
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()


    return redirect('informacion_pago')
