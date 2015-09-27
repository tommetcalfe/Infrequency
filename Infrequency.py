#!/usr/bin/env python

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

podcastArray = []

#-------------------------------------------------------
# Setup Proceedures
#-------------------------------------------------------
def getPodcastList(searchTerm):
    response = urllib2.urlopen("https://itunes.apple.com/search?term="+searchTerm+"&entity=podcast").read()
    print response

#-------------------------------------------------------
def getMP3Lists():
    print "-------------------------------------------------------"
    print "Getting List"
    u = urllib2.urlopen('http://www.gardenerd.com/Podcasts/Gardenerd_Podcasts.xml')
    localFile = open('mp3s.xml','w')
    localFile.write(u.read())
    localFile.close()
    print "-------------------------------------------------------"
    parsed = podcastparser.parse("http://www.gardenerd.com/Podcasts/Gardenerd_Podcasts.xml", urllib.urlopen("http://www.gardenerd.com/Podcasts/Gardenerd_Podcasts.xml"))

    for i in range(len(parsed)):
        podcastArray.append(parsed['episodes'][i]['guid'])

getMP3Lists()
print podcastArray
