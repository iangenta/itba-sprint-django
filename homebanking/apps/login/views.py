
from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index_login(request):
    return render(request,'login/index.html')