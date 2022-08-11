
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_cuentas(request):
    return HttpResponse('index_cuentas')