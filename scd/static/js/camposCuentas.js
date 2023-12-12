document.addEventListener('DOMContentLoaded', function () {
    const togglePassword = document.querySelector('.toggle-password');
    const passwordField = document.querySelector('#id_password');
    const usernameField = document.querySelector('#id_username');
    //
    const password1Field = document.querySelector('#id_password1');
    const password2Field = document.querySelector('#id_password2');
    const showPasswordCheckbox = document.getElementById('flexSwitchCheckReverse'); //show-password
    const passwordFields = document.querySelectorAll('[type="password"]');
    const togglePasswordIcons = document.querySelectorAll('.toggle-password');
    const nombreField = document.querySelector('#id_nombre');
    const apellidoField = document.querySelector('#id_apellido');
    const emailField = document.querySelector('#id_correo_electronico');
    //
    const grupo0Radio = document.querySelector('#id_group_0');
    const grupo1Radio = document.querySelector('#id_group_1');
    
    // USERNAME (Está en signup y signin)
    usernameField.classList.add('form-control', 'border-dark');
    usernameField.setAttribute('autocomplete', 'off');
    
    // SIGNIN
    if (passwordField) {
        passwordField.classList.add('form-control', 'border-dark');
        togglePassword.addEventListener('click', function () {
            const fieldType = passwordField.getAttribute('type');
            passwordField.setAttribute('type', fieldType === 'password' ? 'text' : 'password');
            this.classList.toggle('bi-eye-slash-fill');
        });
    }

    // SIGNUP
    if (nombreField && apellidoField && emailField && password1Field && password2Field) {
        password1Field.classList.add('form-control', 'border-dark');
        password2Field.classList.add('form-control', 'border-dark');
        nombreField.classList.add('form-control', 'border-dark');
        nombreField.setAttribute('autocomplete', 'off');
        apellidoField.classList.add('form-control', 'border-dark');
        apellidoField.setAttribute('autocomplete', 'off');
        emailField.classList.add('form-control', 'border-dark');
        emailField.setAttribute('autocomplete', 'off');
        grupo0Radio.classList.add('form-check-input');
        grupo1Radio.classList.add('form-check-input');
        //
        showPasswordCheckbox.addEventListener('change', function () {
            const passwordType = this.checked ? 'text' : 'password';
            passwordFields.forEach(function (field) {
                field.setAttribute('type', passwordType);
            });
            /*togglePasswordIcons.forEach(function (icon) {
                icon.classList.toggle('fa-eye-slash', !this.checked);
            }, this);*/
        });
    
        /*togglePasswordIcons.forEach(function (icon) {
            icon.addEventListener('click', function () {
                const fieldType = this.previousElementSibling.getAttribute('type');
                this.previousElementSibling.setAttribute('type', fieldType === 'password' ? 'text' : 'password');
                this.classList.toggle('fa-eye-slash');
            });
        });*/
    }
});