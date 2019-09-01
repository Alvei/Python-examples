""" Chapter_8_mad_libs.py
    Use Regex to extract all the NA phone numbers and emails from a file.
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
    also Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 166.
"""
import re, os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# Prompt for file name in cwd to read and save its content to string variable
logging.debug(os.getcwd())

def get_input():
    """ Signature: (None) -> str. """
    file_name = input('Enter the name of the template file you wish to use: ')
    try:
        file_object = open('{0}/{1}.txt'.format(os.getcwd(), file_name))
        text = file_object.read()
        return text
    except FileNotFoundError as err:
        print("File ", file_name, " does not exist.")
        raise err
    else:
        files = os.listdir(os.getcwd())

        # Filter the files that are not txt files
        txt_files = []
        txt_doc_regex = re.compile(r'.txt')
        for doc in files:
            if txt_doc_regex.search(doc) is not None:
                logging.debug(doc)
                txt_files.append(doc)
        print("Available files:", txt_files)
        file_object.close()


text = get_input()

# text = "The ADJECTIVE panda walked to the NOUN and then VERB."
print("\n=>", text)

# Check if there is a one of the key words
txt_regex = re.compile(r'NOUN|ADJECTIVE|VERB')
matches = txt_regex.findall(text)
logging.debug(matches)

key_words = ['ADJECTIVE', 'NOUN', 'VERB']
for match in matches:
    new = str(input("Enter a " + match + ": "))
    text = text.replace(match, new )

print(text)


