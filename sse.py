#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import gevent
# from gevent.wsgi import WSGIServer
# from gevent.queue import Queue
from flask import Flask, Response
# from bottle import get, post, request, response,run,GeventServer
# from gevent import monkey; monkey.patch_all()
import time

PORT_NUMBER = 8000

# @get('/send')
# def send():
# 	response.content_type  = 'text/event-stream'
# 	response.cache_control = 'no-cache'
#
# 	# Set client-side auto-reconnect timeout, ms.
# 	yield 'retry: 100\n\n'
#
# 	n = 1
#
# 	# Keep connection alive no more then... (s)
# 	end = time.time() + 60
# 	while time.time() < end:
# 		yield 'data: %i\n\n' % n
# 		n += 1
# 		sleep(1)

class myHandler(BaseHTTPRequestHandler):

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
				#Open the static file requested and send it
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



	server = HTTPServer(('', PORT_NUMBER), myHandler)
	server.serve_forever()
	print 'Started Http Server on port ' , PORT_NUMBER
	# run(server=server)
	#Wait forever for incoming htto requests


except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
