
document.addEventListener('DOMContentLoaded', function() {
                
    var map = L.map('map').setView([-31.4201, -64.1888], 8); 

    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    
    var peajes = [
    {nombre: 'Peaje Piedras Moras', lat: -32.1844, lon: -64.2562},
    {nombre: 'Peaje Arroyo Tegua', lat: -32.6789, lon: -64.7844},
    {nombre: 'Peaje Toledo', lat: -31.5244, lon: -64.0089},
    {nombre: 'Peaje Ruta 36', lat: -31.8711, lon: -64.2089},
    {nombre: 'Peaje Ruta 9 Norte', lat: -31.2114, lon: -64.3911},
    {nombre: 'Peaje Ruta 19', lat: -31.4131, lon: -64.0717},
    {nombre: 'Peaje Carretera 5', lat: -31.8017, lon: -64.2392},
    {nombre: 'Peaje Carretera 6', lat: -32.4214, lon: -63.6114},
    {nombre: 'Peaje Autopista Córdoba - Rosario', lat: -31.7167, lon: -63.9833}];
    peajes.forEach(function(peaje) {
        L.marker([peaje.lat, peaje.lon]).addTo(map)
            .bindPopup(peaje.nombre);
    });
});