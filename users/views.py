from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login(request):
    return render(request, 'registration/login.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('perfil')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtelo de nuevo.')
            return render(request, 'registration/inicio_sesion.html')
    else:
        return render(request, 'registration/inicio_sesion.html')

def perfil(request):
    return render(request, 'registration/perfil.html')
