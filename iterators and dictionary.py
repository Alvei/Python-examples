"""
Some examples using iterators and zip.
In one case, we match two equal length list, using zip() and list() to create
a list of tupples. That list can then be converted into a dictionary.

for Python 3.5
"""
import pprint

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


# .setdefault(key, default_value) in action
msg = "The first game of the season should be a good one. Two teams evenly matched."
new_dict = {}

for character in msg:
    # check to see if new_dict[key] exist. If not, set to zero, if yes, do nothing.
    new_dict.setdefault(character, 0)
    new_dict[character] += 1

pprint.pprint(new_dict)

# .get(key, defaut) method tries to get the value for the key and if it does not exist use the default
picnic_items = {'apples': 5, "cups": 2}

print("Bringing", str(picnic_items.get('apples', 0)), "apples")
print("Bringing", str(picnic_items.get('egg', 0)), "eggs")

# but this will return an error
print("Bringing", str(picnic_items['egg']), "eggs")