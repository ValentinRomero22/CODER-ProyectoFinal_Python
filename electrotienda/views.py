from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from electrotienda.forms import Formulario_registro_usuario
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {'message' : f'Bienvenido {username}!'}
                return render(request, 'index.html', context = context)
           
            else:
                context = {'errors' : f'No se encontró ningún usuario con el nombre {username}'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors' : errors, 'form' : form}
            return render(request, 'auth/login.html', context = context)
    
    else:
        form = AuthenticationForm()
        context = {'form' : form}
        return render(request, 'auth/login.html', context = context)

def registro_view(request):
    if request.method == 'POST':
        form = Formulario_registro_usuario(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message' : f'Usuario creado correctamente, bienvenido {username}!'}
            return render(request, 'index.html', context = context)

        else: 
            errors : form.errors
            form = Formulario_registro_usuario()
            context = {'errors' : errors, 'form' : form}
            return render(request, 'auth/register.html', context = context)

    else: 
        form = Formulario_registro_usuario()
        context = {'form' : form}
        return render(request, 'auth/register.html', context = context)

def index(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def contacto_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'contacto.html')
    
    else:
        return redirect('login')


