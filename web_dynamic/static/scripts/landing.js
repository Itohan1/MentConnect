const video = document.getElementById('myVideo');
const playOverlay = document.getElementById('playOverlay');

playOverlay.addEventListener('click', () => {
    video.play();
    playOverlay.style.display = 'none';
});

video.addEventListener('pause', () => {
    playOverlay.style.display = 'flex';
});

video.addEventListener('play', () => {
    playOverlay.style.display = 'none';
});