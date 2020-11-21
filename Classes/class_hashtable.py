""" class_hashtable.py
    Better to use the various built-in dict object who uses HashTable and have
    O(1) but doing this to learn the implementation.

    We will use two lists to represent the key, value pair. We use large enough lists
    that allows us to use the modulus % operator to split our list and find an index.

    Given a collection of items, a hash function that maps each item into
    a unique slot is referred to a perfect hash function. O
    Give in best case O(1) but this can be affected by collisions. """

HASH_SIZE = 11  # choose a prime number of make collision resolution algo efficient


class HashTable:
    """ Basic Hash Table implementation using two lists. """

    def __init__(self, length: int = HASH_SIZE) -> None:
        """ Initialize HashTable. Length should be a prime number.
            slots holds the key whereas data holds the matching value."""
        self.size: int = length
        self.slots: list = [None] * self.size
        self.data: list = [None] * self.size

    def put(self, key, data) -> None:
        """ Put the key, value pair in the HashTable. """
        # Calculate the hash. Different implementation can be used
        # The hash_value ends up the index of the two lists.
        hash_value = self.hash_function(key)

        # If new hash_value, save the key value pair their
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            # Already have that key in that index (hash_value)
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # Replace value for a given key
            # We have a collision!
            else:
                next_slot = self.rehash(hash_value)
                while (
                    self.slots[next_slot] is not None
                    and self.slots[next_slot] is not key
                ):
                    next_slot = self.rehash(next_slot)

                # Found a new empty slot
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    def hash_function(self, key: int) -> int:
        """ Get the index of our lists. Implement the simple remainder method. """
        return key % self.size

    def rehash(self, old_hash):
        """ The collision resolution technique is linear probing with a plus "1" rehash. """
        return (old_hash + 1) % self.size

    def get(self, key):
        """ Key the value corresponding to the key. """
        start_slot = self.hash_function(key)
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
            if position == start_slot:
                stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data) -> None:
        self.put(key, data)


def main():
    """ Test Harness. """
    h = HashTable(HASH_SIZE)
    h[54] = "cat"
    h[26] = "dog"
    h[93] = "lion"
    h[17] = "tiger"
    h[31] = "cow"
    h[44] = "goat"
    h[55] = "pig"
    h[20] = "chicken"

    print(f"Keys:\t{h.slots}")
    print(f"Values:\t{h.data}")

    print(h[20])
    h[20] = "duck"
    print(f"Values:\t{h.data}")


if __name__ == "__main__":
    main()
