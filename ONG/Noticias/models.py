from django.db import models

class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=800)
    imagen = models.ImageField ( upload_to = None , height_field = None , width_field = None , max_length = None ,)
    fecha = models.CharField ( max_length = 10)
    
    def __str__(self):
        return self.titulo
