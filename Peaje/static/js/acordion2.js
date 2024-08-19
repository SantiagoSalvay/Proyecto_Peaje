document.addEventListener('DOMContentLoaded', function() {
    const accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const accordionItem = this.parentElement;
            const accordionContent = accordionItem.querySelector('.accordion-content');
            
            // Cerrar cualquier acordeón que esté abierto
            const openAccordion = document.querySelector('.accordion-item.active');
            if (openAccordion && openAccordion !== accordionItem) {
                openAccordion.classList.remove('active');
                openAccordion.querySelector('.accordion-content').style.maxHeight = null;
                openAccordion.querySelector('.accordion-content').style.padding = "0 15px";
            }

            // Toggle el acordeón actual
            accordionItem.classList.toggle('active');

            if (accordionItem.classList.contains('active')) {
                accordionContent.style.maxHeight = accordionContent.scrollHeight + 'px';
                accordionContent.style.padding = "15px";
            } else {
                accordionContent.style.maxHeight = null;
                accordionContent.style.padding = "0 15px";
            }
        });
    });
});
