from pyexpat import model
from django.db import models

# Create your models here.

class Cliente(models.Model):
    cliente_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.CharField(max_length=255)
    tipo_cliente = models.CharField(max_length=255)