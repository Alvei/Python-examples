"""
Created on Wed Dec 31 17:31:48 2014
python 2.7
"""


# Example from O'lleary book
import json
from urllib import urlopen

# location of the youtube api
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"

# connect to youtube through api
response = urlopen(url)

# Get the info in variable content
contents = response.read()

# Decode the content to a text string in JSON format
text = contents.decode('utf8')

# Convert JSON text to data which is a two-level dictionary
data = json.loads(text)

# Get the data from data one dictionary at a time
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])
