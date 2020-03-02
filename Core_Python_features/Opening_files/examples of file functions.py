"""
Examples of I/O
Created on Sun Dec 28 07:45:23 2014 """
import os
from os.path import dirname, join
from pprint import pprint
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)


def num_words(file_name):
    ''' function to count the words in a file.
        Signature: (str) -> int.'''

    with open(file_name, 'r') as file_object:
        total = 0
        for line in file_object:
            count = len(line.split())
            total += count
        logging.debug("total = %s count = %s", total, count)
        return total


def most_common(file_name):
    ''' Function to returns the most common word in a file in a unsorted dictionary.
        Signature: (str) -> dict {word: word count}'''

    with open(file_name, 'r') as file_object:
        words = {}
        for line in file_object:        # Loop of each line
            line_words = line.split()   # Creates a list of words for that line

            for word in line_words:     # Loop over the list of words
                if word in words:       # Check to see if in dictionary
                    words[word] += 1    # Add to the counter
                else:
                    words[word] = 1     # Create a new word in dict with count 1
        # print("list of items: ", words.items())
        # return sorted(words.items(), key=lambda x: x[1], reverse=True)[0]
        return words                    # Unsorted dict


def get_key(item):
    """ Simple function to return the 2nd item from a tuple
        Signature: (tuple(any)) -> any. """
    return item[1]  # return the 2nd item of the tuple on which we will sort


def main():
    """ Main code """
    file_name =  "lorem.txt"
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./", file_name)
    logging.debug(os.getcwd())

    print("\nNumber of words: ", num_words(file_path))

    my_dict = most_common(file_path)
    list_words = my_dict.items()       # Create a dictionary of tuples (word, word_count)
    print("\n Dict of words:")
    print(list_words)

    # replaces the lambda function,
    # uses get_key with no argument since assumes list_words, the first argument
    # get_key returns the second elements of the tuple which is the word count
    new_list = sorted(list_words, key=get_key, reverse=True)
    print("\n LIst of words:")
    print(new_list)
    print("Largest: ", new_list[0])


if __name__ == '__main__':
    main()
