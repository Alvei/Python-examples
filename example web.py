# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 19:00:31 2015

@author: Hugo Sarrazin
"""



""" Simple web calls with a web site that gives quotes"""
import urllib as ur
url = 'http://www.iheartquotes.com/api/v1/random'
conn = ur.urlopen(url)      # Assign object
print conn                  # conn is an instance HTTPREsponse object
data = conn.read()          # Get the data from web page
print data
print "status: ", conn.code  # HTTP status code, 200 is good
print conn.headers          # Gives you the full header and the keys
print conn.headers.getheaders('Content-Type') # Defines the type of text



""" Simpler version of the same code using request library """
#import requests
#
#url = 'http://www.iheartquotes.com/api/v1/random'
#
#response = requests.get(url)
#
#print response
#
#print response.text         # The content of the text
#print response.status_code  # HTTP status code, 200 is good
#print response.headers
#print response.url          # Confirmed the url