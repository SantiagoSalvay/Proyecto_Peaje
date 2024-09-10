document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const numeroCasilla = urlParams.get('casilla');
    document.getElementById('numero-casilla').textContent = numeroCasilla;

    function actualizarHora() {
        const horaActual = new Date().toLocaleTimeString();
        document.getElementById('hora-actual').textContent = horaActual;
    }

    setInterval(actualizarHora, 1000);
    actualizarHora();

    document.querySelector('.btn-volver').addEventListener('click', function() {
        history.back();
    });

    const inputDinero = document.getElementById('dinero-actual');
    inputDinero.addEventListener('input', function(event) {
        let value = event.target.value;

        
        value = value.replace(/[^\d,]/g, '');

        
        value = value.replace(/\./g, '').replace(/,/g, '');

        
        const number = parseInt(value, 10);

        if (!isNaN(number)) {
            const formattedValue = new Intl.NumberFormat('es-ES', {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            }).format(number / 100);

            event.target.value = formattedValue;
        }
    });


    const volverButton = document.getElementById('volverButton');
    volverButton.addEventListener('click', function() {

        window.location.href = 'casilla/'; 
    });
    
    
});