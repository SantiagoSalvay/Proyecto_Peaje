document.addEventListener("DOMContentLoaded", function() {
    function updateTime() {
        const now = new Date();
        const timeString = now.toLocaleTimeString();
        document.getElementById('currentTime').textContent = timeString;
    }

    setInterval(updateTime, 1000);
    updateTime();

    const boxes = document.querySelectorAll('.box');
    const vehicleTypeElement = document.getElementById('vehicleType');
    const vehiclePriceElement = document.getElementById('vehiclePrice');

    const urlParams = new URLSearchParams(window.location.search);
    const numeroCasilla = urlParams.get('casilla');
    const sentidoCobro = urlParams.get('sentido');


    if (document.getElementById('numero-casilla')) {
        document.getElementById('numero-casilla').textContent = numeroCasilla;
    }

    if (document.getElementById('sentido-cobro')) {
        document.getElementById('sentido-cobro').textContent = sentidoCobro;
    }

    boxes.forEach(box => {
        box.addEventListener('click', async function() {
            const vehicle = box.getAttribute('data-vehicle');
            const price = box.getAttribute('data-price');

            vehicleTypeElement.textContent = vehicle;
            vehiclePriceElement.textContent = `$${price}`;

            const successMessage = document.createElement('p');
            successMessage.textContent = "Cobrado con éxito!";
            successMessage.classList.add('message-success');
            vehiclePriceElement.parentNode.appendChild(successMessage);

            setTimeout(() => {
                vehicleTypeElement.textContent = '';
                vehiclePriceElement.textContent = '';
                successMessage.remove();
            }, 13000);

            try {
                const response = await fetch(`/generar-factura/?vehiculo=${vehicle}&importe=${price}`, {
                    method: 'GET'
                });

                if (response.ok) {
                    const blob = await response.blob();
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `factura_${vehicle}.pdf`; 
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                    a.remove();
                } else {
                    console.error('Error al generar la factura');
                }
            } catch (error) {
                console.error('Error en la solicitud de la factura', error);
            }
        });
    });

    const multarButton = document.getElementById('multarButton');
    multarButton.addEventListener('click', function() {

        window.location.href = '/casilla/comienza-turno/cobro/multa'; 
    });
});
