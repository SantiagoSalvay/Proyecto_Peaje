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

    boxes.forEach(box => {
        box.addEventListener('click', function() {
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

            // Generar la factura
            const url = `/generar-factura/?vehiculo=${vehicle}&importe=${price}`;
            window.location.href = url;
        }); 
    });
});
