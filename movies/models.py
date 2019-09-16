#Importamos el modulo para modelos
from django.db import models
#Importamos el modulos para autenticacion de usuarios
from django.contrib.auth.models import User
#Importamos el modulo 'reverse'
from django.urls import reverse

#Creamos el modelo de Post de las peliculas
class Post(models.Model):
    movie_name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=1000)
    director = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    date = models.CharField(max_length=10)
    #Definimos al autor como llave foranea
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #
    def __str__(self):
        return self.movie_name

    #Usamos la absolute_url para redireccionar apropiadamente despues de crear el post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
