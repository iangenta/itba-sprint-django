from django.db import models

# Create your models here.

class Cuenta(models.Model):
    cuenta_id = models.IntegerField(primary_key=True)
    cliente_id = models.IntegerField(max_length=50)
    balance = models.IntegerField()
    tipo_cuenta = models.CharField(max_length=50)
    
    