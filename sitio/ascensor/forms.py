from django.forms import ModelForm
from django import forms
from .models import Cliente,Orden
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'email',
            'password'
        ]

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'tecnico',
            'nombre',
            'apellidos',
            'direccion',
            'ciudad',
            'comuna',
            'telefono',
            'correo',
        ]
class OrdenForm(ModelForm):
    class Meta:
        model = Orden
        fields = [
            'cliente',
            'fecha',
            'horaInicio',
            'horaTermino',
            'identificadorAscensor',
            'modeloAscensor',
            'fallas',
            'reparaciones',
            'piezas',
            'nombreReceptor',
        ]
        widgets = {
            'fecha': forms.TextInput(attrs={'type': 'date'}),
            'horaInicio': forms.TextInput(attrs={'type': 'time'}),
            'horaTermino': forms.TextInput(attrs={'type': 'time'}),
            }