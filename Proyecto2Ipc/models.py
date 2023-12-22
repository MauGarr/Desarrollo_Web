from django.db import models

class Cliente(models.Model):
    nombre= models.CharField(max_length=255, blank=False, null=False)
    nit= models.CharField(max_length=11, blank=False, null=False, unique=True)
    direccion = models.TextField(("Ingrese la direccion."))
    telefono = models.CharField(max_length=8, blank=False, null=False)
    correo = models.EmailField(max_length=254, blank=False, null=False)
    
    def __str__(self):
        return self.nombre

    
class Producto(models.Model):
    nombre= models.CharField(max_length=255, blank=False, null=False)
    descripcion= models.TextField(("Ingrese la descripcion."))
    precio= models.DecimalField(max_digits=5, decimal_places=2)
    existencias= models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class facturas(models.Model):
    maestro = models.ForeignKey(Producto, on_delete=models.CASCADE)
    detalle = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name= 'detalles')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='facturas')
    fecha = models.DateField(("Fecha de la factura."))
    total = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.cliente.nombre
    
class Meta:
    app_label = 'Proyecto2Ipc'    
