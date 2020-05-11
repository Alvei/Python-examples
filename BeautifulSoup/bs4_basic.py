""" YouTube Link: https://www.youtube.com/watch?v=87Gx3U0BDlo

    Ensure that you have both beautifulsoup and requests installed:
    pip install beautifulsoup4
    pip install requests """

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/"
word = "About"
#url = "https://www.youtube.com/watch?v=87Gx3U0BDlo"
#word = "Code"

""" Using the requests module, we use the "get" function provided to access
    the webpage provided as an argument to this function: """
print(f"Opening url:{url}")
result = requests.get("https://www.google.com/")

""" To make sure that the website is accessible, we can ensure that we obtain
    a 200 OK response to indicate that the page is indeed present: """
#print(result.status_code)
result.raise_for_status()

""" For other potential status codes you may encounter,
    consult the following Wikipedia page:
    https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

    We can also check the HTTP header of the website to
    verify that we have indeed accessed the correct page: """
#print(result.headers)

""" For more info on HTTP headers you may consult:
    https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
    Store the page content of the website accessed from requests to a variable: """
src = result.content

""" Now that we have the page source stored, we will use the
    BeautifulSoup module to parse and process the source.
    We create a BeautifulSoup object based on source variable we created above: """
soup = BeautifulSoup(src, 'lxml')

""" Now that the page source has been processed via Beautifulsoup
    we can access specific information directly from it. For instance,
    say we want to see a list of all of the links (defied by "a") on the page: """
links = soup.find_all("a")
#print(f"Type of links: {type(links)}")
print("All the links:")
for link in links:
    print(link)

""" Perhaps we just want to extract the link that has contains the text
    "word" on the page instead of every link. We can use the built-in
    "text" function to access the text content between the <a> </a> tags. """

for link in links:
    if word in link.text:
        print(f"\nfinding word: '{word}' at: {link}")
        print(f"link attribute is: {link.attrs['href']}")