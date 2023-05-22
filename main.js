var video = document.getElementById("physics-work");

alert(video)

const pauseTimes = [10, 20, 30];

function checkAutoPause() {
    document.getElementById("t").innerHTML = video.currentTime;
    if (pauseTimes.includes(Math.floor(video.currentTime))) {
        video.pause();
    }
}

video.addEventListener("loadedmetadata", function() {
    video.addEventListener("timeupdate", checkAutoPause);
});
