#Importamos el modulo 'path'
from django.urls import path

#Importamos la lista de vistas
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView)

#Importamos las vistas
from . import views

urlpatterns = [
    #Url a 'home'
    #path('', views.home, name= 'movies-home'),
    path('', PostListView.as_view(), name='movies-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    #Url a 'about'
    path('about/', views.about, name='movies-about'),
]
