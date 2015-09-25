#!/usr/bin/python
import string
import random
from random import shuffle
import sys
import datetime
import math
import httplib,urllib
import json
import os
import sys
import subprocess
import soundcloud
import datetime
import webbrowser
import sys
import time
import termios

# HOST_NAME = "127.0.0.1"
# PORT_NUMBER = 8888

#create ADXL345 object


# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# class MyTCPServer(SocketServer.TCPServer):
#     allow_reuse_address = True
#     def do_HEAD(s):
#         s.send_response(200)
#         s.send_header("Content-type", "text/html")
#         s.end_headers()
#
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers()
#         self.wfile.write("<html><head><title>Title goes here.</title></head>")
#         self.wfile.write("<body><p>This is a test.</p>")
#         self.wfile.write("<p>You accessed path: %s</p>" % self.path)
#         self.wfile.write("</body></html>")
#         return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
# global xangle

#TERMIOS = termios
#M_PI = 3.141592
#
##----------------------------------------------------
#trackNames = []
#trackStreamingURLs = []
#trackID = []
#trackCreatedAt = []
#trackJSON = []
#
##----------------------------------------------------
## Function to get keys
#def getkey():
#    fd = sys.stdin.fileno()
#    old = termios.tcgetattr(fd)
#    new = termios.tcgetattr(fd)
#    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
#    new[6][TERMIOS.VMIN] = 1
#    new[6][TERMIOS.VTIME] = 0
#    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
#    c = None
#    try:
#            c = os.read(fd, 1)
#    finally:
#            termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
#    return c

#----------------------------------------------------
# Accelorometer Stuff
#----------------------------------------------------
#def setupAccel():
#    accel.setRange(adxl345.RANGE_2G)
#    accel.setRange(adxl345.RANGE_4G)
#    accel.setRange(adxl345.RANGE_8G)
#    accel.setRange(adxl345.RANGE_16G)
#----------------------------------------------------
# Function to return the degrees from the Accelorometer
#def convertAccelToAngle(x,y,z):
#    roll = (math.atan2(-y,z)*180)/M_PI
#    pitch = (math.atan2(x,math.sqrt(y*y + z*z))*180)/M_PI
#    yaw = (math.atan(math.sqrt(x)+math.sqrt(y)/z)*180)/M_PI
#    return roll,pitch,yaw
    # print roll
    # print pitch
#----------------------------------------------------
# Update and check conditions
#def updateAccel():
#    axes = accel.getAxes(True)
#    convertAccelToAngle(axes['x'],axes['y'],axes['z'])

#----------------------------------------------------
## Setup the stream
#def setup():
#    fileOpen = open("id.txt",'r+')
#    clientID = fileOpen.read(32);
#    fileOpen.close()
#
#    print '------------------------'
#    print 'Client ID'
#    print clientID
#    return clientID
##----------------------------------------------------
## Get Tracks
#def getTracks(id,query):
#    client = soundcloud.Client(client_id=id)
#    streamURLClient = client
#    print '------------------------'
#    print 'Getting tracklist'
##    try:
#    tracks = client.get('/tracks', q=query)
##    except Exception, e:
##        print 'Error: %s, Status Code: %d' % (e.message, e.response.status_code)
#
#    for track in tracks:
#        newURL = streamURLClient.get(track.stream_url,allow_redirects=False)
#        print '------------------------'
#        print track.title
#        print ""
#        print newURL.location
#        print ""
#        print datetime.datetime.now()
##        trackJSON.append({"id":1,"title":track.title,"streamurl":newURL.location,"created_at":datetime.datetime.now()})
#
## convertAccelToAngle(0.0,0.0,0.0)
#
#cID = setup()
##----------------------------------------------------
#def main_loop():
##    xangle = 0.000
#    while 1:
##        if xangle > 0.000:
##            xangle -= 0.01
##        elif xangle < 0.000:
##            xangle += 0.01
#
#        c = getkey()
#
##            print convertAccelToAngle(0.4,0.1,0.1)
#        if c == 'g':
#            getTracks(id="fe503f838868c2301b391f1877716edd",query="disclosure")
#        if c == 'p':
#            print 'got', c
#
##        print xangle
#        time.sleep(0.1)
#
##----------------------------------------------------
#if __name__ == '__main__':
#    try:
#        main_loop()
#    except KeyboardInterrupt:
#        print >> sys.stderr, '\nExiting by user request.\n'
#        sys.exit(0)
