function actualizarHora() {
    const ahora = new Date();
    const horas = ahora.getHours().toString().padStart(2, '0');
    const minutos = ahora.getMinutes().toString().padStart(2, '0');
    const segundos = ahora.getSeconds().toString().padStart(2, '0');
    const horaActual = `${horas}:${minutos}:${segundos}`;

    document.getElementById('hora-actual').textContent = horaActual;
}


actualizarHora();

setInterval(actualizarHora, 1000);

const terminarButton = document.getElementById('terminarButtom');
    terminarButton.addEventListener('click', function() {
        window.location.href = 'http://127.0.0.1:8000';  
    });