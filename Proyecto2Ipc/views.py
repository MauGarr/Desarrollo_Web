from django.shortcuts import render
from django.http import HttpResponse
from flask import redirect
from .forms import ClienteForm, ProductoForm, FacturaForm
from .utils import cargar_productos_desde_xml, guardar_productos_en_xml, cargar_clientes_desde_xml, guardar_clientes_en_xml, cargar_facturas_desde_xml, guardar_facturas_en_xml
from .models import Cliente, Producto, Factura
def index(request):
    return render(request, 'inicio.html')

def signup(request):
    return HttpResponse('Prueba')


# Cliente Views
def cliente(request):
    return render(request, 'clientes.html')

def guardar_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # El formulario es válido, procesa los datos
            nit = form.cleaned_data['nit']
            nombre = form.cleaned_data['nombre']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            correo = form.cleaned_data['correo']

            # Cargar clientes existentes
            archivo_xml = "clientes.xml"
            clientes = cargar_clientes_desde_xml(archivo_xml)

            # Agregar el nuevo cliente
            nuevo_cliente = Cliente(
                nit=nit,
                nombre=nombre,
                direccion=direccion,
                telefono=telefono,
                correo=correo
            )
            clientes.append(nuevo_cliente)

            # Guardar la lista actualizada en el archivo XML
            guardar_clientes_en_xml(clientes, archivo_xml)

            return redirect('cliente_list')
    else:
        # Si la solicitud no es POST, muestra el formulario vacío
        form = ClienteForm()

    return render(request, 'clientes/guardar_clientes.html', {'form': form})


#Producto Views
def producto(request):
    
    return render(request, 'producto.html')
def guardar_productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # El formulario es válido, procesa los datos
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            precio = form.cleaned_data['precio']
            existencias = form.cleaned_data['existencias']

            # Cargar productos existentes
            archivo_xml = "productos.xml"
            productos = cargar_productos_desde_xml(archivo_xml)

            # Agregar el nuevo producto
            nuevo_producto = Producto(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                existencias=existencias
            )
            productos.append(nuevo_producto)

            # Guardar la lista actualizada en el archivo XML
            guardar_productos_en_xml(productos, archivo_xml)

            return redirect('product_list')
    else:
        # Si la solicitud no es POST, muestra el formulario vacío
        form = ProductoForm()

    return render(request, 'productos/guardar_productos.html', {'form': form})
# Facturas Views
def facturas(request):
    return render(request, 'facturas.html')
def guardar_facturas(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            # El formulario es válido, procesa los datos
            fecha = form.cleaned_data['fecha']
            total = form.cleaned_data['total']
            cliente = form.cleaned_data['cliente']
            detalle = form.cleaned_data['detalle']
            maestro = form.cleaned_data['maestro']

            # Cargar clientes existentes
            archivo_xml = "facturas.xml"
            facturas = cargar_facturas_desde_xml(archivo_xml)

            # Agregar el nueva factura
            nueva_factura = Factura(
                fecha=fecha,
                total=total,
                cliente=cliente,
                detalle=detalle,
                maestro=maestro
            )
            facturas.append(nueva_factura)

            # Guardar la lista actualizada en el archivo XML
            guardar_facturas_en_xml(facturas, archivo_xml)

            return redirect('cliente_list')
    else:
        # Si la solicitud no es POST, muestra el formulario vacío
        form = FacturaForm()

    return render(request, 'clientes/guardar_clientes.html', {'form': form})

def nav(request):
    return render(request,"nav.html")
