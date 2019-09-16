#Importamos el modulo render
from django.shortcuts import render

#Importamos los 'mixin'
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#Importamos el modulo 'HttpResponse'
from django.http import HttpResponse

#Importamos el modulo de lista de vistas
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )

#Importamos los modelos
from .models import Post

#Creamos una lista dummy con los posts 'solo pruebas'
'''
posts = [
    {
        'movie_name': 'Alien',
        'image_url': 'https://m.media-amazon.com/images/M/MV5BMmQ2MmU3NzktZjAxOC00ZDZhLTk4YzEtMDMyMzcxY2IwMDAyXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
        'director': 'Ridley Scott',
        'language': 'English',
        'date':'1979',
    },
    {
        'movie_name': 'The Terminator',
        'image_url': 'https://m.media-amazon.com/images/M/MV5BYTViNzMxZjEtZGEwNy00MDNiLWIzNGQtZDY2MjQ1OWViZjFmXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
        'director': 'James Cameron',
        'language': 'English',
        'date': '1984',
    },
    {
        'movie_name': 'Amelie',
        'image_url': 'http://www.montmartre-guide.com/wp-content/uploads/2014/07/amelie_affiche.jpg',
        'director': 'Jean-Pierre Jeunet',
        'language': 'French',
        'date': '2001',
    },
]
'''

#Creamos las vistas

#Vista 'home'
def home(request):
    #Asignamos el contexto
    context = {
        #Pasamos los datos al contexto
        'posts': Post.objects.all()
    }
    #Renderizamos el archivo 'home.html'
    return render(request, 'movies/home.html', context)

#Vista 'about'
def about(request):
    #Renderizamos el archivo 'about.html'
    return render(request, 'movies/about.html')

#Lista de vistas
class PostListView(ListView):
    model = Post
    #<app>/<model>_<viewtype>.html
    template_name = 'movies/home.html'
    context_object_name = 'posts'
    #Ordenamos los posts
    ordering = ['-date']

#Vista en detalle
class PostDetailView(DetailView):
    model = Post
    
#Vista para crear un post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['movie_name', 'image_url', 'director', 'language', 'date']

    #Validamos
    def form_valid(self, form):
        form.instance.author = self.request.user
        #Ignorar el error de super
        return super().form_valid(form)

#Vista para editar un post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['movie_name', 'image_url', 'director', 'language', 'date']

    #Validamos
    def form_valid(self, form):
        form.instance.author = self.request.user
        #Ignorar el error de super
        return super().form_valid(form)

    #Hacemos un testeo para prevenir que otros usuarios editen post que no fueron creados por ellos
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#Vista para eliminar un post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    #Redirigimos al 'home'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
