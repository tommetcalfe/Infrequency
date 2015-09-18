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
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css" rel="stylesheet">
    <script src="http://connect.soundcloud.com/sdk-2.0.0.js"></script>
    <script src="main.js"></script>
    <title>Infrequency</title>
    </head>
    <body>
        <div class="site-wrapper">
            <div class="site-wrapper-inner">
                <div class="cover-container">
                    <div class="masthead clearfix"></div>
                </div>

                <div class="inner cover">
                    <h1 class="cover-heading">Infrequency</h1>
                    <div align="center">
                        <div style="max-width:300px;" class="input-group">
                            <input id="get" type="text" class="form-control" placeholder="Search Term">
                            <span class="input-group-btn">
                                <button id="submit" type="submit" class="btn btn-primary">Search</button>
                            </span>
                        </div>
                    </div>
                </div>
                <div align="center">
                    <h5 style='color:black;'  id="state">Stopped</h5>
                    <button id="play" onclick="stateMan.play();" style="border:none;" class="btn btn-primary" type="button">
                        <span class="glyphicon glyphicon-play" style='color:white;' aria-hidden='true'></span>
                    </button>
                    <button id="stop" onclick="stateMan.stop() " style="border:none;" class="btn btn-primary" type="button">
                        <span class="glyphicon glyphicon-stop" style='color:white;' aria-hidden='true'></span>
                    </button>
                    <button id="pause" onclick="stateMan.pause()" style="border:none;" class="btn btn-primary" type="button">
                        <span class="glyphicon glyphicon-pause" style='color:white;' aria-hidden='true'></span>
                    </button>
                    <button id="select" onclick="selectRandomTrack()" style="border:none;" class="btn btn-primary" type="button">
                        <span class="glyphicon glyphicon-filter" style='color:white;' aria-hidden='true'></span>
                    </button>
                    <!-- <h5 style='color:black;'  id="volume">Current Volume: 50</h5> -->
                </div>
                <div class="container">
                    <div align="center">
                        <div id="tracks"></div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
