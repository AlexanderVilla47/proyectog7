
from django.contrib import admin
from django.urls import path

from .views import inicio
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name='Inicio'),
    path('login/', views.login, name='Iniciar Sesión'),
]
