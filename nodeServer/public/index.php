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
    /*
 * Globals
 */

/* Links */
a,
a:focus,
a:hover {
  color: #fff;
}

/* Custom default button */
.btn-default,
.btn-default:hover,
.btn-default:focus {
  color: #333;
  text-shadow: none; /* Prevent inheritence from `body` */
  background-color: #fff;
  border: 1px solid #fff;
}


/*
 * Base structure
 */

html,
body {
  height: 100%;
  background-color: #333;
}
body {
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 3px rgba(0,0,0,.5);
}

/* Extra markup and styles for table-esque vertical and horizontal centering */
.site-wrapper {
  display: table;
  width: 100%;
  height: 100%; /* For at least Firefox */
  min-height: 100%;
  -webkit-box-shadow: inset 0 0 100px rgba(0,0,0,.9);
          box-shadow: inset 0 0 100px rgba(0,0,0,.9);
}
.site-wrapper-inner {
  display: table-cell;
  vertical-align: top;
}
.cover-container {
  margin-right: auto;
  margin-left: auto;
}

/* Padding for spacing */
.inner {
  padding: 30px;
}


/*
 * Header
 */
.masthead-brand {
  margin-top: 10px;
  margin-bottom: 10px;
}

.masthead-nav > li {
  display: inline-block;
}
.masthead-nav > li + li {
  margin-left: 20px;
}
.masthead-nav > li > a {
  padding-right: 0;
  padding-left: 0;
  font-size: 16px;
  font-weight: bold;
  color: #fff; /* IE8 proofing */
  color: rgba(255,255,255,.75);
  border-bottom: 2px solid transparent;
}
.masthead-nav > li > a:hover,
.masthead-nav > li > a:focus {
  background-color: transparent;
  border-bottom-color: #a9a9a9;
  border-bottom-color: rgba(255,255,255,.25);
}
.masthead-nav > .active > a,
.masthead-nav > .active > a:hover,
.masthead-nav > .active > a:focus {
  color: #fff;
  border-bottom-color: #fff;
}

@media (min-width: 768px) {
  .masthead-brand {
    float: left;
  }
  .masthead-nav {
    float: right;
  }
}


/*
 * Cover
 */

.cover {
  padding: 0 20px;
}
.cover .btn-lg {
  padding: 10px 20px;
  font-weight: bold;
}


/*
 * Footer
 */

.mastfoot {
  color: #999; /* IE8 proofing */
  color: rgba(255,255,255,.5);
}


/*
 * Affix and center
 */

@media (min-width: 768px) {
  /* Pull out the header and footer */
  .masthead {
    position: fixed;
    top: 0;
  }
  .mastfoot {
    position: fixed;
    bottom: 0;
  }
  /* Start the vertical centering */
  .site-wrapper-inner {
    vertical-align: middle;
  }
  /* Handle the widths */
  .masthead,
  .mastfoot,
  .cover-container {
    width: 100%; /* Must be percentage or pixels for horizontal alignment */
  }
}

@media (min-width: 992px) {
  .masthead,
  .mastfoot,
  .cover-container {
    width: 700px;
  }
}
    </style>
    <script>
        // function sse() {
        //     var source = new EventSource("/change");
        //     source.onmessage = function(e) {
        //         console.log(e);
        //     };
        // }
        // sse();
    </script>

  </head>
  <body>
      <div class="site-wrapper">

      <div class="site-wrapper-inner">

        <div class="cover-container">
            <div class="masthead clearfix">
            </div>
        </div>

        <div class="inner cover">
            <h1 class="cover-heading">Infrequency</h1>
            <div align="center">
                <div style="max-width:300px;" class="input-group">
                        <input id="get" type="text" class="form-control" placeholder="Search Term">
                        <span class="input-group-btn">
                            <button id="submit" onclick="changeTitle()" type="submit" class="btn btn-primary">Search</button>
                        </span>
                    </div>
                </div>
        </div>
        <div align="center">
            <h5 style='color:white;'  id="state">Stopped</h5>
            <h5 style='color:white;'  id="volume">Current Volume: 50</h5>
        </div>
          <div class="mastfoot">
            <div class="inner">
                <button id="play" onclick="stateMan.play();" style="border:none;" class="btn btn-primary" type="button">
                    <span class="glyphicon glyphicon-play" style='color:white;' aria-hidden='true'></span>
                </button>
                <button id="stop" onclick="stateMan.stop() " style="border:none;" class="btn btn-primary" type="button">
                    <span class="glyphicon glyphicon-stop" style='color:white;' aria-hidden='true'></span>
                </button>
                <button id="pause" onclick="stateMan.pause()" style="border:none;" class="btn btn-primary" type="button">
                    <span class="glyphicon glyphicon-pause" style='color:white;' aria-hidden='true'></span>
                </button>
            </div>
          </div>

        </div>

      </div>

  </div>
    <!-- <div class="container">
        <div align="left">
            <div id="tracks"></div>
        </div>
    </div> -->
    <!-- <footer class="footer">
        <div class="container">
            <p class="text-muted">Tom Metcalfe </br>Programming: David Haylock</p>
        </div>
       </footer> -->
  </body>
</html>
