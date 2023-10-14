// Mostrar fecha actual
document.addEventListener('DOMContentLoaded', function() {
  // Obtener la fecha actual
  var fecha = new Date();
  var dia = fecha.getDate();
  var mes = fecha.toLocaleString('default', { month: 'long' });
  var anio = fecha.getFullYear();
  var fechaFormateada = dia + ' de ' + mes + ' del ' + anio;
  // Actualizar el contenido del elemento HTML con la fecha
  var elementoFecha = document.getElementById('fecha-actual');
  if (elementoFecha) {
      elementoFecha.innerHTML = fechaFormateada;
  }
});

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