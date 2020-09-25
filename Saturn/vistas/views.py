from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    return render(request, "dashboard.html")

def turnos(request):
	return render(request, "turnos.html")

def panelusuario(request):
	return render(request, "panelusuario.html")