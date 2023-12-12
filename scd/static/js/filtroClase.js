$(document).ready(function() {
    // Función para filtrar la tabla
    function filtrarTabla() {
        function removerSignos(input) {
            // Usa una expresión regular para eliminar o reemplazar caracteres especiales
            return input.normalize("NFD").replace(/[^\w\s]|_/g, "").replace(/\s+/g, ' ');
        }

        var inputDia = removerSignos($('#cuadro-busqueda-clase-dia').val());
        var inputNombre = removerSignos($('#cuadro-busqueda-clase-nombre').val());
        var inputMateria = removerSignos($('#cuadro-busqueda-clase-materia').val());
        var inputCurso = removerSignos($('#cuadro-busqueda-clase-curso').val());
        var inputTurno = removerSignos($('#cuadro-busqueda-clase-turno').val());

        // Iterar sobre las filas de la tabla
        $('#tabla-clase-registros tbody tr').each(function() {
            var dia = removerSignos($(this).find('td:eq(2)').text());
            var nombre = removerSignos($(this).find('td:eq(3)').text());
            var materia = removerSignos($(this).find('td:eq(4)').text());
            var curso = removerSignos($(this).find('td:eq(5)').text());
            var turno = removerSignos($(this).find('td:eq(6)').text());

            // Comprobar si la fila coincide con los criterios de búsqueda
            if (
                dia.includes(inputDia) &&
                nombre.includes(inputNombre) &&
                materia.includes(inputMateria) &&
                curso.includes(inputCurso) &&
                turno.includes(inputTurno)
            ) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    }

    // Asigna eventos a los campos de búsqueda
    $('#cuadro-busqueda-clase-dia, #cuadro-busqueda-clase-nombre, #cuadro-busqueda-clase-materia, #cuadro-busqueda-clase-curso, #cuadro-busqueda-clase-turno').on('input', function() {
        filtrarTabla();
    });
});