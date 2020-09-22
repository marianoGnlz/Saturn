from django import forms
from turnos.models import Turno,ObraSocial,Medico,Especialidad
from django.core.exceptions import ValidationError

class MedicoModelChoiceField(forms.ModelChoiceField):
    def to_python(self, value):
        key = self.to_field_name or 'pk'
        value = Medico.objects.filter(**{key: value})
        if not value.exists():
            raise ValidationError(self.error_messages['invalid_choice'], code='invalid_choice')
        else:
            value= value.first()
        return value

class TurnoForm(forms.ModelForm):
    medico = MedicoModelChoiceField(queryset=Medico.objects.none())
    class Meta:
        model = Turno
        

        fields = [
            'fecha_turno',
            'especialidad', 
            'medico',
            'obrasocial',           
            'nombre',
            'dni',
            'edad',
            'telefono',
            'mail',            
            'sexo',            
        ]
        label = {
            'fecha_turno':'fecha_turno',
            'especialidad':'Especialidad',            
            'medico':'Medico',
            'obrasocial':'Obra Social',           
            'nombre':'Nombre',
            'dni':'DNI',
            'edad':'Edad',
            'telefono':'Teléfono',
            'mail':'Email',
            'sexo':'Sexo',            
        }
        widgets = {
            'fecha_turno':forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),    
            'fecha_registro':forms.DateInput(attrs={'class':'form-control'}),
            'especialidad':forms.Select(attrs={'class':'form-control'}),
            'medico':forms.Select(attrs={'class':'form-control'}),
            'obrasocial':forms.Select(attrs={'class':'form-control'}),      
            'nombre':forms.TextInput(attrs={'class':'form-control'}), 
            'dni':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.NumberInput(attrs={'class':'form-control datepicker'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),       
            'mail':forms.TextInput(attrs={'class':'form-control'}),      
            'sexo':forms.Select(attrs={'class':'form-control'}),        
        }

      