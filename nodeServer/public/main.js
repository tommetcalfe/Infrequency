var soundcloudTracks =[];
function setupSoundCloud() {
    SC.initialize({
        client_id: 'xxx'
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
      $("#state").html("State: Playing");
    };

    // Stop playback if not already stopped
    this.stop = function () {
      if (state == "stop" ) return;
      state = "stop";
      track.stop();
      $("#state").html("State: Stopped");
    };

    // Pause playback if not already Paused
    this.pause = function  () {
      if (state == "pause" ) return;
      state = "pause";
      track.pause();
      $("#state").html("State: Paused");
    };
    // Initial state update
    this.stop();
}
//-----------------------------------------------------------------
function getTracks() {
    SC.get('/tracks', { q: 'bbc', limit: 20 }, function(tracks,err) {
        for (var i = 0; i < tracks.length; i++) {
            var links = $('<div><p>'+i+' <strong>ID</strong>:'+tracks[i].id+' <strong>Title</strong>:'+tracks[i].title+'</p></div>');
            links.appendTo($('#tracks'));
        }
        soundcloudTracks = $.makeArray( tracks );
    });
}

//-----------------------------------------------------------------
$(document).ready(function() {

    setupSoundCloud();
    getTracks();

    var trackInfo = "/tracks/";
    console.log(soundcloudTracks);
    // SC.stream(trackInfo,function(sound){
    //     console.log(sound);
    //     stateMan = new StateMan(sound);
    //     volMan = new VolManager(sound);
    // });
});
