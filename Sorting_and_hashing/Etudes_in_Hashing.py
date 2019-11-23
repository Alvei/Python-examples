"""
Etudes in Hashing.py
Having fun with simple hashing

for Python 3.5
"""


class int_dict():
    """Create a dictionary with integer keys."""

    def __init__(self, num_buckets):
        """ Create empty dictionary.
            num_buckets is the number of buckets in dictionary"""

        # Buckets are lists of dict entries(dict_key,dict_value)
        self.buckets = []
        self.num_buckets = num_buckets
        for _ in range(num_buckets):
            self.buckets.append([])

    def add_entry(self, dict_key, dict_val):
        """Assumes dict_key an int. Adds an entry.
           Uses simple hashing function => %
           Collisions are handle by replacing old dict_value with new one."""

        # Use Hashing function to find the right bucket
        # Each bucket is a list of dict entries [(dict_key, dict_value)...]
        loc = dict_key % self.num_buckets
        hash_bucket = self.buckets[loc]

        for index, _ in enumerate(hash_bucket):  # Loop through the list to see if there
            if hash_bucket[index][0] == dict_key:
                hash_bucket[index] = (dict_key, dict_val)  # Collision => replace
                return
        hash_bucket.append((dict_key, dict_val))  # Not in list append to it

    def get_value(self, dict_key):
        """Assumes dict_key is an int.
           Returns entry associated with dict_key.
           Uses simple hashing function => %"""

        # Use Hashing function to find the right bucket
        # Each bucket is a list of dict entries ([(dict_key, dict_value)...]
        loc = dict_key % self.num_buckets
        hash_bucket = self.buckets[loc]

        print(hash_bucket)

        for elem in hash_bucket:  # Each bucket can have more than one entry
            if elem[0] == dict_key:
                return elem[1]  # return the dict_value
        return None

    def __str__(self):
        result = '{'
        for buck in self.buckets:
            for elem in buck:
                result = result + str(elem[0]) + ' : ' + str(elem[1]) + ', '
        return result[:-1] + '}'  # result[:-1] omits the last commma


def test_hashing():
    """Test Harness"""

    # Initialize list of numbers
    test_list = [54, 33, 16, 45, 14, 15, 54]
    length = len(test_list)
    print('\nLength of dictionary and hashing function is: ', length)
    my_dict = int_dict(length)  # Initialize dictionary
    num = 0

    print('\nThe input to the dictionary => the output of hashing function %', length)

    # Loop over list of numbers K. The actual number i is the key
    # num is a simple counter to highlight the location in the list
    # hBucket is the location where to store the value
    for elem in test_list:
        name = 'Value ' + str(num)
        my_dict.add_entry(elem, name)  # Enter key,value pairs
        hbucket = elem % length
        print(elem, ' : ', name, ' => ', str(hbucket))
        num += 1

    print('\nThe dictionary entries of the int_dict are:\n', my_dict)
    print('\nThe buckets are:')
    num = 0
    for hash_bucket in my_dict.buckets:  # Violates abstraction barriers....
        print(num, hash_bucket)
        num += 1


test_hashing()
