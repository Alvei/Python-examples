""" chap9_backup2zip.py
    info on os.walk https://www.geeksforgeeks.org/os-walk-python/
    os.walk(folder) returns a generator with three variables
    path[]:   The current path starting from root
    subdir[]: The subfolders in that directory
    file[]:   The files in the current path"""
import datetime
import os
import re
from typing import List
from zipfile import ZipFile

def create_zip_version(filename: str) -> str:
    """ Determine if the filename exist and adjust backup filename. Ensure name is not empty."""

    assert len(filename) != 0
    path = os.path.abspath(filename)  # Makes sure path is absolute path

    number = 1
    while True:
        # .basename() returns the base name of pathname, 2nd element of the pair returned
        # by passing path to the function split(). https://docs.python.org/3/library/os.path.html
        zip_filename = os.path.basename(path) + "_" + str(number) + ".zip"
        if not os.path.exists(zip_filename):
            break
        number += 1
    return zip_filename

def print_info(archive_name: str) -> None:
    """ To access all of meta-data about the ZIP contents, use the infolist()
        or getinfo() methods. https://pymotw.com/2/zipfile/ """

    my_zf = ZipFile(archive_name)
    for info in my_zf.infolist():
        print(f'\n{info.filename}')
        print(f'\tComment:\t{info.comment}')
        print(f'\tModified:\t{datetime.datetime(*info.date_time)}')
        print(f'\tSystem:\t\t{info.create_system} (0 = Windows, 3 = Unix)')
        print(f'\tZIP version:\t{info.create_version}')
        print(f'\tCompressed:\t{info.compress_size} bytes')
        print(f'\tUncompressed:\t{info.file_size} bytes')

def get_all_file_paths(directory: str) -> List[str]:
    """ Crawling the directory to be zipped. """

    assert len(directory) != 0
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths

def backup2zip(name: str, detail=False, skip=None) -> None:
    """ Backup the entire content of folder into a ZIP file. """

    assert len(name) != 0

    zip_filename = create_zip_version(name)
    print(f"\nFile saved as: {zip_filename}")

    if skip:
        raw_skip = r"{}".format(skip)
        print(f"Will skip files that contains: {raw_skip}")

    match_regex = re.compile(raw_skip)

    # Create a list of all the files
    folder = os.path.abspath(name)        # Makes sure folder is absolute
    file_paths = get_all_file_paths(folder)
    print(f"\nFolder saved: {folder}")
    print(f"Number of files found: {len(file_paths)}")
    files_saved = 0

    # Walk the entire folder tree and compress the files in each folder
    with ZipFile(zip_filename, 'w') as zip_backup:
        # writing each file one by one
        for file_path in file_paths:
            if file_path.endswith(".zip"):
                print(f"\tSkipping: {os.path.basename(file_path)}")
            elif match_regex.search(file_path) is not None:
                print(f"\tSkipping: {os.path.basename(file_path)}")
            else:
                zip_backup.write(file_path)
                files_saved += 1
                if detail:
                    print(f"\tAdding {os.path.basename(file_path)}")

    print(f'Zipped {files_saved} successfully!')

def play_os_walk(name: str) -> None:
    """ Function to test the return values of os.walk(). """

    print(f"\nFilename:\t{name}")
    path = os.path.abspath(name)
    print(f"Path:\t\t{path}")
    print(f"Basename:\t{os.path.basename(path)}")

    tree = list(os.walk(path))  # os.walk() is a generator
    for k in tree:
        print(f"\nPath = {k[0]}")
        print(f"Folder = {k[1]}")
        print(f"File = {k[2]}")

def main():
    """ Main file. """
    source_folder = "C:\\Users\\Hugo Sarrazin\\Documents\\GitHub\\Python-examples\\Core_Python_features\\Error_Handling"
    skip_files = '.json'
    raw_skip = r"{}".format(skip_files)
    print(raw_skip)
    #print_info(zipfilename)
    #play_os_walk(os.getcwd())

    backup2zip(source_folder, detail=False, skip=skip_files)

if __name__ == "__main__":
    main()
