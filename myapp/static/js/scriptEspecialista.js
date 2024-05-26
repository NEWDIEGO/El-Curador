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

    // Supongamos que tienes un objeto usuario con los datos.
    const usuario = {
        nombre: "Juan Pérez",
        fechaNacimiento: "01/01/1990",
        correo: "juan.perez@example.com",
        genero: "Masculino",
        comentario: ""
    };

    // Asignar los datos del usuario a los elementos HTML.
    document.getElementById("nombre").innerText = usuario.nombre;
    document.getElementById("fechaNacimiento").innerText = usuario.fechaNacimiento;
    document.getElementById("correo").innerText = usuario.correo;
    document.getElementById("genero").innerText = usuario.genero;
    document.getElementById("comentario").value = usuario.comentario;
});

function limpiarFormulario() {
    document.querySelector('form').reset();
}

function volver() {
    window.history.back();
}

function listaView() {
    alert("Vista de lista seleccionada");
}

function gridView() {
    alert("Vista de grid seleccionada");
}

function buscarRUT() {
    var rut = document.getElementById('buscar_rut').value;
    alert("Buscar RUT: " + rut); // Reemplazar con lógica de búsqueda real
}

function guardarComentario() {
    const comentario = document.getElementById("comentario").value;
    // Aquí puedes guardar el comentario como lo necesites.
    console.log("Comentario guardado:", comentario);
    alert("Comentario guardado");
}

function limpiarComentario() {
    document.getElementById("comentario").value = "";
}

function loadFile(event) {
    const image = document.getElementById('profileImage');
    image.src = URL.createObjectURL(event.target.files[0]);
    image.style.display = 'block';
}

function csrfSafeMethod(method) {
    // Estos métodos no requieren CSRF
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", jQuery("[name=csrfmiddlewaretoken]").val());
        }
    }
});
