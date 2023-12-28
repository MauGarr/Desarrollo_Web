from django.shortcuts import render
from django.http import HttpResponse
from flask import redirect
from .forms import ClienteForm, ProductoForm, FacturaForm
from .utils import cargar_productos_desde_xml, guardar_productos_en_xml, cargar_clientes_desde_xml, guardar_clientes_en_xml, cargar_facturas_desde_xml, guardar_facturas_en_xml
from .models import Cliente, Producto, Factura
def index(request):
    return render(request, 'inicio.html')

def signup(request):
    # return HttpResponse('Prueba')
    return render(request, 'singup.html')


# Cliente Views
def cliente(request):
    clientes = cargar_clientes_desde_xml("xml/clientes.xml")
    guardar_clientes=guardar_clientes_en_xml(clientes,"xml/clientes.xml")
    return render(request, 'clientes.html', {'clientes': clientes, 'guardar_clientes': guardar_clientes})
def editarcliente(request):
    return render(request, 'editarclientes.html')

def guardar_clientes(request):
  clientes= cargar_clientes_desde_xml("xml/clientes.xml")
  if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        nit= request.POST.get('nit')
        correo= request.POST.get('correo')
        telefono= request.POST.get('telefono')
        cliente = Cliente(nombre=nombre, direccion=direccion, nit=nit, correo=correo, telefono=telefono)
        clientes.append(cliente)
        archivo_xml = "xml/clientes.xml"
        # Guardar la lista actualizada en el archivo XML
        guardar_clientes= guardar_clientes_en_xml(clientes, archivo_xml)

        clientes = cargar_clientes_desde_xml("xml/clientes.xml")
        return render(request, 'clientes.html', {'clientes': clientes, 'guardar_clientes': guardar_clientes})
  else:
        # Si la solicitud no es POST, muestra el formulario vacío
        
        form = ProductoForm()

  clientes = cargar_clientes_desde_xml("xml/clientes.xml")
  guardar_clientes=guardar_clientes_en_xml(clientes,"xml/clientes.xml") 
  return render(request, 'clientes.html', {'clientes': clientes, 'guardar_clientes': guardar_clientes})

def eliminar_cliente(request, nit):
    clientes = cargar_clientes_desde_xml("xml/clientes.xml")
    for cliente in clientes:
        if cliente.nit == nit:
            clientes.remove(cliente)
            break
    archivo_xml = "xml/clientes.xml"
    # Guardar la lista actualizada en el archivo XML
    guardar_clientes= guardar_clientes_en_xml(clientes, archivo_xml)
    return render(request, 'clientes.html', {'clientes': clientes, 'guardar_clientes': guardar_clientes})


#Producto Views
def producto(request):
    productos = cargar_productos_desde_xml("xml/productos.xml")
    guardar_productos=guardar_productos_en_xml(productos,"xml/productos.xml")
    return render(request, 'producto.html', {'productos': productos, 'guardar_productos': guardar_productos})
def editarproducto(request):
    return render(request, 'editarproducto.html')

def guardar_productos(request):
  productos= cargar_productos_desde_xml("xml/productos.xml")
  if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio= request.POST.get('precio')
        existencias= request.POST.get('existencia')
        producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, existencias=existencias)
        productos.append(producto)
        archivo_xml = "xml/productos.xml"
        # Guardar la lista actualizada en el archivo XML
        guardar_productos= guardar_productos_en_xml(productos, archivo_xml)

        productos = cargar_productos_desde_xml("xml/productos.xml")
        return render(request, 'producto.html', {'productos': productos, 'guardar_productos': guardar_productos})
  else:
        # Si la solicitud no es POST, muestra el formulario vacío
        
        form = ProductoForm()

  productos = cargar_productos_desde_xml("xml/productos.xml")
  guardar_productos=guardar_productos_en_xml(productos,"xml/productos.xml") 
  return render(request, 'producto.html', {'productos': productos, 'guardar_productos': guardar_productos})

def eliminar_producto(request, nombre):
    productos = cargar_productos_desde_xml("xml/productos.xml")
    for producto in productos:
        if producto.nombre == nombre:
            productos.remove(producto)
            break
    archivo_xml = "xml/productos.xml"
    # Guardar la lista actualizada en el archivo XML
    guardar_productos= guardar_productos_en_xml(productos, archivo_xml)
    return render(request, 'producto.html', {'productos': productos, 'guardar_productos': guardar_productos})

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

def getinproductos(request):
    productos = cargar_productos_desde_xml("xml/productos.xml")
    guardar_productos=guardar_productos_en_xml(productos,"xml/productos.xml")
    return render(request,"mercaingresa.html",{'productos': productos, 'guardar_productos': guardar_productos})
