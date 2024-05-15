document.addEventListener("DOMContentLoaded", function() {
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