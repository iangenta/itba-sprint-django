
from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index_prestamos(request):
    return HttpResponse('index_prestamos')