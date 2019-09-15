from django.contrib import admin

#Importamos los modelos
from .models import Post

#Registramos los modelos dentro del 'admin'
admin.site.register(Post)