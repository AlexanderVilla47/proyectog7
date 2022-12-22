from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from Usuarios.models import Usuario
from .forms import UsuarioForm
from django.urls import reverse

class Registro(CreateView):
    model= Usuario
    template_name = 'Usuarios/registro.html'
    form_class= UsuarioForm
    
    def get_success_url(self):
        return reverse("Iniciar Sesión")
    #No pude hacer que vuelva a admin_edicion_noticias