from django.shortcuts import render
from django.http import HttpResponse

from Noticias.models import Noticias

def admin_edicion_noticias(request):
    template_name= "Noticias/edicion.html"
    

    contexto= {
        'Noticias': Noticias.objects.all(),
    }
    
    return render(request, template_name, contexto)
