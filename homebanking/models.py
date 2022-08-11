# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    customer_id = models.AutoField()
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipo_cliente = models.CharField(blank=True, null=True)
    numero_tarjeta = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField()
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


class Empleado(models.Model):
    employee_id = models.AutoField()
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleado'


class Movimientos(models.Model):
    id_movimiento = models.IntegerField(db_column='id movimiento', unique=True, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    numero_de_cuenta = models.IntegerField(db_column='numero de cuenta', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    monto = models.IntegerField(blank=True, null=True)
    tipo_de_operacion = models.IntegerField(db_column='tipo de operacion', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hora = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField()
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField()
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    numero = models.IntegerField(db_column='Numero', unique=True)  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    fecha_de_otorgamiento = models.IntegerField(db_column='Fecha de otorgamiento')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha_de_expiracion = models.IntegerField(db_column='Fecha de expiracion')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    credito_debito = models.IntegerField(db_column='Credito/debito')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marca_tarjeta = models.IntegerField(db_column='Marca tarjeta')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'tarjeta'
