#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

from flask import Flask, Response
import time

PORT_NUMBER = 8000

class ServerHandler(BaseHTTPRequestHandler):
	#Handler for the GET requests
	def do_GET(self):
		if self.path=="/":
			self.path="/public/"
		try:
			#Check the file extension required and
			#set the right mime type
			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith("min.css"):
				mimetype='text/css'
				sendReply = True
			if self.path.endswith("min.js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".php"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				f = open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	server = HTTPServer(('', PORT_NUMBER), ServerHandler)
	server.serve_forever()
	print 'Started Http Server on port ' , PORT_NUMBER

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
