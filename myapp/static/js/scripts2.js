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
});
