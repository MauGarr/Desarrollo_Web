import xml.etree.ElementTree as ET
from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nit', 'nombre', 'direccion','telefono','correo')

    def carga_datos():
        try:
            tree = ET.parse('xml/clientes.xml')
            root = tree.getroot()
            clientes = []
            for cliente_elem in root.findall('cliente'):
                cliente = {
                    'nit': cliente_elem.find('nit').text,
                    'nombre': cliente_elem.find('nombre').text,
                    'direccion': cliente_elem.find('direccion').text,
                    'telefono': cliente_elem.find('telefono').text,
                    'correo': cliente_elem.find('correo').text,
                }
                clientes.append(cliente)
            return clientes
        except FileNotFoundError:
            return []
        
    def guardar_dato(clientes):
        root = ET.Element('clientes')
        for cliente in clientes:
            cliente_elem = ET.SubElement(root, 'cliente')
            ET.SubElement(cliente_elem, 'nit').text = cliente['nit']
            ET.SubElement(cliente_elem, 'nombre').text = cliente['nombre']
            ET.SubElement(cliente_elem, 'direccion').text = cliente['direccion']
            ET.SubElement(cliente_elem, 'telefono').text = cliente['telefono']
            ET.SubElement(cliente_elem, 'correo').text = cliente['correo']
        tree = ET.ElementTree(root)
        tree.write('clientes.xml')

   
