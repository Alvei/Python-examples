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

url='http://dfkoz.com/ai-data-landscape/'

page = requests.get(url)             # Get html content
tree = lh.fromstring(page.content)   # Use page.content vs page.text b/c html.fromstring expects bytes
table = tree.xpath('//tr')            # Parse data stored between <tr>..</tr> of HTML

# Create a list of tuples (name, [])
# Populate the 1st element with name of column.
# .text_content() returns text contained within an HTML tag w/o HTML markup
# Then populate the column content
# col = [(name.text_content(), []) for name in table[0]]
col = []
for name in table[0]:
    col.append( (name.text_content(), []) ) # Get the name of the column and initialize and empty list

#print(f"Col={col}")
print(f"lenght of table {len(table)}")
for row in table[1:]:

    for i, elem in enumerate(row.iterchildren()):
        data = elem.text_content()
        # Check if row is empty
        try:
            data=int(data)
        except:
            pass

        # Append the data to the empty list of the i'th column
        col[i][1].append(str(data).strip())

Dict = {title:column for (title, column) in col}
df = pd.DataFrame(Dict)

print(df.shape)
df.to_csv("List_AI.csv")