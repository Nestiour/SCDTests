document.addEventListener('DOMContentLoaded', function() {
    var inputHi = document.getElementById('h_i');
    var inputHf = document.getElementById('h_f');
    var aviso = document.getElementById('aviso-modulo');
    var formulario = document.querySelector('form');

    // Ocultar el aviso por defecto
    aviso.style.display = 'none';

    // Agregar evento de cambio a los inputs
    /*inputHi.addEventListener('input', comprobarModulo);
    inputHf.addEventListener('input', comprobarModulo);*/

    // Agregar eventos de entrada a los inputs
    inputHi.addEventListener('input', validarNumero);
    inputHf.addEventListener('input', validarNumero);

    // Función para validar que solo se ingresen números del 1 al 7
    function validarNumero(event) {
        var valor = event.target.value;
        // Utilizar una expresión regular para permitir solo dígitos del 1 al 7
        var esNumeroValido = /^[1-7]$/.test(valor);

        if (!esNumeroValido) {
            // Si el número ingresado no es válido, eliminar el último carácter
            event.target.value = valor.slice(0, -1);
        } else {
            comprobarModulo();
        }
    }

    // Agregar evento al formulario para prevenir el envío si h_f es menor que h_i
    formulario.addEventListener('submit', function(event) {
        if (parseInt(inputHf.value) < parseInt(inputHi.value)) {
            // Mostrar aviso si se intenta enviar el formulario con h_f menor que h_i
            aviso.style.display = 'block';
            event.preventDefault(); // Evitar el envío del formulario
        }
    });

    // Función para comprobar los módulos y mostrar/ocultar el aviso
    function comprobarModulo() {
        // Validar que ambos inputs tengan valores numéricos antes de la comparación
        var hi = inputHi.value
        var hf = inputHf.value
        if (hi && hf) {
            // Comprobar que h_f sea >= que h_i y permitir solo nros del 1 al 7
            if (hf >= hi && validarIngreso(hi) && validarIngreso(hf)) {
                aviso.style.display = 'none';
            } else {
                aviso.style.display = 'block';
            }
        } else {
            aviso.style.display = 'none';
        }
    }

    // Función para verificar si un número es válido (entre 1 y 7)
    function validarIngreso(numero) {
        return /^[1-7]$/.test(numero);
    }
});