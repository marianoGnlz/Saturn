$(function() {
    $('select[name="especialidad"]').on('change', function() {
        
        var id_especialidad = $("#id_especialidad").val()
        $.ajax({
            url: '/combo_medico/?id_especialidad=' + id_especialidad,
            success: function(respuesta) {
                $("#id_medico").html(respuesta)
            },
            error: function() {
                console.log("No se ha podido obtener la información");
            }
        });
    });
});

$(function() {
    $('select[name="medico"]').on('change', function() {
        
        var id_medico = $("#id_medico").val()
        var id_fecha_turno = $("#id_fecha_turno").val()
        $.ajax({
            url: '/combo_dias/?id_medico=' + id_medico+"&"+ '/?dia_seleccionado=' + id_fecha_turno,

            success: function(respuesta) {
                $("#id_fecha_turno").html(respuesta)
            },
            error: function() {
                console.log("No se ha podido obtener la información");
            }
        });
    });
});
