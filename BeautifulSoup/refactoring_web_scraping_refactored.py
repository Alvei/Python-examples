# Talk: Conor Hoekstra - Beautiful Python Refactoring
import requests
import lxml.html as lh  # parser
import pandas as pd

url = "http://pokemondb.net/pokedex/all"

page = requests.get(url)  # page handle
doc = lh.fromstring(page.content)  # website content
tr = doc.xpath("//tr")  # html <tr> data

titles = [(t.text_content(), []) for t in tr[0]]
fmt = lambda data: int(data) if data.isnumeric else data

cols = [] * len(titles)
for T in tr[1:]:
    for i, t in enumerate(T.iterchildren()):
        cols[i].append(fmt(t.text_content()))

# Check results
print([len(C) for (title, C) in cols])

Dict = {title: column for (title, column) in cols}
df = pd.DataFrame(Dict)
print(df.head())
