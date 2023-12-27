from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'inicio.html')

def signup(request):
    return HttpResponse('Prueba')

def producto(request):
    return render(request, 'producto.html')

def cliente(request):
    return render(request, 'clientes.html')

def facturas(request):
    return render(request, 'facturas.html')

def nav(request):
    return render(request,"nav.html")
