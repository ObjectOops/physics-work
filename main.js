var video = document.getElementById("physics-work");

const pauseTimes = [2, 8, 17, 21, 27, 31, 35, 37, 43, 46, 49, 50, 51, 57, 63, 69, 72, 78, 83, 86, 92, 102, 108, 114];

function checkAutoPause() {
    var currentSecond = Math.floor(video.currentTime);
    if (pauseTimes.includes(currentSecond)) {
        video.pause();
        video.currentTime = currentSecond + 1;
    }
}

video.addEventListener("timeupdate", checkAutoPause);

video.addEventListener("mouseenter", function() {
    video.controls = true;
});
video.addEventListener("mouseleave", function() {
    video.controls = false;
});

document.addEventListener('keydown', function(event) {
    if (event.keyCode === 32) {
        event.preventDefault();
        if (video.paused) {
            video.play();
        } else {
            video.pause();
        }
    }
});
