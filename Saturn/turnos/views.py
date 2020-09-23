from django.shortcuts import render,redirect
from turnos.forms import TurnoForm
from turnos.models import Turno, EspecialidadMedico, Medico, ConfiguracionHoraria
from users.models import Registro
from vistas import views
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def login(request):
    return render(request, "login.html")
    
def new_turn(request):

    form = TurnoForm()
    if request.method == "POST":
        form = TurnoForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
         
            instancia = form.save(commit=False)
            instancia.usuario = Registro.objects.get(email=request.user)
            instancia.save()

            return redirect('/turn_ok')
    # Si llegamos al final renderizamos el formulario
    return render(request, "new_turn.html", {'form': form})  

def combo_medico(request):
    medico_esp = []
    id_especialidad = request.GET.get('id_especialidad')
    medico_esp = EspecialidadMedico.objects.filter(especialidad_id=id_especialidad)
    contexto = {
        'medico_esp':medico_esp
    }
    return render(request, "combo_medico.html", contexto)

def combo_horario(request):  
    id_medico = request.GET.get('id_medico')
    print("Id_medico:", id_medico)
    medico_dias = ConfiguracionHoraria.objects.filter(medico_id=id_medico)
    print("MEDICO = ", medico_dias)
    contexto = {
        'medico_dias':medico_dias
    }
    return render(request, "combo_dias.html", contexto)

def turn_ok(request):    
    registro = Registro.objects.get(email=request.user)
    turno = Turno.objects.filter(usuario_id=registro.idUsuario)
    contexto = {
        'turno':turno,
        }
    return render(request, "turn_ok.html",contexto) 