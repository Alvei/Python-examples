import requests, bs4
"""res = requests.get('http://nostarch.com')
print(res.raise_for_status())
no_starch_soup = bs4.BeautifulSoup(res.text, features="lxml")
print(type(no_starch_soup))
"""

example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file.read(), features="lxml")
elems = example_soup.select('#author')
print(f"core object: {type(example_soup)}")
print(f"Tagged object: {type(elems)}")
print(f"Length Tag={len(elems)}")
print(elems[0])