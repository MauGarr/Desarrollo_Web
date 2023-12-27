import xml.etree.ElementTree as ET
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context, Template
from Proyecto2Ipc.forms import ClienteForm
from Proyecto2Ipc.models import Cliente
from django.shortcuts import render


def index(request):

    return render(request,"winicio.html"),
def singup(request):
    return HttpResponse('Prueba'),


def producto(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_plantilla = os.path.join(BASE_DIR, 'Proyecto2Ipc', 'templates', 'producto.html')
    
    with open(ruta_plantilla, 'r') as plantillaExterna:
        contenido = plantillaExterna.read()

    return HttpResponse(contenido)

def cliente(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_plantilla = os.path.join(BASE_DIR, 'Proyecto2Ipc', 'templates', 'clientes.html')
    
    with open(ruta_plantilla, 'r') as plantillaExterna:
        contenido = plantillaExterna.read()

    return HttpResponse(contenido)

def facturas(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_plantilla = os.path.join(BASE_DIR, 'Proyecto2Ipc', 'templates', 'facturas.html')
    
    with open(ruta_plantilla, 'r') as plantillaExterna:
        contenido = plantillaExterna.read()

    return HttpResponse(contenido)



  

