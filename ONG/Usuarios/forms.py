from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):
    username= forms.CharField(widget= forms.TextInput(attrs={"class": "form-control"}))
    first_name= forms.CharField(widget= forms.TextInput(attrs={"class": "form-control"}))
    last_name= forms.CharField(widget= forms.TextInput(attrs={"class": "form-control"}))
    email= forms.CharField(widget= forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model= Usuario
        fields=["username", "first_name", "last_name", "email",]