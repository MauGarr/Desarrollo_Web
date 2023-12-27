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




def lista_clientes(request):
    clientes = ClienteForm.carga_datos()
    return render(request, '/Proyecto2Ipc/plantillas/lista_clientes.html', {'clientes': clientes})

def detalle_clientes(request, nit):
    clientes = ClienteForm.carga_datos()
    cliente = next((c for c in clientes if c['nit'] == nit), None)
    return render(request, 'plantillas/detalles_cliente.html', {'cliente': cliente})


def nuevo_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = {
                'nit': form.cleaned_data['nit'],
                'nombre': form.cleaned_data['nombre'],
                'direccion': form.cleaned_data['direccion'],
                'telefono': form.cleaned_data['telefono'],
                'correo': form.cleaned_data['correo'],
            }
            clientes = ClienteForm.carga_datos()
            clientes.append(cliente)
            ClienteForm.guardar_dato(clientes)
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'mycrudapp/cliente_edit.html', {'form': form})

def cliente_edit(request, nit):
    clientes = ClienteForm.carga_datos()
    cliente = next((c for c in clientes if c['nit'] == nit), None)
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente['nombre'] = form.cleaned_data['nombre']
            cliente['direccion'] = form.cleaned_data['direccion']
            cliente['telefono'] = form.cleaned_data['telefono']
            cliente['correo'] = form.cleaned_data['correo']
            Cliente.guardar_dato(clientes)
            return redirect('lista_clientes')
    else:
        form = ClienteForm(initial=cliente)
    return render(request, 'plantillas/editor_cliente.html', {'form': form})

def cliente_delete(request, nit):
    clientes = ClienteForm.carga_datos()
    clientes = [c for c in clientes if c['nit'] != nit]
    ClienteForm.guardar_dato(clientes)
    return redirect('cliente_list')   

  

