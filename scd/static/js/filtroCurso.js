$(document).ready(function() {
    // Función para filtrar la tabla
    function filtrarTabla() {
        var inputAnio = $('#cuadro-busqueda-cur-anio').val().toUpperCase();
        var inputDiv = $('#cuadro-busqueda-cur-div').val().toUpperCase();
        var inputEspec = $('#cuadro-busqueda-cur-esp').val().toUpperCase();
        var inputTurn = $('#cuadro-busqueda-cur-tur').val().toUpperCase();

        // Iterar sobre las filas de la tabla
        $('#tabla-curso-registros tbody tr').each(function() {
            var anio = $(this).find('td:eq(2)').text().toUpperCase();
            var div = $(this).find('td:eq(3)').text().toUpperCase();
            var espec = $(this).find('td:eq(4)').text().toUpperCase();
            var turn = $(this).find('td:eq(5)').text().toUpperCase();

            // Comprobar si la fila coincide con los criterios de búsqueda
            if (
                anio.includes(inputAnio) &&
                div.includes(inputDiv) &&
                espec.includes(inputEspec) &&
                turn.includes(inputTurn)
            ) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    }

    // Asigna eventos a los campos de búsqueda
    $('#cuadro-busqueda-cur-anio, #cuadro-busqueda-cur-div, #cuadro-busqueda-cur-esp, #cuadro-busqueda-cur-tur').on('input', function() {
        filtrarTabla();
    });
});