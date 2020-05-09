""" YouTube Link: github from vprusso

    Let's obtain the links from the following website:
    https://www.whitehouse.gov/briefings-statements/

    One of the things this website consists of is records of presidential
    briefings and statements.

    Goal: Extract all of the links on the page that point to the
    briefings and statements. """

import requests
from bs4 import BeautifulSoup

url = "https://www.whitehouse.gov/briefings-statements/"
result = requests.get(url)
print(f"Downloading image {url}")
res = requests.get(url)
res.raise_for_status()              # Make sure it worked
src = result.content                    # Get the content that was captured by requests
soup = BeautifulSoup(src, 'lxml')       # Convert into a bs4 object

""" On WH page, through inspection we discover that all url are inside the h2 tag. """
urls = []
for h2_tag in soup.find_all('h2'):
    a_tag = h2_tag.find('a')            # For each h2_tag get the a tag
    urls.append(a_tag.attrs['href'])    # Get the attrs for the the links inside the a tag

for url in urls:
    print(url)
