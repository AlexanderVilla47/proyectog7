from django.shortcuts import render
from django.http import HttpResponse

from Noticias.models import Noticias

def inicio(request):
    template_name= "index.html"
    
    #n = Noticias.objects.create(
    #    titulo= "Salvamos un cav",
    #    descripcion= "Hoy encontramos un gato casi muerto y lo salvamos :)",
    #    fecha= "10/11/1000"
    #)
    
    noticias= Noticias.objects.all()

    contexto= {
        'Noticias': noticias,
    }
    return render(request, template_name, contexto)

def login(request):
    template_name= "login.html"
    
    return render(request, template_name, {})