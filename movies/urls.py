#Importamos el modulo 'path'
from django.urls import path

#Importamos la lista de vistas
from .views import PostListView

#Importamos las vistas
from . import views

urlpatterns = [
    #Url a 'home'
    #path('', views.home, name= 'movies-home'),
    path('', PostListView.as_view(), name='movies-home'),
    #Url a 'about'
    path('about/', views.about, name='movies-about'),
]
