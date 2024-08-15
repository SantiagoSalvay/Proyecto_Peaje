function setProgress(percent, element) {
    const circle = element.querySelector('.progress-ring__circle');
    const radius = circle.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;
  
    circle.style.strokeDasharray = `${circumference} ${circumference}`;
    circle.style.strokeDashoffset = `${circumference}`;
  
    const offset = circumference - (percent / 100) * circumference;
    
    // Velocidad de la animación en ms (más bajo = más rápido)
    const animationSpeed = 7;
  
    // Animación del círculo
    let currentOffset = circumference;
    const interval = setInterval(() => {
        if (currentOffset <= offset) {
            clearInterval(interval);
        } else {
            currentOffset -= (circumference / 100);
            circle.style.strokeDashoffset = currentOffset;
        }
    }, animationSpeed);
  
    // Animación del porcentaje
    const percentageText = element.querySelector('.percentage');
    let currentPercent = 0;
    const percentageInterval = setInterval(() => {
      if (currentPercent >= percent) {
        clearInterval(percentageInterval);
      } else {
        currentPercent++;
        percentageText.textContent = `${currentPercent}%`;
      }
    }, 700 / percent); // Este valor controla la velocidad del texto
}
  
// Aplicar la animación al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    const progressCircles = document.querySelectorAll('.progress-circle');
    progressCircles.forEach(circle => {
        setProgress(100, circle); // Cambia 100 por el porcentaje que desees animar
    });
});
