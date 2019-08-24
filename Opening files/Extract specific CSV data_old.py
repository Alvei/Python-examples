"""
reading CSV.py

Practice using CSV
Created on Sat Mar 31 08:39:41 2018
http://zetcode.com/python/csv/
http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/

for python 3.5
"""

import csv, pprint
from os.path import dirname, join


def read_two_lists(file_path, key_col, value_col):
    """ Read two lists from the csv data that will become (key, value) pairs 
        Signature (string, int, int) -> tuple(list, list)."""

    with open(file_path) as csvfile:
        try:
            readCSV = csv.reader(csvfile, delimiter=',')
        except IOError:
            print('Unable to load "%s".  Check that it exists.' % csvfile)
            return

        values = []
        keys = []
        for row in readCSV:
            key = row[key_col]          
            value = row[value_col]

            values.append(value)
            keys.append(key)

        # Return a tuple with the two lists
        print("List of Values =", values)
        print("List Keys =", keys)
        return (keys, values) 

def read_dict(file_path, key_col, value_col):
    """ Read the csv data. In this case, we know upfront the data we want to store. 
        The 1st (value) and 4th columns (key).
        Signature (string) -> dict."""

    with open(file_path) as csvfile:
        try:
            readCSV = csv.reader(csvfile, delimiter=',')
        except IOError:
            print('Unable to load "%s".  Check that it exists.' % csvfile)
            return
        my_dict = {}

        for row in readCSV:
            my_dict[row[key_col]] = row[value_col]         # Need to know the organization of data

        print("Dictionary:", my_dict)

        return my_dict 

def find_list_match(list1, list2, key):
    """ Uses the fact that index in one list is the same for the other list.
        Signature: (list, list) -> None."""

    # Basic error checking
    try:
            index = list1.index(key.lower())
            value = list2[index]
            print('The value of key', key, 'is:', value)
    except Exception as e:
            print("Exception:", e)


def find_value(my_dict, key):
    """ Return the value.
        Signature: (dict, str) -> str."""

    # Basic error checking
    try:
            value = my_dict[key.lower()]
            print('The value for the key', key, 'is:', value)
    except Exception as e:
            print("Exception:", e)


def main():
    """ Test harness. """
    file_name = 'color.csv'
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./", file_name)

    # (colors, dates) = read_two_lists(file_path, 3, 0)
    my_dict = read_dict(file_path, 3, 0)

    what_color = input('What color do you wish to know the date of?:')
    # find_list_match(colors, dates, what_color)
    find_value(my_dict, what_color)   


if __name__ == "__main__":
    main()
