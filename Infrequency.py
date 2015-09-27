#!/usr/bin/env python

#-------------------------------------------------------
# * Project: Infrequency
# * File: Infrequency.py
# * Author: David Haylock
# * Creation Date: 27-09-2015
# * Copyright: (c) 2015 by David Haylock and Tom Metcalfe
#-------------------------------------------------------

# Import Libraries
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
import urllib2
import podcastparser
import pprint
import time
import getopt
import termios
import os
import subprocess
from pyomxplayer import OMXPlayer
from adxl345 import ADXL345


global omx
TERMIOS = termios
podcastArray = []
podcastTitleArray = []
podcastMP3Array = []
query = ""
M_PI = 3.141592
adxl345 = ADXL345()


#-------------------------------------------------------
#  Fancy Stuff
#-------------------------------------------------------
print "-------------------------------------------------------"
print """ _       ___
| |._ _ | | '_ _  ___  ___  _ _  ___ ._ _  ___  _ _
| || ' || |-| '_>/ ._>/ . || | |/ ._>| ' |/ | '| | |
|_||_|_||_| |_|  \___.\_  |`___|\___.|_|_|\_|_.`_. |
                        |_|                    <___'"""

#-------------------------------------------------------
#  Get new Query from Command Line interface
#-------------------------------------------------------
myopts, args = getopt.getopt(sys.argv[1:],"q:a")
for o, a in myopts:
    if o == '-q':
        query = a
    else:
        query = "gardening"

#----------------------------------------------------
# Function to get keys
#----------------------------------------------------
def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
            c = os.read(fd, 1)
    finally:
            termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

#-------------------------------------------------------
# Setup Proceedures
#-------------------------------------------------------
def getPodcastList(searchTerm):
    print "-------------------------------------------------------"
    resource_url = "https://itunes.apple.com/search?term="+searchTerm+"&entity=podcast"
    print "Looking for " + resource_url
    response = json.loads(urllib2.urlopen(resource_url).read())
    tidy = json.dumps(response,indent=1)
    numberOfResults = response['resultCount']

    for i in range(numberOfResults):
        podcastTitleArray.append(response['results'][i]['collectionName'])
        podcastArray.append(response['results'][i]['feedUrl'])

    print "Found " + str(numberOfResults) + " results"

#----------------------------------------------------
# As it sounds gets the MP3 urls from the podcastArray[val]
#-------------------------------------------------------
def getMP3Lists(podcastURL):
    print "-------------------------------------------------------"
    print "Getting MP3 Links"
    u = urllib2.urlopen(podcastURL)

    # Save the output to the xml file
    localFile = open('mp3s.xml','w')
    localFile.write(u.read())
    localFile.close()
    print "-------------------------------------------------------"
    del podcastMP3Array[:]

    # Parse the content through podcastparser
    parsed = podcastparser.parse(podcastURL, urllib.urlopen(podcastURL))
    print "Found: " + str(len(parsed))
    for i in range(len(parsed)):
        podcastMP3Array.append(parsed['episodes'][i]['enclosures'][0]['url'])
        print "         "+parsed['episodes'][i]['enclosures'][0]['url']


    print "-------------------------------------------------------"

#-------------------------------------------------------
def getNewMP3s():
    randomNumber = 0
    if len(podcastArray) > 0:
        randomNumber = random.randint(0,len(podcastArray)-1)

    print "-------------------------------------------------------"
    print "Podcast Title: " + podcastTitleArray[randomNumber]
    print "Podcast RSS: " + podcastArray[randomNumber]
    getMP3Lists(podcastURL=podcastArray[randomNumber])

#-------------------------------------------------------
#
#-------------------------------------------------------
def stopTrack():
    omx.stop()
    # track.stdin.write('q')
    print "Stop the Track"

#-------------------------------------------------------
# Plays new track at random then deletes the track from
# the array so its not played again
#-------------------------------------------------------
def playNewTrack():
    global track
    if len(podcastMP3Array) > 0:
        randomMP3 = random.randint(0,len(podcastMP3Array)-1)
        print "Play " + podcastMP3Array[randomMP3]
        omx = OMXPlayer(podcastMP3Array[randomMP3])
        # track = subprocess.Popen(['omxplayer','-o','hdmi',podcastMP3Array[randomMP3]],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
        # time.sleep(5)
        # track.stdin.write('q')
        del podcastMP3Array[randomMP3]
    else:
        print "No more tracks ... Getting a new playlist!"
        getNewMP3s()

#-------------------------------------------------------
# Function to return the degrees from the Accelorometer
#-------------------------------------------------------
def convertAccelToAngle(x,y,z):
    roll = (math.atan2(-y,z)*180)/M_PI
    pitch = (math.atan2(x,math.sqrt(y*y + z*z))*180)/M_PI
    print roll
    print pitch

#-------------------------------------------------------
def main_loop():
    while 1:
        axes = adxl345.getAxes(True)
        print "   x = %.3fG" % ( axes['x'] )
        print "   y = %.3fG" % ( axes['y'] )
        print "   z = %.3fG" % ( axes['z'] )
        time.sleep(0.5)
        # c = getkey()
        # if c == 'g':
        #     getNewMP3s()
        # if c == 'p':
        #     # stopTrack()
        #     time.sleep(1)
        #     playNewTrack()

#-------------------------------------------------------
if __name__ == '__main__':
    # Do once on launch though with buttons could reconfigure results
    print "ADXL345 on address 0x%x:" % (adxl345.address)
    getPodcastList(query)

    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by User Request.\n'
        sys.exit(0)
