""" Chapter_8_regex_search.py
    Search for a regex pattern in all txt files in a directory.
    Regext pattern passed finishes with !
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
    also Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 8. Page 195.
"""

import os
import re
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

def look_for_pattern(pattern):
    """ Look for specific regex pattern across all files ending in *.txt.
        Signature: (str) -> None. """

    # Create at list all files in directory
    files = os.listdir(os.getcwd())
    logging.debug(os.getcwd())

    txt_files = []              # List of files with *.txt extensions

    # Filter the files that are not txt files
    txt_doc_regex = re.compile(r'.txt')

    for doc in files:
        if txt_doc_regex.search(doc) is not None:
            logging.debug(doc)
            txt_files.append(doc)

    # Write regex to match a search. In this case looking for pattern ending in !
    search_regex = re.compile(pattern)

    # Open each txt file in turn and if regex triggers print matches to console
    for doc in txt_files:
        # Create an absolute directory path for the doc in list
        opened_file = open('{0}/{1}'.format(os.getcwd(), doc))

        contents = opened_file.read()
        logging.debug("Content of a file:%s\n", contents)
        string = ''.join(contents)
        logging.debug("String:%s", string)
        found = search_regex.findall(string)
        found_str = ' '.join(found)
        print("Answer for this doc:", found_str)


def main():
    """ Test harness """

    pattern = r'\s?\w*\!'
    look_for_pattern(pattern)

if __name__ == "__main__":
    main()