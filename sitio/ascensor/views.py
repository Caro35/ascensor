from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'ascensor/index.html')

def crearCliente(request):
    return render(request,'ascensor/CrearCliente.html')

def crearTecnico(request):
    return render(request,'ascensor/CrearTecnico.html')

def listadoClientes(request):
    return render(request,'ascensor/ListadoClientes.html')
