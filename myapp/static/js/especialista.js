function volverEspecialista(){
    window.location.href = '/Especialista';
}

function verPerfil() {
    window.location.href = '/Especialista/Perfil/';
}

function verLista() {
    window.location.href = '/Especialista/Lista_de_espera/';
}


function IrNotificar() {
    window.location.href = '/Especialista/Notificar/';
    
}
function Notificar(){
      // Mostrar alerta de notificación
      alert("Notificación realizada");

      // Esperar 5 segundos antes de redirigir
      setTimeout(function() {
          // Redirigir a otra página
          window.location.href = "/Especialista/Lista_de_espera/";
      }, 3000); // 5000 milisegundos = 5 segundos
}
function CerrarSesion() {
    window.location.href = '//';
}
