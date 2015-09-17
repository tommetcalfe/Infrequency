var sys = require("sys");
var http = require("http");
var fs = require("fs");

function sendServerSendEvent(req, res) {
 res.writeHead(200, {
 'Content-Type' : 'text/event-stream',
 'Cache-Control' : 'no-cache',
 'Connection' : 'keep-alive'
 });

 var sseId = (new Date()).toLocaleTimeString();
     console.log("hi"+ sseId)
     writeServerSendEvent(res,sseId,"hi");
}

function writeServerSendEvent(res, sseId, data) {
 res.write('id: ' + sseId + '\n');
 res.write("data: new server event " + data + '\n\n');
 res.end()
}

//-------------------------------------------------------------------------
http.createServer(function(request,response){
    if (request.url.indexOf('.js') != -1) {
        fs.readFile("./public"+ request.url, function(err,data){
            if(err) {
                response.writeHead(404);
                response.end(JSON.stringify(err));
                return;
            }
            response.writeHead(200, {'Content-Type': 'text/javascript'});
            // response.write(data)
            response.end(data);
        });
    }
    if (request.url.indexOf('.html') != -1) {
        fs.readFile("./public"+ request.url, function(err,data){
            if(err) {
                response.writeHead(404);
                response.end(JSON.stringify(err));
                return;
            }
            response.writeHead(200, {'Content-Type': 'text/html'});
            // response.write(data)
            response.end(data);
        });
    }
    if (request.url.indexOf('.php') != -1) {
        fs.readFile("./public"+ request.url, function(err,data){
            if(err) {
                response.writeHead(404);
                response.end(JSON.stringify(err));
                return;
            }
            response.writeHead(200, {'Content-Type': 'text/html'});
            // response.write(data)
            response.end(data);
        });
    }
    if (request.url.indexOf('.css') != -1) {
        fs.readFile("./public"+ request.url, function(err,data){
            if(err) {
                response.writeHead(404);
                response.end(JSON.stringify(err));
                return;
            }
            response.writeHead(200, {'Content-Type': 'text/css'});
            // response.write(data)
            response.end(data);
        });
    }
    // if (req.headers.accept && req.headers.accept == 'text/event-stream') {
    //     if (request.url == "/change") {
    //         sendServerSendEvent(request,response);
    //     }
    // }


        // response.writeHead(200, {'Content-Type': 'text/html'});
        // response.write()
        // response.end(data);

}).listen(8080);
console.log("Infrequency Launched at 127.0.0.1:8080");
