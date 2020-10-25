import requests
import lxml.html as lh  # parser
import pandas as pd

url = "http://pokemondb.net/pokedex/all"

# Store the contents of the website under doc
page = requests.get(url)
doc = lh.fromstring(page.content)

# Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath("//tr")

# Check the length of the first 12 rows
# print([len(T) for T in tr_elements[:12]])

### Parse the Table Header ####
col = []
i = 0
# For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i += 1
    name = t.text_content()
    print('%d:"%s"' % (i, name))
    col.append((name, []))

# print (col)

### Creating the Panda DF ###
# Since out first row is the header, data is stored on the second row onwards
for j in range(1, len(tr_elements)):
    # T is our j'th row
    T = tr_elements[j]

    # If row is not of size 10, the //tr data is not from our table
    if len(T) != 10:
        break

    # i is the index of our column
    i = 0

    # Iterate through each element of the row
    for t in T.iterchildren():
        data = t.text_content()
        # Check if row is empty
        if i > 0:
            # Convert any numerical value to integers
            try:
                data = int(data)
            except:
                pass
        # Append the data to the empty list of the i'th column
        col[i][1].append(data)
        # Increment i for the next column
        i += 1

# Check results
print([len(C) for (title, C) in col])

Dict = {title: column for (title, column) in col}
df = pd.DataFrame(Dict)

