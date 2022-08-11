from django.db import models

# Create your models here.

class Tarjeta(models.Model):
    numero = models.IntegerField(primary_key=True, default="numero")
    cvv = models.IntegerField( default="cvv")
    fecha_otorgamiento = models.DateField()
    fecha_expiracion = models.DateField()
    tipo_tarjeta = models.CharField(max_length=10, default="tipo_tarjeta")
    marca_tarjeta = models.CharField(max_length=50, default="marca_tarjeta")