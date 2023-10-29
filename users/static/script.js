console.log("Welcome to Music Beats");

// Initialize the Variables
var player = document.getElementById('player');
var masterPlay = document.getElementById('play-btn');
var progressbar = document.getElementById('seekObj');
var beat_id = 0;
var likeSpan = document.getElementById("like");
var dropdownPlaylist = document.getElementsByClassName("dropdown-playlist")


function calculateTotalValue(length) {
    var minutes = Math.floor(length / 60),
        seconds_int = length - minutes * 60,
        seconds_str = seconds_int.toString(),
        seconds = seconds_str.substr(0, 2),
        time = minutes + ':' + seconds

    return time;
}

function calculateCurrentValue(currentTime) {
    var current_hour = parseInt(currentTime / 3600) % 24,
        current_minute = parseInt(currentTime / 60) % 60,
        current_seconds_long = currentTime % 60,
        current_seconds = current_seconds_long.toFixed(),
        current_time = (current_minute < 10 ? "0" + current_minute : current_minute) + ":" + (current_seconds < 10 ? "0" + current_seconds : current_seconds);

    return current_time;
}

function initProgressBar() {
    var length = player.duration
    if (isNaN(length)) {
        return;
    }

    var current_time = player.currentTime;

    // calculate total length of value
    var totalLength = calculateTotalValue(length)
    jQuery(".end-time").html(totalLength);

    // calculate current value time
    var currentTime = calculateCurrentValue(current_time);
    jQuery(".start-time").html(currentTime);

    progressbar.value = (player.currentTime / player.duration);

    if (player.currentTime == player.duration) {
        $('#play-btn').removeClass('pause');
    }
};

progressbar.addEventListener("click", seek);

function seek(evt) {
    var percent = evt.offsetX / this.offsetWidth;
    player.currentTime = percent * player.duration;
    progressbar.value = percent / 100;
}

// Handle play/pause click
masterPlay.addEventListener('click', () => {
    if (player.paused || player.currentTime <= 0) {
        player.play();
        masterPlay.classList.add('pause')
    }
    else {
        player.pause();
        masterPlay.classList.remove('pause')
    }
})

const makeGetRequest = (endpoint) => {
    console.log(endpoint)
    fetch(endpoint, {
        method: 'GET',
    }).then(response => {
        if (response.ok) {
            response.text().then(data => console.log(data))
        } else {
            console.log("Error occurred")
        }
    }).catch(error => console.error('Fetch error: ' + error))
};

if (likeSpan) {
    likeSpan.addEventListener("click", () => {
        if (likeSpan.classList.contains("heart-color")) {
            console.log("Already liked")
            makeGetRequest("/beats/dislike/" + beat_id)
            likeSpan.classList.remove("heart-color")
        } else {
            makeGetRequest("/beats/like/" + beat_id)
            likeSpan.classList.add("heart-color")
        }
    })
}

Array.from(document.getElementsByClassName('play')).forEach((element) => {
    element.addEventListener('click', () => {
        var audioPath = element.getAttribute('data-audio-path');
        var masterSongName = document.getElementById('beat-title')
        beat_id = element.getAttribute('data-beat-id')
        console.log(beat_id)
        player.src = audioPath;
        masterSongName.innerText = element.getAttribute('data-beat-title') + " by " + element.getAttribute('data-beat-singer')

        var newImageUrl = element.getAttribute('data-image-url')
        var albumImage = document.querySelector('.album-image');
        albumImage.style.backgroundImage = 'url(' + newImageUrl + ')';

        // Initialize like button
        var check_liked_beat_endpoint = "/beats/check-liked-beat/" + beat_id
        fetch(check_liked_beat_endpoint, {
            method: 'GET',
        }).then((response) => {
            if (response.ok) {
                likeSpan.classList.add("heart-color")
            } else {
                console.log("not liked")
            }
        }).catch((error) => {
            console.log("Error occurred: " + error)
        })

        player.currentTime = 0;
        player.play();
        masterPlay.classList.add('pause')
    })
})

Array.from(dropdownPlaylist).forEach(element => {
    element.addEventListener("click", () => {
        console.log("inside")
        var beat_id = element.getAttribute('data-beat-id')
        var playlist_id = element.getAttribute('data-playlist-id')
        var add_beat_endpoint = "playlist/" + playlist_id + "/add/" + beat_id

        fetch(add_beat_endpoint, {
            method: 'GET'
        }).then(response => {
            if (response.ok) {
                console.log("added to playlist")
            } else {
                console.log("Error occurred")
            }
        }).catch(error => {
            console.log("error occured: " + error)
        })
    })
})