from django.shortcuts import render
from django.http import HttpResponse

from Noticias.models import Noticias

def inicio(request):
    template_name= "index.html"
    
    #n = Noticias.objects.create(
    #    titulo= "Salvamos un gato",
    #    descripcion= "Hoy encontramos un gato casi muerto y lo salvamos :)",
    #    fecha= "10/11/1000"
    #)
    
    Noticia= Noticias.objects.all()
    
    contexto= {
        'Not': Noticias
    }
    return render(request, template_name, contexto)