/*
    Esta codigo permite encontrar a los Docentes que coincidan con la busqueda y mostrarlos.
    Hace uso de:
        *Un cuadro de texto con id "cuadro-busqueda",
        *El elemento "tr" de una tabla con id "tabla-registros" (para mostrarlos o no)
        *El tr debe tener los artibutos:
            °data-nombre, con valor {{ d.nombre | lower }}
            °data-apellido, con valor {{ d.apellido | lower }}
    Si la variable nombreCompleto que concatena apellido y nombre contiene el termino de busqueda, se muestra,
    de lo contrario, se oculta.
*/
function filtrarRegistros() {
    var cuadroBusqueda = document.getElementById('cuadro-busqueda');
    var tablaRegistros = document.getElementById('tabla-registros').getElementsByTagName('tr');

    var valorBusqueda = cuadroBusqueda.value.toLowerCase();

    for (var i = 0; i < tablaRegistros.length; i++) {
        var registro = tablaRegistros[i];
        var nombre = registro.getAttribute('data-nombre');
        var apellido = registro.getAttribute('data-apellido');

        // Verifica si los atributos data-nombre y data-apellido existen antes de usarlos
        if (nombre && apellido) {
            nombre = nombre.toLowerCase();
            apellido = apellido.toLowerCase();

            var nombreCompleto = apellido + ' ' + nombre;

            if (nombreCompleto.includes(valorBusqueda)) {
                registro.style.display = 'table-row';
            } else {
                registro.style.display = 'none';
            }
        } else {
            // Si los atributos data-nombre o data-apellido están ausentes, muestra la fila
            registro.style.display = 'table-row';
        }
    }
}
// Llamar a la funcion cada vez que cambie el cuadro de entrada
document.addEventListener('DOMContentLoaded', function() {
    var cuadroBusqueda = document.getElementById('cuadro-busqueda');
    cuadroBusqueda.addEventListener('input', filtrarRegistros);
});
// ---

function limpiarBusqueda() {
    var formulario = document.getElementById('miFormulario');
    formulario.reset(); // Esto borra los datos ingresados en el formulario
    filtrarRegistros();
}
// Llamar a las funciones
document.addEventListener('DOMContentLoaded', function() {
    var botonBorrar = document.getElementById('botonBorrar');
    botonBorrar.addEventListener('click', limpiarBusqueda);
});

