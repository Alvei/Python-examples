""" tut_read_html.py
    Inspired by
    https://www.marsja.se/how-to-use-pandas-read_html-to-scrape-data-from-html-tables/
    """
import pandas as pd

# This is a table with columns a, b, c, d and two rows with numbers
html = '''<table>
  <tr>
    <th>a</th>
    <th>b</th>
    <th>c</th>
    <th>d</th>
  </tr>
  <tr>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
  </tr>
  <tr>
    <td>5</td>
    <td>6</td>
    <td>7</td>
    <td>8</td>
  </tr>
</table>'''

df = pd.read_html(html)
#print(f"ans: {type(df)}\n {df}")  # The resulst are a list

# Scrape data from Wikipedia. In fact, we are going to get the HTML table of Pythonidae snakes (also known as Python snakes).
dfs = pd.read_html('https://en.wikipedia.org/wiki/Pythonidae')
print(f"How many tables on the website {len(dfs)}")
print(f"Printing the 3rd table \n{dfs[2]}")