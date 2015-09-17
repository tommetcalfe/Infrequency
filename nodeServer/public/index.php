<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="IoT radio">
    <meta name="author" content="David Haylock">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="/bootstrap/js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="/bootstrap/css/bootstrap.min.css">
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css" rel="stylesheet">
    <script src="http://connect.soundcloud.com/sdk-2.0.0.js"></script>
    <script src="main.js"></script>
    <title>Infrequency</title>

    <style>
    body {
      margin-bottom: 0px;
    }
    .footer {
      position: absolute;
      bottom: 0;
      width: 100%;
      height: 60px;
      /* background-color: #f5f5f5; */
    }
    .container {
        margin-top: 60px;
        width: auto;
        max-width: 680px;
        padding: 0 15px;
    }
    .container .text-muted {
        margin: 20px 0;
    }
    </style>
    <script>
        function sse() {
            var source = new EventSource('/stream');
            source.onmessage = function(e) {
                // var out = document.getElementById('out');
                // out.innerHTML =  '  <li>'+ e.data + '</li>' + out.innerHTML;
            };
        }
        sse();
    </script>

  </head>
  <body>
      <nav style="margin-bottom:0px" class="navbar navbar-fixed-top navbar-inverse" role="navigation">
        <div class="container-fluid">
        <div class="col-lg-4">
            <div class="navbar-header">
                <p style='color:white;' class="navbar-brand" href="#">Infrequency</p>
                <p style='color:white;' class="navbar-text" id="state">State: Stopped</p>
                <p style='color:white;' class="navbar-text" id="volume">Current Volume: 50</p>
            </div>
        </div>
        <div class="navbar-form navbar-right">
            <button id="play" onclick="stateMan.play()" style="border:none;" class="btn btn-primary" type="button">
                <span class="glyphicon glyphicon-play" style='color:white;' aria-hidden='true'></span>
            </button>
            <button id="stop" onclick="stateMan.stop()" style="border:none;" class="btn btn-primary" type="button">
                <span class="glyphicon glyphicon-stop" style='color:white;' aria-hidden='true'></span>
            </button>
            <button id="pause" onclick="stateMan.pause()" style="border:none;" class="btn btn-primary" type="button">
                <span class="glyphicon glyphicon-pause" style='color:white;' aria-hidden='true'></span>
            </button>
        </div>
      </div>
    </nav>
    <div class="container">
        <div align="left">
            <div id="tracks"></div>
        </div>
    </div>
    <footer class="footer">
        <div class="container">
            <p class="text-muted">Tom Metcalfe </br>Programming: David Haylock</p>
        </div>
   </footer>
  </body>
</html>
