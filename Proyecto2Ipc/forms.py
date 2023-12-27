import xml.etree.ElementTree as ET
from django import forms
from .models import Cliente, Producto, Factura


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'nit', 'direccion', 'telefono', 'correo']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'existencias']
        
class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['maestro', 'detalle', 'cliente', 'fecha', 'total']
   
