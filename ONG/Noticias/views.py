from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from Noticias.models import Noticias
from .forms import NoticiaForm
from django.urls import reverse

def admin_edicion_noticias(request):
    template_name= "Noticias/edicion.html"
    

    contexto= {
        'Noticias': Noticias.objects.all(),
    }
    
    return render(request, template_name, contexto)

class NuevaNoticia(CreateView):
    model= Noticias
    template_name = 'Noticias/nueva_noticia.html'
    form_class= NoticiaForm
    
    def get_success_url(self):
        return reverse("edicion_noticias:admin_edicion_noticias")
    #No pude hacer que vuelva a admin_edicion_noticias