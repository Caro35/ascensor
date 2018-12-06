from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string

from ascensor.forms import ClienteForm, OrdenForm, UserForm

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


# Clientes
@staff_member_required(login_url=settings.LOGIN_URL)
def listadoClientes(request):
    if request.method == 'POST':
        form = None
        if (request.POST['idCliente'] != "None"):
            instance = get_object_or_404(Cliente,id=request.POST['idCliente'])
            form = ClienteForm(request.POST,instance=instance)
        else:
            form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ascensor/ListadoClientes.html?mensaje=exito')
    else:
        form = ClienteForm()
    # Consulta de clientes
    clientes = Cliente.objects.all()
    return render(request, 'ascensor/ListadoClientes.html', {'form': form,'clientes':clientes})

@staff_member_required(login_url=settings.LOGIN_URL)
def formClientes(request):
    pk = request.GET.get('id','')
    datos = dict()
    if(pk!=''):
        # Editar
        form = ClienteForm(instance=get_object_or_404(Cliente,pk=request.GET['id']))
        datos['formulario'] = render_to_string('ascensor/formularios/form_clientes.html',context={'form':form},request=request)
        # return render(request,'ascensor/formularios/form_clientes.html',context={'form':form})
    else:
        # Nuevo
        form = ClienteForm()
        datos['formulario'] = render_to_string('ascensor/formularios/form_clientes.html',context={'form':form},request=request)
    return JsonResponse(datos)

@staff_member_required(login_url=settings.LOGIN_URL)
def eliminarCliente(request):
    pk = request.GET.get('id','')
    cliente = get_object_or_404(Cliente,pk=pk)
    cliente.delete()
    return JsonResponse({"respuesta":"OK"})