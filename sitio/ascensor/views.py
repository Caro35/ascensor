from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Cliente,Orden
from .forms import ClienteForm,OrdenForm

# Create your views here.
def index(request):
    return render(request,'ascensor/index.html')

def crearCliente(request):
    return render(request,'ascensor/CrearCliente.html')

def crearTecnico(request):
    return render(request,'ascensor/CrearTecnico.html')

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
            # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrdenForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/ListadoOrdenes.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrdenForm()

    return render(request, 'ascensor/ListadoOrdenes.html', {'form': form})