document.addEventListener("DOMContentLoaded", function() {
    const documentoSelect = document.getElementById('documento');
    const extraInputContainer = document.getElementById('extraInputContainer');
    const extraLabel = document.getElementById('extraLabel');
    const extraInput = document.getElementById('extraInput');
    const loginForm = document.getElementById('loginForm');

    documentoSelect.addEventListener('change', function() {
        const selectedValue = documentoSelect.value;

        if (selectedValue === 'DNI') {
            extraLabel.textContent = 'Ingrese su DNI';
            extraInput.placeholder = 'Número de DNI';
            extraInputContainer.style.display = 'block';
        } else if (selectedValue === 'PASAPORTE') {
            extraLabel.textContent = 'Ingrese su Pasaporte';
            extraInput.placeholder = 'Número de Pasaporte';
            extraInputContainer.style.display = 'block';
        } else {
            extraInputContainer.style.display = 'none';
        }
    });

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); 

        if (!documentoSelect.value || !extraInput.value || !document.getElementById('nombre').value || !document.getElementById('apellido').value) {
            alert('Por favor, complete todos los campos antes de iniciar sesión.');
        } else {
            
            window.location.href = '/casilla/'; 
        }
    });
});
