from django.forms import ModelForm
from django import forms
from .models import Cliente,Orden

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
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