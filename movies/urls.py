#Importamos el modulo 'path'
from django.urls import path

#Importamos las vistas
from . import views

urlpatterns = [
    #Url a 'home'
    path('', views.home, name= 'movies-home'),
    #Url a 'about'
    path('about/', views.about, name='movies-about'),
]
