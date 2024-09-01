// js/casilla.js
document.addEventListener("DOMContentLoaded", function() {
    const casillas = document.querySelectorAll('.casilla');

    casillas.forEach((casilla, index) => {
        casilla.querySelector('.numero').textContent = index + 1;

        // Agregar evento de clic para redirigir a la página de detalle de casilla
        casilla.addEventListener('click', function() {
            const numeroCasilla = index + 1;
            // Redirigir a la nueva página con el número de casilla en la URL
            window.location.href = `${comienzaTurnoUrl}?casilla=${numeroCasilla}`;
        });
    });
});
