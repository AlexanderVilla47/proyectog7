from django.urls import path

from . import views

app_name= "edicion_noticias"

urlpatterns = [
    path('admin/edicion', views.ListadoNoticias.as_view(), name= 'admin_edicion_noticias'),
    path('admin/agregar', views.NuevaNoticia.as_view(), name= 'NuevaNoticia'),
]