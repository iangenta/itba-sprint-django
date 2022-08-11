from apps.tarjetas.models import Tarjeta
from django.db import models

# Create your models here.


class Cliente(models.Model):
    cliente_id = models.IntegerField(primary_key=True, default=1)
    nombre_cliente = models.CharField(max_length=255, default="nombre_cliente")
    apellido_cliente = models.CharField(max_length=255, default="apellido_cliente")
    dni_cliente = models.CharField(max_length=255, default="dni_cliente")
    tipo_cliente = models.CharField(max_length=255, default="tipo_cliente")
    numero_tarjeta = models.ForeignKey(Tarjeta, null = True, blank=True, on_delete=models.CASCADE)