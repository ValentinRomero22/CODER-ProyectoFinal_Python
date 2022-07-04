from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from electrotienda.forms import Formulario_registro_usuario, UserEditForm
from django.contrib.auth.decorators import login_required

from productos.models import Producto

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
            errors = form.errors 
            form = Formulario_registro_usuario()
            context = {'errors' : errors, 'form' : form}
            return render(request, 'auth/register.html', context = context)

    else: 
        form = Formulario_registro_usuario()
        context = {'form' : form}
        return render(request, 'auth/register.html', context = context)

def index(request):
    productos = Producto.objects.get(id=1)
    for ImagenProducto in productos.images.all():
        return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def contacto_view(request):
    return render(request, 'contacto.html')


def about_us(request):
    return render(request, 'about.html')   


@login_required
def edit_user(request):
    user = request.user 

    if request.method == 'POST':
        form=UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']

            return render (request, 'index.html')
        
    else:
        form = UserEditForm(initial={'email':user.email})
    
    return render (request, 'auth/update_user.html', {'form': form, 'user' : user})
