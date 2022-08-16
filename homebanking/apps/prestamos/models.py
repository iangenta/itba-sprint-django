from tkinter import CASCADE
from django.db import models
from apps.clientes.models import Cliente
# Create your models here.

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(max_length=50,blank=True, null=True)
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    customer_id = models.ForeignKey(Cliente, on_delete=CASCADE)

    class Meta:
        managed = False
        db_table = 'prestamo'