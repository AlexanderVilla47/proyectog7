
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import inicio
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name='Inicio'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='Iniciar Sesión'),
    path('logout/', auth_views.logout_then_login, name='Logout')
]
