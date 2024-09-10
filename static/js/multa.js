
function actualizarHora() {
    const horaElemento = document.getElementById('hora');
    const fecha = new Date();
    const horas = String(fecha.getHours()).padStart(2, '0');
    const minutos = String(fecha.getMinutes()).padStart(2, '0');
    const segundos = String(fecha.getSeconds()).padStart(2, '0');
    horaElemento.textContent = `${horas}:${minutos}:${segundos}`;
}


setInterval(actualizarHora, 1000);


document.getElementById('montoCobrar').addEventListener('input', function (e) {

    let valor = e.target.value.replace(/[^0-9,]/g, '');


    const partes = valor.split(',');


    partes[0] = partes[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');


    e.target.value = partes.join(',');
});


document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();  
    window.history.back();  
});

