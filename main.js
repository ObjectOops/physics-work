alert('started')

const video = document.getElementById('physics-work');

const pauseTimes = [10, 20, 30];

function pauseVideoAtTimes() {
    alert('hi')
    currentTime = Math.floor(video.currentTime);
    if (pauseTimes.includes(currentTime)) {
        video.pause();
    }
}

function jumpToTime(time) {
    video.currentTime = time;
}

video.addEventListener('timeupdate', pauseVideoAtTimes);
