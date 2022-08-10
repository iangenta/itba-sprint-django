from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario= models.CharField(max_length=12)
    email= models.EmailField(max_length=50)
    passw= models.CharField(max_length=16)
    dni = models.IntegerField()
    
    