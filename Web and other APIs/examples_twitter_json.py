
"""
Created on Wed Dec 31 20:02:35 2014
for python 2.7

"""
import urllib2
import json

url = "https://api.twitter.com/1/statuses/user_timeline.json?\
       include_entities=true&include_rts=true&screen_name=twitterapi&count=2"

if __name__ == "__main__":
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    data = json.load(f)   # Converting in python based data such as list, strings, dict

    for item in data:
        print(item.get('create_at'))
