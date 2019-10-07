""" secrets.py
    Simple program to use a offset key to create a secret.
    Only works with alphanumeric characters and single whitespace. """
import string
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

def char_cypher(letter: str, key: int) -> str:
    """ Takes a single alpha character and applies the key offset.
        Does some basic check that the character is in the the alphabet
        punctionation => !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    #alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = string.ascii_letters + ' ' + string.digits + string.punctuation
    len_alpha = len(alphabet)
    position = alphabet.find(letter)

    logging.debug("Character:<%s> Location:%i", letter, position)

    if key >= len_alpha:
        raise ValueError("Key-offset is greater than length of alphabet: <{}>".format(len_alpha))

    if position == -1:
        raise ValueError("A character is not in the alphabet: <{}>".format(letter))

    # To avoid exceeding the number of characters in the alphabet
    # % brings it back to zero and creates a loop on the alphabet
    new_pos = (position + key) % len_alpha

    return alphabet[new_pos]

def cypher(phrase: str, key: int) -> str:
    """ convert a string to a new cypher. """
    if type(phrase) not in [str]:
        raise TypeError ("Type Error, input currently a ", type(phrase))

    new_list = []
    for char in phrase:
        new_list.append(char_cypher(char, key))

    # Convert the list to a string
    return list_to_string(new_list)

def list_to_string(char_list):
    """ using .join() method to join the list. """
    word = ""
    return word.join(char_list)

def main():
    """ Main program """
    key = 19
    phrase = input("Enter a string of charaters: ")
    #print(string.punctuation)
    #phrase = 'b0nj0ur comm3nt ca va!'

    new_phrase = cypher(phrase, key)
    print("New Phrase[{}]:\t\t {}".format(len(new_phrase), new_phrase))

    org_phrase = cypher(new_phrase, -key)
    print("Original Phrase[{}]:\t {}".format(len(org_phrase), org_phrase))

if __name__ == "__main__":
    main()