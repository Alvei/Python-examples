"""
Some examples using iterators and zip.
In one case, we match two equal length list, using zip() and list() to create
a list of tupples. That list can then be converted into a dictionary.

for Python 3.5
"""
import pprint

def use_dict():
    """ Iterator examples. """
    accusation: dict = {'room': 'Ballroom', 'weapon': 'pipe', 'person': 'col. mustard'}
    print('\nDictionary: ', accusation)

    for card in accusation:  # iterates on key
        print(f"card = {card}")

    for value in accusation.values():
        print(f"value = {value}")

    for item in accusation.items():
        print(f"Item (key, value) = {item}")

def use_zip():
    """ Simple example of using zip(). """
    english: list = ['Monday', 'Tuesday', 'Wednesday']
    french: list = ['lundi', 'mardi', 'mercredi']
    print('\nlist 1 =', english)
    print('list 2 =', french)

    # Create iterable
    my_iterator = zip(english, french)
    print("iterator is", my_iterator)

    # create list from iterable
    it_list = list(my_iterator)
    print("List from iterator", it_list)

    # convert list to dictionary
    my_dict = dict(it_list)
    print('Converting list from iterator into dictionary:', my_dict)

def use_setdefault():
    """ .setdefault(key, default_value) in action. """
    msg: str = "The first game of the season should be a good one. "
    new_dict: dict = {}

    for character in msg:
        # check to see if new_dict[key] exist. If not, set to zero, if yes, do nothing.
        new_dict.setdefault(character, 0)
        new_dict[character] += 1

    pprint.pprint(new_dict)

def use_get_dict():
    """ .get(key, defaut) method of dict tries to get the value for the key
        and if it does not exist use the default. """
    picnic_items: dict = {'apples': 5, "cups": 2}

    print("Bringing", str(picnic_items.get('apples', 0)), "apples")
    print("Bringing", str(picnic_items.get('egg', 0)), "eggs")

    # but this will return an error. Can be safer to use the get() method.
    print("*** NEXT LINE WILL RETURN AN ERROR ON PURPOSE")
    print("Bringing", str(picnic_items['egg']), "eggs")

if __name__ == "__main__":
    #use_dict()
    #use_zip()
    use_setdefault()
    #use_get_dict()
