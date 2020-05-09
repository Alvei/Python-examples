""" downloadXkcdpy.py """
import requests, os, bs4

url = 'http://xkcd.com'             # Starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

print("\n\n")

while not url.endswith("#"):

    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()                  # Check all worked

    soup = bs4.BeautifulSoup(res.text)      # Load the page to bs4

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
        prev_link = soup.select('a[rel="prev')[0]
        url = 'http://xkcd.com' + prev_link.get("href")

print("\nDone.")