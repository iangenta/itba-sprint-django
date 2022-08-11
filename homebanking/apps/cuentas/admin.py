from django.contrib import admin
from apps.cuentas.models import Cuenta,Movimiento
# Register your models here.
admin.site.register(Cuenta)
admin.site.register(Movimiento)