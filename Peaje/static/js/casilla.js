// js/casilla.js
document.addEventListener("DOMContentLoaded", function() {
    const casillas = document.querySelectorAll('.casilla');

    casillas.forEach((casilla, index) => {
        casilla.querySelector('.numero').textContent = index + 1;


        casilla.addEventListener('click', function() {
            const numeroCasilla = index + 1;
            window.location.href = `${comienzaTurnoUrl}?casilla=${numeroCasilla}`;
        });
    });
});
