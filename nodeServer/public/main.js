var soundcloudTracks = [];

var fading = false;
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
            var links = $('<div><p style="font-size:8px;">'+i+' <strong>ID</strong>:'+tracks[i].id+' <strong>Title</strong>:'+tracks[i].title+'</p></div>');
            // $('#tracks').appendTo(links).hide().slideDown('slow');
            links.appendTo($('#tracks')).hide().slideDown('slow');


        }
        soundcloudTracks = tracks;
        // soundcloudTracks = copy(tracks);
        // }
        // soundcloudTracks = $.makeArray( tracks );
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
//-----------------------------------------------------------------
function selectRandomTrack() {
    soundcloudTracks
}
//-----------------------------------------------------------------
$(document).ready(function() {

    setupSoundCloud();
    getTracks("disclosure");
    console.log(soundcloudTracks);
    var trackInfo = "160106800";

    var source = new EventSource("/tilt");
    source.onmessage = function(event) {
        console.log(event.data);
    };

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
