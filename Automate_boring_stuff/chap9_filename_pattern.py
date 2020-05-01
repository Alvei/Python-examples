""" Search for a regex pattern in filenames inside the current directory."""
import os
import re
from typing import List

def find_file_with_pattern(raw_match: str) -> List[str]:
    """ Function to find files that matches regex pattern in raw string format. """

    match_regex = re.compile(raw_match)

    # List all files in directory and filter those that are not txt files.
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}\n")
    files = os.listdir(os.getcwd())


    # Doing match using list comprehension
    #files_lower = [file.lower() for file in files]
    match_files = [doc for doc in files if match_regex.search(doc) is not None]
    print(f"Found {len(files)} files, {len(match_files)} had filename matching the pattern: '{raw_match}'\n")
    return match_files

if __name__ == "__main__":
    MATCH = 'chapter_'
    NEW = 'chap'
    match_files = find_file_with_pattern(r'{}'.format(MATCH))
    #print(match_files)

    for doc in match_files:
        new_name = doc.replace(MATCH, NEW)
        print(f"{doc}\t\t\t\t {new_name}")
        os.rename(doc, new_name)
