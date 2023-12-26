import xml.etree.ElementTree as ET
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context, Template
from Proyecto2Ipc.forms import ClienteForm
from Proyecto2Ipc.models import Cliente
from django.shortcuts import render
import os

def index(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_plantilla = os.path.join(BASE_DIR, 'Proyecto2Ipc', 'templates', 'inicio.html')
    
    with open(ruta_plantilla, 'r') as plantillaExterna:
        contenido = plantillaExterna.read()

    return HttpResponse(contenido)

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



  

