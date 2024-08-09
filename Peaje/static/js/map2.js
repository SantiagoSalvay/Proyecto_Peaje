document.addEventListener('DOMContentLoaded', function() {
    var mapSucursal = L.map('map-sucursal').setView([-31.4201, -64.1888], 8); 

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mapSucursal);

    var sucursales = [
        {nombre: 'Sucursal Villada', lat: -31.36231, lon: -64.27634},
        {nombre: 'Sucursal Valle Mall', lat: -31.37798, lon: -64.27771},
        {nombre: 'Sucursal Patio Olmos', lat: -31.41978, lon: -64.18821}
    ];

    sucursales.forEach(function(sucursal) {
        L.marker([sucursal.lat, sucursal.lon]).addTo(mapSucursal)
            .bindPopup(sucursal.nombre);
    });
});