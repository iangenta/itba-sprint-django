from django.db import models

# Create your models here.


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.CharField(max_length=50,blank=True, null=True)
    tipo_cuenta = models.CharField(max_length=50,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'

class Movimiento(models.Model):
    movimiento_id = models.IntegerField(primary_key=True, default="movimiento_id")
    numero_cuenta = models.IntegerField(default="numero_cuenta")
    monto=models.IntegerField(default="monto")
    tipo_operacion= models.CharField(max_length=50, default="tipo_operacion")
    hora = models.TimeField()
    