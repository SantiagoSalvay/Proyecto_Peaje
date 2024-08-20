function setProgress(percent, element) {
    const circle = element.querySelector('.progress-ring__circle');
    const radius = circle.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;

   
    circle.style.strokeDasharray = `${circumference} ${circumference}`;
    circle.style.strokeDashoffset = `${circumference}`;

    const offset = circumference - (percent / 100) * circumference;


    const animationSpeed = 30; 


    let currentOffset = circumference;
    const interval = setInterval(() => {
        if (currentOffset <= offset) {
            clearInterval(interval);
        } else {
            currentOffset -= (circumference / 100);
            circle.style.strokeDashoffset = currentOffset;
        }
    }, animationSpeed);


    const percentageText = element.querySelector('.percentage');
    let currentPercent = 0;
    const percentageInterval = setInterval(() => {
        if (currentPercent >= percent) {
            clearInterval(percentageInterval);
        } else {
            currentPercent++;
            percentageText.textContent = `${currentPercent}%`;
        }
    }, 3100 / percent); 
}


document.addEventListener('DOMContentLoaded', () => {
    const progressCircles = document.querySelectorAll('.progress-circle');
    progressCircles.forEach(circle => {
        setProgress(100, circle); 
    });
});