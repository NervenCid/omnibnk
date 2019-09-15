from django.shortcuts import render, redirect

#Importamos el modulo de mensajes
from django.contrib import messages

#Importamos 
from .forms import UserRegisterForm

#Creamos las vistas para usuario

#Registro
def register(request):
    #Validamos el usuario
    if request.method == 'POST':
        #Creamos el formulario de registro
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #Guardamos el usuario
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para el usuario {username}')
            return redirect('movies-home')
    else:
        form = UserRegisterForm()    

    #Renderizamos en una vista
    return render(request, 'users/register.html', {'form': form})
