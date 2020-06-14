""" Scraping_html_tables.py
    Inspired by
    https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
    https://python-docs.readthedocs.io/en/latest/scenarios/scrape.html
    https://www.youtube.com/watch?v=W-lZttZhsUY
    XPath is a way of locating information in structured documents such as HTML

"""
import requests
import lxml.html as lh
import pandas as pd

url='http://pokemondb.net/pokedex/all'

page = requests.get(url)            # Get html content
tree = lh.fromstring(page.content)   # Use page.content vs page.text b/c html.fromstring expects bytes
table = tree.xpath('//tr')            # Parse data stored between <tr>..</tr> of HTML

# Create a list of tuples (name, [])
# Populate the 1st element with name of column.
# .text_content() returns text contained within an HTML tag w/o HTML markup.
col = [(name.text_content(), []) for name in table[0]]

# Use conditional to update data
fmt = lambda data : int(data) if data.isnumeric() else data

# Then populate the column content
for row in table[1:]:
    for i, elem in enumerate(row.iterchildren()):
        col[i][1].append(fmt(elem.text_content()))

Dict = {title:column for (title,column) in col}
df = pd.DataFrame(Dict)

print(df.head())