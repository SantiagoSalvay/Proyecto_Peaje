window.addEventListener('resize', () => {
    const carouselImages = document.querySelectorAll('.carousel-image');
    const containerWidth = document.querySelector('.carousel-container').clientWidth;

    carouselImages.forEach(image => {
        image.style.height = `${containerWidth * 0.5}px`; // Adjust height based on container width
    });
});

// Initial setup
window.dispatchEvent(new Event('resize'));
