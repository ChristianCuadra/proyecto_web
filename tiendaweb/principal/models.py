from django.db import models
from django.contrib.auth.models import User

class Productos(models.Model):
    id_producto   = models.IntegerField(primary_key=True)
    nombre        = models.CharField(max_length=60) 
    categoria     = models.CharField(max_length=60)
    precio        = models.IntegerField()
    descripcion   = models.CharField(max_length=1000, null=False, default='')
    imagen        = models.ImageField(upload_to='producto')
    marca         = models.CharField(max_length=100, null=False, default='')
    
    def __str__(self):
        return str(self.nombre)+" "+str(self.precio)   


class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
class CarritoItem(models.Model):
    id = models.AutoField(primary_key=True)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id) + (self.producto.nombre)
    
    
class InformacionUsuario (models.Model):
    usuario =         models.OneToOneField(User, on_delete=models.CASCADE)
    nro_tarjeta =     models.CharField(max_length=16)
    codigo_seg =      models.CharField(max_length=3)
    fecha_venc_mes =  models.CharField(max_length=2)
    fecha_venc_anno = models.CharField(max_length=2)
    direccion =       models.CharField(max_length=300)
    
    def __str__(self):
        return str (self.usuario) + (self.nro_tarjeta)