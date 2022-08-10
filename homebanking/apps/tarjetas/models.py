from django.db import models

# Create your models here.

class Tarjeta(models.Model):
    numero = models.IntegerField(primary_key=True)
    cvv = models.IntegerField(max_length=3)
    fecha_otorgamiento = models.DateField()
    fecha_expiracion = models.DateField()
    tipo_tarjeta = models.CharField(max_length=10)
    marca_tarjeta = models.CharField(max_length=50)