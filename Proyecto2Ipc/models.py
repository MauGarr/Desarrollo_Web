from django.db import models


class Cliente(models.Model):
    nombre= models.CharField(max_length=255, blank=False, null=False)
    nit= models.CharField(max_length=11, blank=False, null=False, unique=True)
    direccion = models.TextField(("Ingrese la direccion."))
    telefono = models.CharField(max_length=8, blank=False, null=False)
    correo = models.EmailField(max_length=254, blank=False, null=False)
    

    
class Producto(models.Model):
    nombre= models.CharField(max_length=255, blank=False, null=False)
    descripcion= models.TextField(("Ingrese la descripcion."))
    precio= models.DecimalField(max_digits=5, decimal_places=2)
    existencias= models.IntegerField()
    
class Factura(models.Model):
    maestro = models.CharField(max_length=11, blank=False, null=False, unique=True)
    productos = models.TextField("Productos") 
    nit_cliente = models.CharField(max_length=11, blank=False, null=False, unique=True)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    

class Meta:
    app_label = 'Proyecto2Ipc'    
