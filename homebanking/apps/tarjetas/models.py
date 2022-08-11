from django.db import models

# Create your models here.

class Tarjeta(models.Model):
    numero = models.IntegerField(db_column='Numero', unique=True)  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    fecha_de_otorgamiento = models.DateField(db_column='Fecha de otorgamiento')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_de_expiracion = models.DateField(db_column='Fecha de expiracion')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    credito_debito = models.IntegerField(db_column='Credito/debito')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marca_tarjeta = models.IntegerField(db_column='Marca tarjeta')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'tarjeta'
