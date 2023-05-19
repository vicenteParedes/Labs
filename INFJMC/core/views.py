from django.shortcuts import render
from django.http import  HttpResponse
from .models import Carrera

def index(request):
    return HttpResponse('Hola mundo')
    

def home(request):
    #return HttpResponse('home')
    return render(request, 'core/home.html')

def profesores(request):
    #return HttpResponse('profesores')
    return render(request, 'core/profesores.html')

def carreras(request):
    #return HttpResponse('Carreras')
    carreras= Carrera.objects.all()
    data={
        'carrera': carreras
    }
    return render(request, 'core/carreras.html',data)
    
# Create your views here.
