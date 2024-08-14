document.addEventListener('DOMContentLoaded', function() {
    var accordionButtons = document.querySelectorAll('.accordion-button');

    accordionButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var accordionContent = this.nextElementSibling;
            var accordionIcon = this.querySelector('.accordion-icon');
            var accordionArrow = this.querySelector('.accordion-arrow');
            
            // Cerrar todos los demás paneles
            document.querySelectorAll('.accordion-content').forEach(function(content) {
                if (content !== accordionContent) {
                    content.style.maxHeight = null;
                    content.previousElementSibling.classList.remove('active');
                    content.previousElementSibling.querySelector('.accordion-icon').textContent = '+';
                    content.previousElementSibling.querySelector('.accordion-arrow').style.transform = 'rotate(0deg)';
                }
            });
            
            // Alternar la apertura/cierre del panel
            if (accordionContent.style.maxHeight) {
                accordionContent.style.maxHeight = null;
                accordionIcon.textContent = '+';
                accordionArrow.style.transform = 'rotate(0deg)';
                this.classList.remove('active');
            } else {
                accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
                accordionIcon.textContent = '-';
                accordionArrow.style.transform = 'rotate(90deg)';
                this.classList.add('active');
            }
        });
    });
});
