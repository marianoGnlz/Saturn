from django.shortcuts import render, redirect

def welcome(request):
    return render(request, "welcome.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    # Redireccionamos a la portada
    return redirect('/')
