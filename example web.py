"""
Simple web calls with a web site that gives quotes.
Created on Sat Jan 03 19:00:31 2015
Originally for python 2.7
Updated for python 3.X https://realpython.com/python-requests/
"""


# import urllib as ur
import requests
"""
url = 'http://www.iheartquotes.com/api/v1/random'
conn = ur.urlopen(url)      # Assign object

print(conn)                	# conn is an instance HTTPREsponse object
data = conn.read()          # Get the data from web page

print(data)
print("status: ", conn.code)  	# HTTP status code, 200 is good
print(conn.headers)          	# Gives you the full header and the keys
print(conn.headers.getheaders('Content-Type')) 	# Defines the type of text
"""


""" Version of the same code using request library compatible with Python 3.x"""


url = 'http://www.iheartquotes.com/api/v1/random'

response = requests.get(url)

print("Response:", response)

print("Text:", response.text)         # The content of the text
print("Code:", response.status_code)  # HTTP status code, 200 is good
print("Header:", response.headers)
print("Url:", response.url)          # Confirmed the url
