// Mostrar fecha actual
function setearFechaActual() {
  var fecha = new Date();
  var diasSemana = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
  var nombreDia = diasSemana[fecha.getDay()];
  var dia = fecha.getDate();
  var mes = fecha.toLocaleString('default', { month: 'long' });
  var anio = fecha.getFullYear();
  var fechaFormateada = nombreDia + ', ' + dia + ' de ' + mes + ' del ' + anio;

  // Busca todos los elementos con ID "fecha-actual" y establece el valor
  var elementosFechaActual = document.querySelectorAll('[id^="fecha-actual"]');
  elementosFechaActual.forEach(function(elemento) {
      if (elemento.tagName === 'INPUT' || elemento.tagName === 'TEXTAREA') {
          elemento.value = fechaFormateada;
      } else {
          elemento.textContent = fechaFormateada;
      }
  });
}

// Llama a la función cuando se carga la página
document.addEventListener('DOMContentLoaded', setearFechaActual);


// ----------------------------------------------------
// Esto permite visualizar los tooltips de Bootstrap
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// ----------------------------------------------------
// Esto permite visualizar los Modals de Bootstrap
const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})