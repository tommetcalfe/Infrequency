var soundcloudTracks = [];
var playedArray = [];
var trackInfo = "160106800";
var songName = "";
//-----------------------------------------------------------------
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
      $("#state").html("Playing: "+songName);
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
    SC.get('/tracks', { q: searchTerm, limit: 20 }, function(tracks,err) {
        for (var i = 0; i < tracks.length; i++) {
            var links = $('<div><p id="track'+i+'" style="font-size:8px;">'+i+' <strong>ID</strong>:'+tracks[i].id+' <strong>Title</strong>:'+tracks[i].title+'</p></div>');
            // $('#tracks').appendTo(links).hide().slideDown('slow');
            links.appendTo($('#tracks')).hide().slideDown('slow');


        }
        soundcloudTracks = tracks;
    });
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
Array.prototype.contains = function(elem)
{
    for (var i in this) {
        if (this[i] == elem) return true;
    }
    return false;
}
//-----------------------------------------------------------------
function selectRandomTrack() {
    var num = getRandomInt(0,soundcloudTracks.length);
    console.log(num)
    console.log(playedArray)
    if(playedArray.contains(num)) {
        console.log("Number in array");
        // num = getRandomInt(0,soundcloudTracks.length);
        // if(playedArray.contains(num) == false) {
        //     playedArray.push(num);
        // }
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
        }
        else {
            $('#track'+i).css('color','black');
        }
    }


    console.log(trackInfo);
    SC.stream("/tracks/"+trackInfo,function(sound){
        stateMan = new StateMan(sound);
        volMan = new VolManager(sound);
    });
}
//-----------------------------------------------------------------
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
//-----------------------------------------------------------------
function updateStats(data) {
    console.log(data);
}
//-----------------------------------------------------------------
$(document).ready(function() {

    setupSoundCloud();
    getTracks("disclosure");

    var es = new EventSource("http://localhost:8080/some/path");
    es.onopen = function (event) {
        console.log("opened");
    };
    es.onmessage = function (event) {
        updateStats(event);
    };

    $('#submit').click(function(){
        console.log("Emptying Tracks");
        $('#tracks').empty();
        var str = $("#get").val();
        console.log("You've searched for: " + str);
        console.log("Getting New Tracks");
        getTracks(str);
    });
});
