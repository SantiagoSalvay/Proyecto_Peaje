document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('.carousel');
    const indicators = document.querySelectorAll('.indicator');
    const progressBar = document.querySelector('.progress-bar');
    let currentIndex = 0;
    const slideDuration = 5000;

    function slide(index) {
        currentIndex = index;
        carousel.style.transform = `translateX(-${currentIndex * 50}%)`;
        updateIndicators();
        resetProgressBar();
    }

    function updateIndicators() {
        indicators.forEach((indicator, index) => {
            indicator.classList.toggle('active', index === currentIndex);
        });
    }

    function resetProgressBar() {
        progressBar.style.transition = 'none';
        progressBar.style.width = '0%';
        setTimeout(() => {
            progressBar.style.transition = `width ${slideDuration}ms linear`;
            progressBar.style.width = '100%';
        }, 50);
    }

    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => slide(index));
    });

    setInterval(() => slide((currentIndex + 1) % 2), slideDuration);
    resetProgressBar();
});