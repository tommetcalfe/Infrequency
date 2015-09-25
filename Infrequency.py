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
from xml.dom.minidom import parse
import xml.dom.minidom


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

    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parse("mp3s.xml")
    collection = DOMTree.documentElement
    if collection.hasAttribute("channel"):
       print "Root element : %s" % collection.getAttribute("shelf")

    # Get all the movies in the collection
    # movies = collection.getElementsByTagName("movie")
    # print parser

# getPodcastList("gardening")
getMP3Lists()
