"""
Some examples using iterators and zip.
In one case, we match two equal length list, using zip() and list() to create
a list of tupples. That list can then be converted into a dictionary.

for Python 3.5
"""
# Iterator examples
accusation = {'room': 'Ballroom', 'weapon': 'pipe', 'person': 'col. mustard'}
print('\nDictionary: ', accusation)

for card in accusation:  # iterates on key
    print('card =', card)

for value in accusation.values():
    print('value =', value)

for item in accusation.items():
    print('Item (key, value) = ', item)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'lundi', 'mardi', 'mercredi'
print('\nlist 1 =', english)
print('list 2 =', french)
# Create iterable
it = zip(english, french)
print("iterator is", it)


# create list from iterable
it_list = list(it)
print("List from iterator", it_list)

# convert into dictionary
d = dict(it_list)
print('Converting list from iterator into dictionary:', d)
