from django.shortcuts import render
from django.http import HttpResponse

from Noticias.models import Noticias

def inicio(request):
    template_name= "index.html"
    
    
    return render(request, template_name, {})

def login(request):
    template_name= "login.html"
    #if 'ingresar' in request.POST:
    #    username= request.POST.get("username")
    #if 'ingresar' in request.POST:
    #    username= request.POST.get("password")   
        
    #print(request.method)
    #print(request.POST.get("password", None))
    #print(request.POST.get("username", None))
    return render(request, template_name, {})

def noticias(request):
    template_name= "noticias.html"
    
    #n = Noticias.objects.create(
    #    titulo= "Salvamos un cav",
    #    descripcion= "Hoy encontramos un gato casi muerto y lo salvamos :)",
    #    fecha= "10/11/1000"
    #)
    

    contexto= {
        'Noticias': Noticias.objects.filter(activo=True),
    }
    
    return render(request, template_name, contexto)