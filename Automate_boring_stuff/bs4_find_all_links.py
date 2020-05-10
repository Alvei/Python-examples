""" bs4_find_all_links.py
    Download all linked pages from a given URL and note any 404's.
    Project from Automate the Boring Stuff, chapter 11. """

import requests
import bs4

#url = input('Enter the URL that you would like to verify the links for: ')
url = "https://www.yahoo.com/"
print(f"\nOpening website: {url}")
res = requests.get(url)
res.raise_for_status()                              # Check that nothing went wrong

soup = bs4.BeautifulSoup(res.text, 'html.parser')   # Convert to bs4 object
links = soup.select('a')                            # Find all the links
fof = []                                            # List of links that led to 404 page

print(f"Found {len(links)} links")
for link in links:
    try:
        unmade_url = link['href']
        print(f"Found link: {unmade_url}")

        # Check to see if it is a valid url
        if unmade_url.startswith('http'):
            to_check = unmade_url

        elif unmade_url.startswith('//'):
            to_check = 'https:' + unmade_url

        elif unmade_url.startswith('#'):
            to_check = url + unmade_url

        #print(f"\tChecking link: {unmade_url}")
        result = requests.get(to_check)

        if result.status_code == 404:
            fof.append(to_check)

    except:
        pass

print(f'\nLinks processed these {len(fof)} returned error 404:')
print('\n'.join(fof))