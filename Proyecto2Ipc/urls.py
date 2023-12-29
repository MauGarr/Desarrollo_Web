"""
URL configuration for Proyecto2Ipc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto2Ipc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('producto/', views.producto,name='producto'),
    path('producto/ingresar', views.getinproductos,name='getinproductos'),
    path('producto/editar/<str:nombre>/', views.editarproducto,name='editarproducto'),
    path('producto/saveProductos/', views.guardar_productos),
    path('producto/eliminar_producto/<str:nombre>/', views.eliminar_producto, name='eliminar_producto'),
    path('cliente/', views.cliente,name='cliente'),
    path('cliente/ingresar',views.signup,name="singup"),
    path('cliente/editar/<str:nit>/', views.editarcliente,name='editar_cliente'),
    path('cliente/editar/<str:nit>/actualizarcliente', views.guardar_clientes_actualizar,name='actualizarcliente'),
    path('cliente/saveClientes/', views.guardar_clientes),
    path('cliente/eliminar_cliente/<str:nit>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('facturas/', views.facturas,name='facturas'),
    path('facturas/eliminar_factura/<str:maestro>/', views.eliminar_factura, name='eliminar_factura'),
    path('facturas/ingresar/saveFacturas/', views.guardar_facturas, name='guardar_facturas'),
    path('facturas/ingresar/', views.getinfacturas,name='getinfacturas'),
    path('producto/editar/<str:nombre>/actualizarproducto', views.guardar_productos_actualizar,name='actualizarproducto'),
    
    
]
