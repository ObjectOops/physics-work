const video = document.getElementById("physics-work");

const pauseTimes = [10, 20, 30];

function checkAutoPause() {
    if (pauseTimes.includes(Math.floor(video.currentTime))) {
        video.pause();
    }
}

video.addEventListener("timeupdate", checkAutoPause);
