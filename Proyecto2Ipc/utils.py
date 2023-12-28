import xml.etree.ElementTree as ET
from .models import Cliente, Producto, Factura

#Clientes
#Utilidad para guardar datos en xml de los clientes
def guardar_clientes_en_xml(clientes, archivo_xml):
    root = ET.Element("clientes")

    for cliente in clientes:
        cliente_elem = ET.SubElement(root, "cliente")
        nit_cliente = ET.SubElement(cliente_elem, "nit")
        nit_cliente.text = str(cliente.nit)
        nombre_cliente = ET.SubElement(cliente_elem, "nombre")
        nombre_cliente.text = cliente.nombre
        direccion_cliente = ET.SubElement(cliente_elem, "direccion")
        direccion_cliente.text = cliente.direccion
        telefono_cliente = ET.SubElement(cliente_elem, "telefono")
        telefono_cliente.text = cliente.telefono
        correo_cliente = ET.SubElement(cliente_elem, "correo")
        correo_cliente.text = cliente.correo

    tree = ET.ElementTree(root)
    with open(archivo_xml, "wb") as xml_file:
        tree.write(xml_file)
#Utilidad para cargar datos en xml de los clientes
def cargar_clientes_desde_xml(archivo_xml):
    tree = ET.parse(archivo_xml)
    root = tree.getroot()

    clientes = []
    for clientes_elem in root.findall("cliente"):
        nit = int(clientes_elem.find("nit").text)
        nombre = clientes_elem.find("nombre").text
        direccion = clientes_elem.find("direccion").text
        telefono = clientes_elem.find("telefono").text
        correo = clientes_elem.find("correo").text
        clientes.append(Cliente(nit=nit, nombre=nombre, direccion=direccion, telefono=telefono, correo=correo))

    return clientes

#Productos
#Utilidad para guardar datos en xml de los productos
def guardar_productos_en_xml(productos, archivo_xml):
    root = ET.Element("productos")

    for producto in productos:
        producto_elem = ET.SubElement(root, "producto")
        nombre_producto = ET.SubElement(producto_elem, "nombre")
        nombre_producto.text = producto.nombre
        descripcion_producto = ET.SubElement(producto_elem, "descripcion")
        descripcion_producto.text = producto.descripcion
        precio_producto = ET.SubElement(producto_elem, "precio")
        precio_producto.text = producto.precio
        existencias_producto = ET.SubElement(producto_elem, "existencias")
        existencias_producto.text = producto.existencias

    tree = ET.ElementTree(root)
    with open(archivo_xml, "wb") as xml_file:
        tree.write(xml_file)
#Utilidad para cargar datos en xml de los productos
def cargar_productos_desde_xml(archivo_xml):
    tree = ET.parse(archivo_xml)
    root = tree.getroot()

    productos = []
    for producto_elem in root.findall("producto"):
        nombre = producto_elem.find("nombre").text
        descripcion = producto_elem.find("descripcion").text
        precio = producto_elem.find("precio").text
        existencias = producto_elem.find("existencias").text
        productos.append(Producto(nombre=nombre, descripcion=descripcion, precio=precio, existencias=existencias))

    return productos
#Facturas
#Utilidad para guardar datos en xml de las facturas
def guardar_facturas_en_xml(facturas, archivo_xml):
    root = ET.Element("facturas")

    for factura in facturas:
        factura_elem = ET.SubElement(root, "factura")
        fecha_factura = ET.SubElement(factura_elem, "fecha")
        fecha_factura.text = str(factura.fecha)
        total_factura = ET.SubElement(factura_elem, "total")
        total_factura.text = str(factura.total)
        cliente_factura = ET.SubElement(factura_elem, "cliente")
        cliente_factura.text = str(factura.cliente_id)
        detalle_factura = ET.SubElement(factura_elem, "detalle")
        detalle_factura.text = str(factura.detalle_id)
        maestro_factura = ET.SubElement(factura_elem, "maestro")
        maestro_factura.text = str(factura.maestro_id)

    tree = ET.ElementTree(root)
    with open(archivo_xml, "wb") as xml_file:
        tree.write(xml_file)
#Utilidad para cargar datos en xml de las facturas
def cargar_facturas_desde_xml(archivo_xml):
    tree = ET.parse(archivo_xml)
    root = tree.getroot()

    facturas = []
    for factura_elem in root.findall("factura"):
        fecha = factura_elem.find("fecha").text
        total = float(factura_elem.find("total").text)
        cliente = int(factura_elem.find("cliente").text)
        detalle = int(factura_elem.find("detalle").text)
        maestro = int(factura_elem.find("maestro").text)
        facturas.append(Factura(fecha=fecha, total=total, cliente_id=cliente, detalle_id=detalle, maestro_id=maestro))

    return facturas