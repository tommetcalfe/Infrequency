#!/usr/bin/env python 
import string
#import random
#from random import shuffle
import sys
import datetime
import math
import httplib,urllib
import json
import os
import sys

import urllib2
contents = urllib2.urlopen("https://itunes.apple.com/search?term=gardening&entity=podcast").read()

print contents

#
#import soundcloud
#
#
#M_PI = 3.141592
#
#clientID = os.system("cat id.txt")
## create a client object with your app credentials
#client = soundcloud.Client(client_id="fe503f838868c2301b391f1877716edd")
##streamURLClient = client
#
#print clientID
#
## Function to return the degrees from the Accelorometer
#def convertAccelToAngle(x,y,z):
#    roll = (math.atan2(-y,z)*180)/M_PI
#    pitch = (math.atan2(x,math.sqrt(y*y + z*z))*180)/M_PI
#    # yaw = (math.atan(math.sqrt(x)+math.sqrt(y)/z)*180)/M_PI
#    print roll
#    print pitch
#
#
#
## convertAccelToAngle(0.0,0.0,0.0)



#
#import soundcloud
#
## create a client object with your app credentials
#client = soundcloud.Client(client_id='fe503f838868c2301b391f1877716edd')
#
## find all sounds of buskers licensed under 'creative commons share alike'
#tracks = client.get('/tracks',query='gardening')
#
#for track in tracks:
#    newURL = client.get(track.stream_url,allow_redirects=False)
#    print "------------------------"
#    print track.title
#    print newURL.location
#
#print "------------------------"