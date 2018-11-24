from django.forms import ModelForm
from .models import Cliente,Orden

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
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