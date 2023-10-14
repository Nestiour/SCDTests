// ----- ----- ----- ----- ----- ----- ----- ----- -----
// Funciones para evitar el ingreso incorrecto de datos
// Funcion para permitir solo números
function validarSoloNumeros(input) {
    input.addEventListener("input", function(event) {
      var inputValue = event.target.value;
      var numericValue = inputValue.replace(/[^0-9]/g, "");
      event.target.value = numericValue;
    });
  }
  // Obtener los elementos
  var txtDni = document.getElementById("txtDni");
  var txtTelefono = document.getElementById("txtTelefono");
  // Aplicar funcion a los campos
  validarSoloNumeros(txtDni);
  validarSoloNumeros(txtTelefono);
  
  // ----- ----- ----- ----- ----- ----- ----- ----- -----
  // Funcion permitir solo letras
  function validarSoloLetras(input) {
    input.addEventListener("input", function(event) {
      var inputValue = event.target.value;
      var lettersOnlyValue = inputValue.replace(/[^\p{L}\s]/gu, "");
      event.target.value = lettersOnlyValue;
    });
  }
  //
  var txtApellido = document.getElementById("txtApellido");
  var txtNombre = document.getElementById("txtNombre");
  //
  validarSoloLetras(txtApellido);
  validarSoloLetras(txtNombre);