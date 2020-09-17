from django import forms
from users.models import Registro

class RegistroForm(forms.ModelForm):
    
    class Meta:
        model = Registro
        fields = [
            "email",
            "password",
            "nombre",
            "apellido",
            "dni",
            "telefono",
            "fechaDeNacimiento",
            "sexo"
        ]
        label = {
            'email': 'Email',
            'password': 'Contraseña',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'dni': 'Ingrese su DNI',
            'telefono': 'Telefono',
            'fechaDeNacimiento': 'Fecha de Nacimiento',
            'sexo': 'Sexo'
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'fechaDeNacimiento': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'sexo': forms.RadioSelect(attrs={'class':'form-check-input mb-3 mt-2'})
        }
        
