from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    template_name= "index.html"
    contexto= {
        'nombre': "Alex"
    }
    return render(request, template_name, contexto)