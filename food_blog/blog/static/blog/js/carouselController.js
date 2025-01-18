const track = document.querySelector('.carousel-track');
const slides = Array.from(track.children);
const nextButton = document.querySelector('.carousel-button-right');
const prevButton = document.querySelector('.carousel-button-left');

let currentSlide = 0

const updateSlidePosition = () => {
    track.style.transform = `translateX(-${currentSlide * 100}%)`;
}

nextButton.addEventListener('click', () => {
    if(currentSlide < slides.length -1) {
        currentSlide++;
        updateSlidePosition()
    }
});

prevButton.addEventListener('click', () => {
    if(currentSlide > 0) {
        currentSlide--;
        updateSlidePosition();
    }
});