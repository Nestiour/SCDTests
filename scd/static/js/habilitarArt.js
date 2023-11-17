document.addEventListener('DOMContentLoaded', function() {
    var asistencias = document.querySelectorAll('.asistencia');
    var articulos = document.querySelectorAll('.articulo');
    var clases = document.querySelectorAll('.id_cla');

    // Función para gestionar los campos basándose en el valor de asistencia
    function gestionarCampos() {
        asistencias.forEach(function(asistencia, index) {
            var asistenciaSeleccionada = asistencia.value;
            var mostrarArticulos = asistenciaSeleccionada === 'A';
            var mostrarClases = asistenciaSeleccionada !== 'A';

            articulos[index].parentNode.style.display = mostrarArticulos ? 'block' : 'none';
            articulos[index].required = mostrarArticulos;

            clases[index].parentNode.style.display = true ? 'block' : 'none';
            clases[index].required = true;
            /*clases[index].parentNode.style.display = mostrarClases ? 'block' : 'none';
            clases[index].required = mostrarClases;*/
        });
    }

    // Agrega eventos de cambio a los elementos relevantes usando un bucle
    asistencias.forEach(function(asistencia) {
        asistencia.addEventListener('change', gestionarCampos);
    });

    // Llama a la función para gestionar los campos cuando se carga la página
    gestionarCampos();
});


/*document.addEventListener('DOMContentLoaded', function() {
    var asistenciaSelect = document.getElementById('asistencia');
    var articuloInput = document.getElementById('articulo');
    var claseSelect = document.getElementById('id_cla');

    // Función para gestionar los campos basándose en el valor de asistencia
    function gestionarCampos() {
        if (asistenciaSelect.value === 'A') {
            articuloInput.parentNode.style.display = 'block';
            articuloInput.required = true;
            claseSelect.parentNode.style.display = 'none';
            claseSelect.required = false;
        } else if (asistenciaSelect.value === 'P') {
            articuloInput.parentNode.style.display = 'none';
            articuloInput.required = false;
            claseSelect.parentNode.style.display = 'block';
            claseSelect.required = true;
        } else {
            articuloInput.parentNode.style.display = 'none';
            articuloInput.required = false;
            claseSelect.parentNode.style.display = 'block';
            claseSelect.required = true;
        }
    }

    // Agrega eventos de cambio a los elementos relevantes
    asistenciaSelect.addEventListener('change', gestionarCampos);
    articuloInput.addEventListener('change', gestionarCampos);
    claseSelect.addEventListener('change', gestionarCampos);
});*/