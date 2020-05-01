""" Chapter_8_mad_libs.py
    Use regex to find all keywords and then replace to substitute for a new words.
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
    also Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 166.
"""
import re, os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# Prompt for file name in cwd to read and save its content to string variable
logging.debug(os.getcwd())

def get_input() -> str:
    """ Signature: (None) -> str. """
    file_name = input('Enter the name of the file to use without the .txt extension: ')
    try:
        file_object = open('{0}/{1}.txt'.format(os.getcwd(), file_name))

    except FileNotFoundError as err:
        print(f"File {file_name} does not exist.")
        find_files_in_dir(r'.txt')
        raise err
    else:
        text = file_object.read()
        file_object.close()
        return text


def find_files_in_dir(pattern: str) -> None:
    """ Find all the files in a current directory that matches a pattern. """
    files = os.listdir(os.getcwd())
    logging.debug(os.getcwd())

    # Filter the files that are not txt files
    txt_files = []
    txt_doc_regex = re.compile(pattern)
    for doc in files:
        if txt_doc_regex.search(doc) is not None:
            logging.debug(doc)
            txt_files.append(doc)
    print(f"Available files: {txt_files}")


def main():
    """ core code """
    text = get_input()

    # text = "The ADJECTIVE panda walked to the NOUN and then VERB."
    print("\n=>", text)

    # Check if there is a one of the key words
    txt_regex = re.compile(r'NOUN|ADJECTIVE|VERB')
    matches = txt_regex.findall(text)
    logging.debug(matches)

    for match in matches:
        new = str(input("Enter a " + match + ": "))
        text = text.replace(match, new )

    print(f"\n=> {text}")

if __name__ == "__main__":
    main()
