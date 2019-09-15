from django.shortcuts import render

#Importamos un modulo que facilita la creacion de usuarios
from django.contrib.auth.forms import UserCreationForm


#Creamos las vistas para usuario

#Registro
def register(request):
    #Creamos el formulario de registro
    form = UserCreationForm()
    #Renderizamos en una vista
    return render(request, 'users/register.html', {'form': form})
