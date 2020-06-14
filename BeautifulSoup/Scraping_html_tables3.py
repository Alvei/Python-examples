""" Scraping_html_tables.py
    Inspired by
    https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
    https://python-docs.readthedocs.io/en/latest/scenarios/scrape.html
    https://www.youtube.com/watch?v=W-lZttZhsUY
    https://github.com/codereport/Talks/tree/master/2020-04-PyCon/BeautifulPythonRefactoring
    XPath is a way of locating information in structured documents such as HTML

"""
import requests
import lxml.html as lh
import pandas as pd

url='http://pokemondb.net/pokedex/all'

page = requests.get(url)            # Get html content
tree = lh.fromstring(page.content)   # Use page.content vs page.text b/c html.fromstring expects bytes
table = tree.xpath('//tr')            # Parse data stored between <tr>..</tr> of HTML

# .text_content() returns text contained within an HTML tag w/o HTML markup. Grap 1st row with headers
titles = [name.text_content() for name in table[0]]

# Use conditional to update data
fmt = lambda data : int(data) if data.isnumeric() else data

# Then populate the column content. Iterate over all the remaining row amd oterate over each elements in row
# Convert the elements if needed using the lambda and then the zip(*) is a transpose function
cols = zip(*[[fmt(elem.text_content()) for elem in row.iterchildren()]
                                       for row in table[1:]])

Dict = {title:column for title, column in zip(titles, cols)}
df = pd.DataFrame(Dict)

print(df.head())

# An alternative way of doing this
header = {
    "User-Agent": "Mozilla /5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest" }
#r = requests.get(url, headers=header)
r = requests.get(url)
df2 = pd.read_html(r.text)[0]
print(df2.head())