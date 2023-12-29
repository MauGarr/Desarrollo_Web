from django.shortcuts import render
from django.http import HttpResponse
from .forms import ClienteForm, ProductoForm, FacturaForm
from .utils import cargar_productos_desde_xml, guardar_productos_en_xml, cargar_clientes_desde_xml, guardar_clientes_en_xml, cargar_facturas_desde_xml, guardar_facturas_en_xml
from .models import Cliente, Producto, Factura
from flask import redirect
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

def editarcliente(request, nit):
    clientes = cargar_clientes_desde_xml("xml/clientes.xml")
    cliente_por_editar = None
    for cliente in clientes:
        if cliente.nit == nit:
            cliente_por_editar = cliente
            clientes.remove(cliente)
            break
    archivo_xml = "xml/clientes.xml"
    nombre=cliente_por_editar.nombre
    direccion=cliente_por_editar.direccion
    nit=cliente_por_editar.nit
    correo=cliente_por_editar.correo
    telefono=cliente_por_editar.telefono
    
    # Guardar la lista actualizada en el archivo XML
    guardar_clientes_en_xml(clientes, archivo_xml)
    
    
    return render(request, 'editarclientes.html', {'nombre': nombre, 'direccion': direccion, 'nit': nit, 'correo': correo, 'telefono': telefono})

def guardar_clientes_actualizar(request,nit):
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

def editarproducto(request, nombre):
    productos = cargar_productos_desde_xml("xml/productos.xml")
    producto_por_editar = None
    for producto in productos:
        if producto.nombre == nombre:
            producto_por_editar = producto
            productos.remove(producto)
            break
    archivo_xml = "xml/productos.xml"
    nombre=producto_por_editar.nombre
    descripcion=producto_por_editar.descripcion
    precio=producto_por_editar.precio
    existencias=producto_por_editar.existencias
    # Guardar la lista actualizada en el archivo XML
    guardar_productos_en_xml(productos, archivo_xml)
    
    
    return render(request, 'editarproducto.html', {'nombre': nombre, 'descripcion': descripcion, 'precio': precio, 'existencias': existencias})

def guardar_productos_actualizar(request, nombre):
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
  facturas = cargar_facturas_desde_xml("xml/facturas.xml")
  guardar_facturas= guardar_facturas_en_xml(facturas, "xml/facturas.xml")
  return render(request, 'facturas.html', {'facturas': facturas, 'guardar_facturas': guardar_facturas})
def guardar_facturas(request):
  facturas= cargar_facturas_desde_xml("xml/facturas.xml")
  if request.method == 'POST':
        maestro = request.POST.get('maestro')
        productos = request.POST.get('productos')
        nit_cliente= request.POST.get('nit_cliente')
        total= request.POST.get('total')
        factura = Factura(total=total, nit_cliente=nit_cliente, productos=productos, maestro=maestro)
        facturas.append(factura)
        archivo_xml = "xml/facturas.xml"
        # Guardar la lista actualizada en el archivo XML
        guardar_facturas= guardar_facturas_en_xml(facturas, archivo_xml)

        facturas = cargar_facturas_desde_xml("xml/facturas.xml")
        return render(request, 'facturas.html', {'facturas': facturas, 'guardar_facturas': guardar_facturas})
  else:
        # Si la solicitud no es POST, muestra el formulario vacío
        
        form = ProductoForm()

  facturas = cargar_facturas_desde_xml("xml/facturas.xml")
  guardar_facturas= guardar_facturas_en_xml(facturas, archivo_xml)
  return render(request, 'facturas.html', {'facturas': facturas, 'guardar_facturas': guardar_facturas})
def eliminar_factura(request, maestro):
    facturas = cargar_facturas_desde_xml("xml/facturas.xml")
    for factura in facturas:
        if factura.maestro == maestro:
            facturas.remove(factura)
            break
    archivo_xml = "xml/facturas.xml"
    # Guardar la lista actualizada en el archivo XML
    guardar_facturas= guardar_facturas_en_xml(facturas, archivo_xml)
    return render(request, 'facturas.html', {'facturas': facturas, 'guardar_facturas': guardar_facturas})

def editarfactura(request, maestro):
    facturas = cargar_facturas_desde_xml("xml/facturas.xml")
    factura_por_editar = None
    for factura in facturas:
        if factura.maestro == maestro:
            factura_por_editar = factura
            facturas.remove(factura)
            break
    archivo_xml = "xml/facturas.xml"
    maestro=factura_por_editar.maestro
    productos=factura_por_editar.productos
    nit_cliente=factura_por_editar.nit_cliente
    total=factura_por_editar.total
    # Guardar la lista actualizada en el archivo XML
    guardar_facturas_en_xml(facturas, archivo_xml)
      
    return render(request, 'editarFactura.html', {'maestro': maestro, 'productos': productos, 'nit_cliente': nit_cliente, 'total': total})

def guardar_facturas_actualizar(request, maestro):
  facturas= cargar_facturas_desde_xml("xml/facturas.xml")
  if request.method == 'POST':
        maestro = request.POST.get('maestro')
        productos = request.POST.get('productos')
        nit_cliente= request.POST.get('nit_cliente')
        total= request.POST.get('total')
        factura = Factura(total=total, nit_cliente=nit_cliente, productos=productos, maestro=maestro)
        facturas.append(factura)
        archivo_xml = "xml/facturas.xml"
        # Guardar la lista actualizada en el archivo XML
        guardar_facturas= guardar_facturas_en_xml(facturas, archivo_xml)
        facturas = cargar_facturas_desde_xml("xml/facturas.xml")
        return render(request, 'facturas.html', {'facturas': facturas, 'guardar_facturas': guardar_facturas})
  else:
        # Si la solicitud no es POST, muestra el formulario vacío
        
        form = ProductoForm()

  facturas = cargar_facturas_desde_xml("xml/facturas.xml")
  guardar_facturas=guardar_facturas_en_xml(facturas,"xml/facturas.xml") 
  return render(request, 'facturas.html', {'facturas': facturas, 'guardar_facturas': guardar_facturas})
def nav(request):
    return render(request,"nav.html")

def getinproductos(request):
    productos = cargar_productos_desde_xml("xml/productos.xml")
    guardar_productos=guardar_productos_en_xml(productos,"xml/productos.xml")
    return render(request,"mercaingresa.html",{'productos': productos, 'guardar_productos': guardar_productos})

def getinfacturas(request):
    facturas = cargar_facturas_desde_xml("xml/facturas.xml")
    guardar_facturas=guardar_facturas_en_xml(facturas,"xml/facturas.xml")
    return render(request,"agregarFactura.html",{'facturas': facturas, 'guardar_facturas': guardar_facturas})
