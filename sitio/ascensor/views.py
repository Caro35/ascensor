from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClienteForm, OrdenForm, UserForm
from .models import Cliente, Orden


# Create your views here.
@login_required
def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s&noauth=noauth' % (settings.LOGIN_URL, request.path))
    else:
        if request.user.is_staff:
            return redirect('ListadoOrdenes.html')
        else:
            return redirect('MisOrdenes.html')

@login_required
def misClientes(request):
    return render(request,'ascensor/MisClientes.html')

@staff_member_required(login_url=settings.LOGIN_URL)
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
    # Consulta de clientes
    clientes = Cliente.objects.all()
    return render(request, 'ascensor/ListadoClientes.html', {'form': form,'clientes':clientes})

@staff_member_required(login_url=settings.LOGIN_URL)
def listadoOrdenes(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            #TODO: Guardar
            return HttpResponseRedirect('ascensor/ListadoOrdenes.html')
    else:
        form = OrdenForm()

    return render(request, 'ascensor/ListadoOrdenes.html', {'form': form})

@login_required
def nuevaOrden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            #TODO: Guardar
            return HttpResponseRedirect('ascensor/ListadoOrdenes.html')
    else:
        form = OrdenForm()

    return render(request, 'ascensor/NuevaOrden.html', {'form': form})

@login_required
def misOrdenes(request):
    return render(request, 'ascensor/MisOrdenes.html')

@staff_member_required(login_url=settings.LOGIN_URL)
def listadoTecnicos(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #TODO: Guardar
            return HttpResponseRedirect('ascensor/ListadoTecnicos.html')
    else:
        form = UserForm()
    return render(request, 'ascensor/ListadoTecnicos.html', {'form': form})

def salir(request):
    logout(request)
    return HttpResponseRedirect('/ascensor')
