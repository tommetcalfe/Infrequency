var soundcloudTracks = [];
var websocket;
var fading = false;
var playedArray = [];

function setupSoundCloud() {
    SC.initialize({
        client_id: '004f94bea5f40f3f5efcbd72928c6cfa'
    });
}
//-----------------------------------------------------------------
function VolManager(currentTrack) {
    var track = currentTrack;
    var vol = 50;
    this.updateVolume  = function () {
        $("#volume").html("Current Volume: " + vol);
        track.setVolume(vol);
    };

    // Increases volume level
    this.volUp = function () {
      if (vol >= 100) return;
      vol += 10;
      this.updateVolume();
    };
    // Decrease volume level
    this.volDown = function () {
      if (vol <= 0) return;
      vol -= 10;
      this.updateVolume();
    };
    // Mutes volume
    this.mute = function () {
      track.mute();
      $("#mState").html("MUTE");
    };
    // Unmutes volume
    this.unmute = function () {
      track.unmute();
      $("#mState").html("");
    };
    // Initial volume update
    this.updateVolume();
  }
//-----------------------------------------------------------------
  // Manages play state
function StateMan(currentTrack) {
    var track = currentTrack;
    var state = "";

    this.play = function () {
      if (state == "play" ) return;
      state = "play";
      track.play();
      $("#state").html("Playing");
    };

    // Stop playback if not already stopped
    this.stop = function () {
      if (state == "stop" ) return;
      state = "stop";
      track.stop();
      $("#state").html("Stopped");
    };

    // Pause playback if not already Paused
    this.pause = function  () {
      if (state == "pause" ) return;
      state = "pause";
      track.pause();
      $("#state").html("Paused");
    };
    // Initial state update
    this.stop();
}
//-----------------------------------------------------------------
function getTracks(searchTerm) {
    // soundcloudTracks = [];
    SC.get('/tracks', { q: searchTerm, limit: 20 }, function(tracks,err) {
        for (var i = 0; i < tracks.length; i++) {
            var links = $('<div><p id="track'+i+'"style="font-size:8px;">'+i+' <strong>ID</strong>:'+tracks[i].id+' <strong>Title</strong>:'+tracks[i].title+'</p></div>');
            links.appendTo($('#tracks')).hide().slideDown('slow');
        }
        soundcloudTracks = tracks;
    });
}
//-----------------------------------------------------------------
Array.prototype.contains = function(elem)
{
    for (var i in this) {
        if (this[i] == elem) return true;
    }
    return false;
}
//-----------------------------------------------------------------
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
//-----------------------------------------------------------------
function copy(o) {
   var out, v, key;
   out = Array.isArray(o) ? [] : {};
   for (key in o) {
       v = o[key];
       out[key] = (typeof v === "object") ? copy(v) : v;
   }
   return out;
}
//-----------------------------------------------------------------
function selectRandomTrack() {
    var num = getRandomInt(0,soundcloudTracks.length);
        console.log(num)
        console.log(playedArray)
        if(playedArray.contains(num)) {
            console.log("Number in array");
        }
        else {
            playedArray.push(num);
        }
        console.log(playedArray)

        trackInfo = soundcloudTracks[num].id;
        songName = soundcloudTracks[num].title;
        for(var i = 0; i < soundcloudTracks.length; i++) {
            if(i == num) {
                $('#track'+i).css('color','red');
                $('#track'+i).css('text-decoration', 'line-through');
            }
            else {
                $('#track'+i).css('color','black');
            }
    }
}
//-----------------------------------------------------------------
$(document).ready(function() {
    // document.myform.url.value = "ws://localhost:8080/"<!-- -->
    var websocket = new WebSocket("ws://localhost:8001/ws");
    websocket.onopen = function(evt) {
        console.log("Opened Socket")
        console.log(evt);
        websocket.send("Connected")
    };
    websocket.onclose = function(evt) { console.log("Closed Socket")};
    websocket.onmessage = function(evt) { console.log("Message from Socket")};
    websocket.onerror = function(evt) { console.log("Error on Socket")};

    setupSoundCloud();
    getTracks("disclosure");
    console.log(soundcloudTracks);
    var trackInfo = "160106800";

    SC.stream("/tracks/"+trackInfo,function(sound){
        console.log(sound);
        stateMan = new StateMan(sound);
        volMan = new VolManager(sound);
    });

    $('#submit').click(function(){
        $('#tracks').empty();
        var str = $("#get").val();
        getTracks(str);
        console.log(soundcloudTracks);
    });
});
