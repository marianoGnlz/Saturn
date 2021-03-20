from django.shortcuts import render,redirect
from turnos.forms import TurnoForm
from turnos.models import Turno, EspecialidadMedico, Medico, ConfiguracionHoraria
from users.models import Registro
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


import datetime
from django.http import request

# Create your views here.
def new_turn(request):

    form = TurnoForm()
    if request.method == "POST":
        form = TurnoForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            instancia = form.save(commit=False)

            date_time_str = request.POST['hora_turno'] + ':00.000000'
            date_time_obj = datetime.datetime.strptime(date_time_str, '%H:%M:%S.%f')


            instancia.hora_turno = date_time_obj.time()
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
    fecha_seleccionada = request.GET.get('fecha_seleccionada')
    dia_seleccionado = request.GET.get('dia_seleccionado')
    dia = dia_seleccionado.capitalize()
    horario_medico = ConfiguracionHoraria.objects.filter(nombredia__contains=dia, medico_id=id_medico)
    #fecha_seleccionada = '2020-09-25'
    horarios_array = []

    for hm in horario_medico:
        hora_desde = hm.hora_desde.hour
        hora_hasta = hm.hora_hasta.hour

        i = hora_desde
        while i < hora_hasta:
            j = 0
            while j < 60:
                hora_final = str(i).zfill(2) + ':' + str(j).zfill(2)
                encontrados = Turno.objects.filter(fecha_turno=fecha_seleccionada, hora_turno=hora_final).count()
                if encontrados == 0:
                    horarios_array.append(hora_final)
                j = j + hm.duracion
            i = i + 1


    contexto = {
        'horarios_array':horarios_array
        }
    return render(request, "combo_horario.html", contexto)

def turn_ok(request):
    registro = Registro.objects.get(email=request.user)
    turno = Turno.objects.filter(usuario_id=registro.idUsuario)
    paginator = Paginator(turno, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        turnos = paginator.page(page)
    except(EmptyPage, InvalidPage):
        turnos = paginator.page(paginator.num_pages)

    contexto = {
        'turno': turnos,
        }
    return render(request, "turn_ok.html",contexto)

@login_required(login_url='login')
def listado_del_dia(request):
    medicos = Medico.objects.all()
    now = datetime.datetime.now().date()
    nombre_medico = ''

    turnos_del_dia = []

    if request.method == "POST":
        medico_select = request.POST['listado_medico']

        medico = Medico.objects.get(medicoId=medico_select)
        nombre_medico = medico.nombre
        turnos_del_dia = Turno.objects.filter(fecha_turno=now, medico_id=medico_select).order_by('-TurnoId')

    contexto = {
        'medicos':medicos,
        'turnos_del_dia':turnos_del_dia,
        'nombre_medico':nombre_medico
    }
    # Si llegamos al final renderizamos el formulario
    return render(request, "listado_del_dia.html", contexto)

def delete_turn(request,TurnoId):
    idturno= Turno.objects.get(TurnoId=TurnoId)
    idturno.delete()
    return render(request,"delete_turn.html")

def adicional(request):
    id_obrasocial = request.GET.get('obraSocialId')
    obrasocial_adicional = ObraSocial.objects.get(ObraSocialId=id_obrasocial)
    contexto = {
        'obrasocial_adicional':obrasocial_adicional
    }
    return render(request, "adicional.html", contexto)

def fecha_valida(request):
    id_fecha_turno = request.GET.get('fecha_valida')
    print("fecha del turno:", id_fecha_turno)
    fecha_turno = datetime.datetime.strptime(id_fecha_turno, "%Y-%m-%d").date()
    print("fecha convertida:", fecha_turno)
    now = datetime.datetime.now().date()
    print("Hoy: ", now)

    contexto = {
        'fecha_turno':fecha_turno,
        'now':now
    }
    return render(request, "fecha_valida.html", contexto)

