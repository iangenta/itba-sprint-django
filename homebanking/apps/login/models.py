from django.db import models
from apps.clientes.models import Cliente
# Create your models here.

class Usuario(models.Model):
    usuario= models.CharField(max_length=12, default="usuario")
    email= models.EmailField(max_length=50, default="email")
    passw= models.CharField(max_length=16, default="password")
    dni = models.IntegerField( default="dni")
    cliente_id = models.ForeignKey(Cliente, null = True, blank=True, on_delete=models.CASCADE)
    