$(document).ready(function() {
    // Función para filtrar la tabla
    function filtrarTabla() {
        var inputNombre = $('#cuadro-busqueda-docmat-nombre').val().toUpperCase();
        var inputMateria = $('#cuadro-busqueda-docmat-materia').val().toUpperCase();

        // Iterar sobre las filas de la tabla
        $('#tabla-docmat-registros tbody tr').each(function() {
            var nombre = $(this).find('td:eq(3)').text().toUpperCase();
            var materia = $(this).find('td:eq(6)').text().toUpperCase();

            // Comprobar si la fila coincide con los criterios de búsqueda
            if (
                nombre.includes(inputNombre) &&
                materia.includes(inputMateria)
            ) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    }

    // Asigna eventos a los campos de búsqueda
    $('#cuadro-busqueda-docmat-nombre, #cuadro-busqueda-docmat-materia').on('input', function() {
        filtrarTabla();
    });
});