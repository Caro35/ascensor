from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('MisClientes.html', views.misClientes, name='misClientes'),
    path('MisOrdenes.html', views.misOrdenes, name='misOrdenes'),
    path('ListadoClientes.html', views.listadoClientes, name='listadoClientes'),
    path('ListadoOrdenes.html', views.listadoOrdenes, name='listadoOrdenes'),
    path('NuevaOrden.html', views.nuevaOrden, name='nuevaOrden'),
    path('ListadoTecnicos.html', views.listadoTecnicos, name='listadoTecnicos'),
    path('logout',views.salir,name='salir'),
    path('form_clientes',views.formClientes,name='formClientes'),
    path('eliminarCliente',views.eliminarCliente,name='eliminarCliente'),
    
]
