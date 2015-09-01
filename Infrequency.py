#!/usr/bin/env python
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

M_PI = 3.141592

#----------------------------------------------------
# Function to return the degrees from the Accelorometer
def convertAccelToAngle(x,y,z):
    roll = (math.atan2(-y,z)*180)/M_PI
    pitch = (math.atan2(x,math.sqrt(y*y + z*z))*180)/M_PI
    # yaw = (math.atan(math.sqrt(x)+math.sqrt(y)/z)*180)/M_PI
    print roll
    print pitch

#----------------------------------------------------
# Setup the stream
def setup():
    fileOpen = open("id.txt",'r+')
    clientID = fileOpen.read(32);
    fileOpen.close()

    print '------------------------'
    print 'Client ID'
    print clientID

    client = soundcloud.Client(client_id=clientID)
    streamURLClient = client
    print '------------------------'
    print 'Getting tracklist'
    try:
        tracks = client.get('/tracks', q='bbc')
    except Exception, e:
        print 'Error: %s, Status Code: %d' % (e.message, e.response.status_code)

    for track in tracks:
        newURL = streamURLClient.get(track.stream_url,allow_redirects=False)
        print '------------------------'
        print track.title
        print ""
        print newURL.location

# convertAccelToAngle(0.0,0.0,0.0)
setup()
