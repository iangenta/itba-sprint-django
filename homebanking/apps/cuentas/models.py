from django.db import models

# Create your models here.

class Cuenta(models.Model):
    cuenta_id = models.IntegerField(primary_key=True, default="cuenta_id")
    cliente_id = models.IntegerField( default="cliente_id")
    balance = models.IntegerField(default="balance")
    tipo_cuenta = models.CharField(max_length=50, default="tipo_cuenta")
    
class Movimiento(models.Model):
    movimiento_id = models.IntegerField(primary_key=True, default="movimiento_id")
    numero_cuenta = models.IntegerField(default="numero_cuenta")
    monto=models.IntegerField(default="monto")
    tipo_operacion= models.CharField(max_length=50, default="tipo_operacion")
    hora = models.TimeField()
    