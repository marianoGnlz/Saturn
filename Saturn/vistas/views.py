from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Registro


@login_required(login_url='login')
def dashboard(request):
    return render(request, "dashboard.html")
