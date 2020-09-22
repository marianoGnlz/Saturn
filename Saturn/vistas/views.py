from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Registro

@login_required(login_url='login')
def welcome(request):
    return render(request, "welcome.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    # Redireccionamos a la portada
    return redirect('/')

def dashboard(request):
    return render(request, "dashboard.html")
