from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from Noticias.models import Noticias
from .forms import NoticiaForm
from django.urls import reverse
'''
def admin_edicion_noticias(request):
    template_name= "Noticias/edicion.html"
    

    contexto= {
        'Noticias': Noticias.objects.all(),
    }
    
    return render(request, template_name, contexto)
'''
class ListadoNoticias(ListView):
    model= Noticias
    template_name= "Noticias/edicion.html"
    context_object_name = 'Noticias'
    paginate_by = 3
    
    def get_queryset(self):
        return Noticias.objects.all().order_by("titulo")
    

class NuevaNoticia(CreateView):
    model= Noticias
    template_name = 'Noticias/nueva_noticia.html'
    form_class= NoticiaForm
    
    def get_success_url(self):
        return reverse("edicion_noticias:admin_edicion_noticias")
