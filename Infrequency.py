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

import soundcloud


M_PI = 3.141592

clientID = os.system("cat id.txt")
# create a client object with your app credentials
client = soundcloud.Client(client_id=clientID)
streamURLClient = client

print clientID

# Function to return the degrees from the Accelorometer
def convertAccelToAngle(x,y,z):
    roll = (math.atan2(-y,z)*180)/M_PI
    pitch = (math.atan2(x,math.sqrt(y*y + z*z))*180)/M_PI
    # yaw = (math.atan(math.sqrt(x)+math.sqrt(y)/z)*180)/M_PI
    print roll
    print pitch



# convertAccelToAngle(0.0,0.0,0.0)


tracks = client.get('/tracks', q='bbc')

for track in tracks:
    newURL = streamURLClient.get(track.stream_url,allow_redirects=False)
    print newURL.location
