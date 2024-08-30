document.addEventListener("DOMContentLoaded", function() {
    // Seleccionar todos los botones con la clase "casilla"
    const casillas = document.querySelectorAll('.casilla');

    // Asignar números del 1 al 10 a cada casilla
    casillas.forEach((casilla, index) => {
        casilla.querySelector('.numero').textContent = index + 1; // Números del 1 al 10
    });
});
