""" downloadXkcdpy.py
    Learn to use beautiful soup
    Inspired by automate the boring stuff. chapter 11
"""
import requests, os
from bs4 import BeautifulSoup       # Import specific class

url = 'http://xkcd.com'             # Starting url
os.makedirs('xkcd', exist_ok=True)  # Store comics in ./xkcd

print("\n\n")
count = 0                           # To limit the number of images downloaded

while (not url.endswith("#")) and count <= 10:
    count +=1
    print(f"Downloading page {url}...")
    res = requests.get(url)

    # Check all worked and raise question exception if not 200 but 1st print
    print(f"Was url found (200 is good, 404 is bad): {res.status_code}")
    res.raise_for_status()

    # Create soup object with the text found in res. Could have done it with .content method also
    soup = BeautifulSoup(res.text)

    comic_elem = soup.select("#comic img")  # Find the URL of the comic image

    if comic_elem == []:
        print("Could not find comic image.")
    else:
        # Found the url of the image
        comic_URL = "http:" + comic_elem[0].get('src')

        print(f"Downloading image {comic_URL}")
        res = requests.get(comic_URL)
        res.raise_for_status()

        # Save the image to ./xkcd
        base = os.path.basename(comic_URL)
        newfile = os.path.join("xkcd", base )
        print(f"base: {base} and newfile: {newfile}")
        image_file = open(newfile, "wb")

        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

        # Get the prev button's url
        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prev_link.get("href")

print("\nDone.")