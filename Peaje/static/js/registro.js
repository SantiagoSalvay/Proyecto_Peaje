document.addEventListener('DOMContentLoaded', function() {
    const provincias = {
        "Buenos Aires": ["La Plata", "Mar del Plata", "Bahía Blanca", "Tandil", "Necochea", "Olavarría", "Pergamino", "Luján", "Junín", "San Nicolás"],
        "Córdoba": ["Córdoba", "Villa Carlos Paz", "Río Cuarto", "Villa María", "Alta Gracia", "La Falda", "Cosquín", "San Francisco", "Villa Dolores", "Capilla del Monte"],
        "Santa Fe": ["Santa Fe", "Rosario", "Rafaela", "Venado Tuerto", "Reconquista", "Villa Constitución", "Esperanza", "Cañada de Gómez", "Gálvez", "San Lorenzo"],
        "Mendoza": ["Mendoza", "San Rafael", "Godoy Cruz", "Luján de Cuyo", "Maipú", "Rivadavia", "Tunuyán", "Las Heras", "Malargüe", "San Martín"],
        "Tucumán": ["San Miguel de Tucumán", "Tafí Viejo", "Yerba Buena", "Concepción", "Banda del Río Salí", "Monteros", "Aguilares", "Famaillá", "Lules", "Juan Bautista Alberdi"],
        "Salta": ["Salta", "San Ramón de la Nueva Orán", "Tartagal", "General Güemes", "Embarcación", "Metán", "Rosario de la Frontera", "Cafayate", "Joaquín V. González", "Aguas Blancas"],
        "Misiones": ["Posadas", "Oberá", "Eldorado", "Puerto Iguazú", "Apóstoles", "Montecarlo", "Jardín América", "San Vicente", "Leandro N. Alem", "San Pedro"],
        "Chaco": ["Resistencia", "Presidencia Roque Sáenz Peña", "Villa Ángela", "Charata", "San Bernardo", "Las Breñas", "General José de San Martín", "Quitilipi", "Castelli", "Machagai"],
        "Entre Ríos": ["Paraná", "Concordia", "Gualeguaychú", "Gualeguay", "Concepción del Uruguay", "Villaguay", "Nogoyá", "La Paz", "Victoria", "Diamante"],
        "San Juan": ["San Juan", "Rawson", "Rivadavia", "Chimbas", "Santa Lucía", "Pocito", "Caucete", "9 de Julio", "Albardón", "Angaco"]
    };

    const provinciaSelect = document.getElementById('provincia');
    const localidadSelect = document.getElementById('localidad');

    // Poblar el select de provincias
    for (const provincia in provincias) {
        const option = document.createElement('option');
        option.value = provincia;
        option.textContent = provincia;
        provinciaSelect.appendChild(option);
    }

    // Cambiar las localidades cuando se selecciona una provincia
    provinciaSelect.addEventListener('change', function() {
        const selectedProvincia = this.value;
        const localidades = provincias[selectedProvincia] || [];
        
        // Limpiar el select de localidades
        localidadSelect.innerHTML = '<option value="">Seleccione</option>';

        // Poblar el select de localidades
        localidades.forEach(function(localidad) {
            const option = document.createElement('option');
            option.value = localidad;
            option.textContent = localidad;
            localidadSelect.appendChild(option);
        });
    });
});
