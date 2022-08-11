from django.db import models
from apps.clientes.models import Cliente
# Create your models here.

class Prestamo(models.Model):
    loan_id = models.IntegerField(primary_key=True, default="loan_id")
    loan_date = models.DateField( default="loan_date")
    loan_total = models.IntegerField( default="loan_total")
    loan_type = models.CharField(max_length=50, default="loan_type")
    cliente_id= models.ForeignKey(Cliente,null = True, blank = True, on_delete=models.CASCADE)
    
    