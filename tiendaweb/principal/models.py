from django.db import models

class Productos(models.Model):
    id_producto   = models.IntegerField(primary_key=True)
    nombre        = models.CharField(max_length=60) 
    categoria     = models.CharField(max_length=60)
    precio        = models.IntegerField()
    descripcion   = models.CharField(max_length=500, null=False, default='')

    def __str__(self):
        return str(self.nombre)+" "+str(self.precio)   
