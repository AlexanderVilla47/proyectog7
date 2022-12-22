from django import forms
from .models import Noticias

class NoticiaForm(forms.ModelForm):
    class Meta:
        model= Noticias
        fields=["titulo", "descripcion", "fecha", "activo"]
        
        