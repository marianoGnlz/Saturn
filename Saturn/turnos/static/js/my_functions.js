
$( document ).ready(function() {

    var id_especialidad = $("#id_especialidad").val()

    if (id_especialidad !== undefined || id_especialidad !== '') {
        armarComboMedico();
    }

    $("#imprimirListadoTurnos").click(function(){
       
        $("#areaImprimirTurnos").printArea();      
    });
});

$(function() {
    $('select[name="especialidad"]').on('change', function() {
        armarComboMedico();
    });
    $('select[name="medico"]').on('change', function() {
        armarHorario();
    });
    $('input[name="fecha_turno"]').on('change', function() {
        armarComboMedico();
    });
    $('select[name="obrasocial"]').on('change', function() {
        adicional();
    });
    $('input[name="fecha_turno"]').on('change', function() {
        fecha_valida();
    });
});


function armarComboMedico(){
    var id_especialidad = $("#id_especialidad").val()
    if (id_especialidad === undefined || id_especialidad == '') {
        console.log("Variable indefinida")
     }
     else {
        $.ajax({
            url: '/combo_medico/?id_especialidad=' + id_especialidad,
            success: function(respuesta) {
                $("#id_medico").html(respuesta)
    
            },
            error: function() {
                console.log("No se ha podido obtener la información");
            }
        });
    }   
}

function adicional(){
    var obraSocialId = $("#id_obrasocial").val()
    if (id_obrasocial === undefined || id_obrasocial == '') {
        console.log("Variable indefinida")
     }
     else {
        $.ajax({
            url: '/adicional/?obraSocialId=' + obraSocialId,
            success: function(respuesta) {
                $("#adicional").html(respuesta)
            },
            error: function() {
                console.log("No se ha podido obtener la información");
            }
        });
    }   
}

function fecha_valida(){
    var fecha_valida = $("#id_fecha_turno").val()
    if (fecha_valida === undefined || fecha_valida == '') {
        console.log("Variable indefinida")
     }
     else {
        $.ajax({
            url: '/fecha_valida/?fecha_valida=' + fecha_valida,
            success: function(respuesta) {
                $("#fecha_valida").html(respuesta)
            },
            error: function() {
                console.log("No se ha podido obtener la información");
            }
        });
    }   
}

function armarHorario(){
    var id_medico = $("#id_medico").val()
    var id_fecha_turno = $("#id_fecha_turno").val()

    moment.locale('es');
    var dia = moment($('#id_fecha_turno').val()).format('dddd');

    
    $.ajax({
        url: '/combo_horario/?id_medico=' + id_medico+'&fecha_seleccionada=' + id_fecha_turno+'&dia_seleccionado=' + dia,

        success: function(respuesta) {
            $("#id_hora_turno").html(respuesta)
        },
        error: function() {
            console.log("No se ha podido obtener la información");
        }
    });
}
