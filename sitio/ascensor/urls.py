from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('CrearCliente.html', views.crearCliente, name='crearCliente'),
    path('CrearTecnico.html', views.crearTecnico, name='crearTecnico'),
    path('ListadoClientes.html', views.listadoClientes, name='listadoClientes'),
]
