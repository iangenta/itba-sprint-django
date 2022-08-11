from django.db import models

# Create your models here.



class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50,blank=True, null=True)
    customer_surname = models.CharField(max_length=50,blank=True, null=True)
    customer_dni = models.CharField(max_length=50,blank=True, null=True,db_column='customer_DNI')
    dob = models.CharField(max_length=50,blank=True, null=True)
    branch_id = models.IntegerField()
    tipo_cliente = models.CharField(max_length=50,blank=True, null=True)
    numero_tarjeta = models.CharField(max_length=50,blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'cliente'



class Movimientos(models.Model):
    id_movimiento = models.IntegerField(db_column='id movimiento', unique=True, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    numero_de_cuenta = models.IntegerField(db_column='numero de cuenta', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    monto = models.IntegerField(blank=True, null=True)
    tipo_de_operacion = models.IntegerField(db_column='tipo de operacion', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hora = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimientos'
