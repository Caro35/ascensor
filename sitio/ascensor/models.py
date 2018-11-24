from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    objects = models.Manager()
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length = 25)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    correo = models.EmailField()
    #El Técnico es un User.
    tecnico = models.ForeignKey(User,on_delete=models.DO_NOTHING)
class Orden(models.Model):
    objects = models.Manager()
    cliente = models.ForeignKey(Cliente,on_delete=models.DO_NOTHING)
    fecha = models.DateField()
    horaInicio = models.TimeField(verbose_name="Hora de inicio")
    horaTermino = models.TimeField(verbose_name="Hora de termino")
    identificadorAscensor = models.CharField(max_length=20,verbose_name="Identificador ascensor")
    modeloAscensor = models.CharField(max_length=20,verbose_name="Modelo del ascensor")
    fallas = models.TextField(blank=True)
    reparaciones = models.TextField(blank=True)
    piezas = models.TextField(blank=True)
    nombreReceptor = models.CharField(max_length=50,verbose_name="Nombre del receptor")

