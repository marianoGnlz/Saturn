from django.urls import path, include
from vistas import views


urlpatterns=[
    path('dashboard/', views.dashboard, name='dashboard'),
    path('panelusuario/', views.panelusuario, name='panelusuario'),
    path('turnos/', views.turnos, name='turnos'),
]
