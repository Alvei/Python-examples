""" Read_file.py """

from os.path import dirname, join

def read_file(file_name: str, debug: bool = False) -> str:
    """ Read a file and return a long string while doing some basic error checking. """

    # Find the location of the current directory. Assumes the text file is in the same directory
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./", file_name)

    with open(file_path, 'rt') as in_file:
        try:
            # Read the entire file into a string variable
            contents = in_file.read()
            if debug:
                print("Original file:\n", contents, '\n', sep="")
            return contents
        except IOError:
            print(f"Unable to load {file_path} Check that it exists.")
            return "IOError"
