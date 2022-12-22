from django.db import models

class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=8000)
    fecha = models.CharField ( max_length = 10)
    
    activo= models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
