from django.urls import path, include
from turnos import views


urlpatterns=[
    path('new_turn/', views.new_turn, name='new_turn'),
    path('turn_ok/', views.turn_ok, name='turn_ok'),
]