from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Cliente,Orden
from .forms import ClienteForm,OrdenForm,UserForm

# Create your views here.
def index(request):
    return render(request,'ascensor/index.html')

def misClientes(request):
    return render(request,'ascensor/MisClientes.html')

def listadoClientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/ascensor/ListadoClientes.html?mensaje=exito')
    else:
        form = ClienteForm()
    return render(request, 'ascensor/ListadoClientes.html', {'form': form})

def listadoOrdenes(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            #TODO: Guardar
            return HttpResponseRedirect('ascensor/ListadoOrdenes.html')
    else:
        form = OrdenForm()

    return render(request, 'ascensor/ListadoOrdenes.html', {'form': form})

def nuevaOrden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            #TODO: Guardar
            return HttpResponseRedirect('ascensor/ListadoOrdenes.html')
    else:
        form = OrdenForm()

    return render(request, 'ascensor/NuevaOrden.html', {'form': form})

def misOrdenes(request):
    return render(request, 'ascensor/MisOrdenes.html')

def listadoTecnicos(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #TODO: Guardar
            return HttpResponseRedirect('ascensor/ListadoTecnicos.html')
    else:
        form = UserForm()
    return render(request, 'ascensor/ListadoTecnicos.html', {'form': form})