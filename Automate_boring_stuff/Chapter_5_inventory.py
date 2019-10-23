"""" Add to invetory.
    Inspired from Automate the Boring Stuff with Python - Al Sweigart. Page 120."""


def display_inventory(inventory: dict, bag_name: str):
    """ Print contents and total number of items in inventory.
        Signature: (dict) -> None. """
    print(f"Inventory of {bag_name}:")
    total = 0
    for key, value in inventory.items():
        print(f"\t{str(value)} {key}")
        total += value
    print('Total number of items : ' + str(total))


def add_to_inventory(inventory: dict, added_items: list) -> dict:
    """ Combine a list of loot with an inventory."""

    # Add item and use cool method .setdefault() to put a default value if key does not exist
    for loot in added_items:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return(inventory)

def main():
    """ Test Harness """

    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42,
         'dagger': 1, 'arrow': 12, 'map fragments': 3}
    #display_inventory(stuff, "First bag")

    inv = {'gold coin': 52, 'rope': 1}
    display_inventory(inv,"Second bag")
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    print(f"\nAdding loot of {len(dragon_loot)} items")
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv,"Second bag")

if __name__ == "__main__":
    main()