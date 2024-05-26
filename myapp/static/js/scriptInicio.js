document.addEventListener('DOMContentLoaded', function() {
    // Agregar animaciones a los enlaces del menú
    let menuLinks = document.querySelectorAll('.menu a, .button');
    menuLinks.forEach(function(link) {
        link.addEventListener('mouseover', function() {
            link.style.transform = 'scale(1.05)';
        });
        link.addEventListener('mouseout', function() {
            link.style.transform = 'scale(1)';
        });
    });

    // Agregar animaciones a los botones del formulario
    let formButtons = document.querySelectorAll('form button');
    formButtons.forEach(function(button) {
        button.addEventListener('mouseover', function() {
            button.style.transform = 'scale(1.05)';
        });
        button.addEventListener('mouseout', function() {
            button.style.transform = 'scale(1)';
        });
    });
    
    // Verificación de edad
    document.getElementById('fechaNacimiento').addEventListener('change', checkAge);
    document.getElementById('rut').addEventListener('input', formatRUT);
    document.getElementById('registrarBtn').addEventListener('click', validateForm);
});

function checkAge() {
    var dob = new Date(document.getElementById('fechaNacimiento').value);
    var today = new Date();
    var age = today.getFullYear() - dob.getFullYear();
    var m = today.getMonth() - dob.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < dob.getDate())) {
        age--;
    }
    if (age < 18) {
        document.getElementById('registrarBtn').disabled = true;
        alert("Debe tener al menos 18 años para registrarse.");
    } else {
        document.getElementById('registrarBtn').disabled = false;
    }
}

function formatRUT() {
    var input = document.getElementById('rut');
    var rut = input.value.replace(/\D/g, '');

    if (rut.length > 9) {
        rut = rut.slice(0, 9);
    }

    var parts = [];
    if (rut.length > 2) {
        parts.push(rut.substring(0, 2));
        if (rut.length > 5) {
            parts.push(rut.substring(2, 5));
            parts.push(rut.substring(5, 8));
            parts.push(rut.substring(8));
        } else if (rut.length > 2) {
            parts.push(rut.substring(2));
        }
    } else {
        parts.push(rut);
    }
    input.value = parts.join('.').replace(/\.(?=[^.]*$)/, '-');
}

function validateForm() {
    var contraseña = document.getElementById('contraseña').value;
    var confirmarContraseña = document.getElementById('confirmarContraseña').value;

    if (contraseña !== confirmarContraseña) {
        alert('Las contraseñas no coinciden');
        return false;
    }

    var fechaNacimiento = new Date(document.getElementById('fechaNacimiento').value);
    var hoy = new Date();
    var edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
    var m = hoy.getMonth() - fechaNacimiento.getMonth();
    if (m < 0 || (m === 0 && hoy.getDate() < fechaNacimiento.getDate())) {
        edad--;
    }
    if (edad < 18) {
        alert('Debe tener al menos 18 años de edad');
        return false;
    }

    alert('Paciente Registrado');
    return true;
}

function limpiarFormulario() {
    document.querySelector('form').reset();
}

function volver() {
    window.history.back();
}
