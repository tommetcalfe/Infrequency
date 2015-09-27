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
import time
import getopt

podcastArray = []
query = "gardening"


# def setupSearch(argv):
#     try:
#         opts, args = getopt(argv,"hi:o",["term="])
#     except getopt.GetoptError:
#         print 'Infrequency.py -q <your query>'
#         sys.exit(2)
#
#     for opt, arg in opts:
#         if opt == '-h':
#             print 'test.py -q <your query>'
#             sys.exit()
#         elif opt in ("-q", "--term"):
#             query = arg
#             print query


#-------------------------------------------------------
# Setup Proceedures
#-------------------------------------------------------
def getPodcastList(searchTerm):
    resource_url = "https://itunes.apple.com/search?term="+searchTerm+"&entity=podcast"
    response = json.loads(urllib2.urlopen(resource_url).read())
    tidy = json.dumps(response,indent=1)
    numberOfResults = response['resultCount']
    print numberOfResults
    for i in range(numberOfResults):
        print "-------------------------"+str(i)+"------------------------------"
        print "Podcast Name: " + response['results'][i]['collectionName']
        print "Podcast Feed: " + response['results'][i]['feedUrl']
    # print tidy
    # print response

#-------------------------------------------------------
def getMP3Lists(podcastURL):
    print "-------------------------------------------------------"
    print "Getting List"
    u = urllib2.urlopen('http://www.gardenerd.com/Podcasts/Gardenerd_Podcasts.xml')
    localFile = open('mp3s.xml','w')
    localFile.write(u.read())
    localFile.close()
    print "-------------------------------------------------------"
    parsed = podcastparser.parse("http://6ftmama.com/feed/podcast/", urllib.urlopen("http://6ftmama.com/feed/podcast/"))
    # print parsed
    for i in range(len(parsed)):
        podcastArray.append(parsed['episodes'][i]['enclosures'][0]['url'])

#-------------------------------------------------------
def main_loop():
    while 1:
        print "hello"
        time.sleep(0.3)

#-------------------------------------------------------
if __name__ == '__main__':
    # getPodcastList(query)
    # setupSearch(sys.argv[1:])
    getMP3Lists()
    print podcastArray
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by User Request.\n'
        sys.exit(0)
