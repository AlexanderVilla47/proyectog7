from django.urls import path

from . import views

app_name= "edicion_noticias"

urlpatterns = [
    path('admin/edicion', views.admin_edicion_noticias, name= 'admin_edicion_noticias'),
]