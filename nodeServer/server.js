var sys = require("util");
var http = require("http");
var fs = require("fs");
var ssePusher = require('sse-pusher');
var connect = require('connect');
var app = connect();

var push = ssePusher(); // instantiation variant 1
var push = ssePusher.create();

app.use(push.handler('/some/path'));
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
            response.end(data);
        });
    }
}).listen(8080);
push('eventname', 'eventdata');

console.log("Infrequency Launched at 127.0.0.1:8080");
