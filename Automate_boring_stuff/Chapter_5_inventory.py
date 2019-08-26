"""" Add to invetory.

    Inspired from Automate the Boring Stuff with Python - Al Sweigart. Page 120.
"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42,
         'dagger': 1, 'arrow': 12, 'map fragments': 3}


def display_inventory(inventory):
    """ Print contents and total number of items in inventory.
        Signature: (dict) -> None. """
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number of items : ' + str(total))


display_inventory(stuff)

print()   # For display reasons when running both projects

"""List to Dictionary Function for Fantasy Game Inventory"""


def add_to_inventory(inventory, added_items):
    """ Combine a list of loot with an inventory.
        Signature: (dict, list) -> dict."""

    # Add item and use cool method .setdefault() to put a default value if key does not exist
    for loot in added_items:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return(inventory)


inv = {'gold coin': 52, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)