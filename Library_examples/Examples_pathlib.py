""" Examples uses of Pathlib module. Path lib is supported throughout the standard library due 
to the addition of the file system path protocol.
References:
realpython.com/python-pathlib 
Trey Hunner as a Blog Dec 2018. treyhunner.com/2018/12/why-you-should-be-using-pathlib/
https://docs.python.org/3/library/pathlib.html """

from pathlib import Path
import collections


def tree(directory):
    """ Create a directory tree. """
    print(f"+ {directory}")
    for path in sorted(directory.rglob("*")):
        depth = len(path.relative_to(directory).parts)
        spacer = "      " * depth
        print(f"{spacer}+ {path.name}")


def main():
    """ Test Harness. """

    my_dir = Path.cwd()
    print(f"\nCurrent working directory: {my_dir}")

    # Return a new path object representing the user’s home directory
    home = Path.home()
    print(f"Home: {home}")

    # Create a new path. The slash operator helps create child paths, similarly to os.path.join()
    new_dir = my_dir / "temp"
    print(f"New_dir: {new_dir}")

    # Checking type
    print(f"type of variabel: {type(my_dir)}")

    # Doing the same with .joinpath()
    new_dir2 = my_dir.joinpath("temp")
    print(f"Check if the slash and .joinpath() are the same? {new_dir == new_dir2}")

    ###### Opening file  #####
    path = new_dir / "text.txt"
    with open(path, mode="r") as file_input:
        for line in file_input:
            print(line.strip())  # .strip() required to remove EOL

    # Using convenience method
    print("\n")
    print(path.read_text())

    # Even more direct
    print(Path(new_dir / "text.txt").read_text())

    #### Using Path properties #####
    # .anchor is the part of the path before the directories
    # .parent returns another path object whearas others return strings
    print(
        f"name: {path.name}\nparent: {path.parent}\nstem: {path.stem}\nsuffix: {path.suffix}\nanchor: {path.anchor}"
    )

    #### Moving and Deleting ####
    # Because it does not have safe moving of files use
    destination = path
    try:
        with destination.open(mode="xb") as fid:
            fid.write(source.read_bytes())  # focused on try/except not on working case!
    except IOError:
        print(f"\n*** {destination.name} already exist. ***")

    ### Counting ###
    path = Path(".")  # Initialize object

    # Listing Python source files in this directory tree
    f = list(path.glob("*.py"))
    print(f"Files: {f}")
    file_count = collections.Counter(p.suffix for p in path.iterdir())
    print(f"Counting files: {file_count}")

    # Listing subdirectories
    tree(Path.cwd())

    current_dirs = [x for x in path.iterdir() if x.is_dir()]
    print(f"\nSubdirectories: {current_dirs}")

    #### Find the last modified file ####
    from datetime import datetime

    # f in my_iterdir() loops through the current files
    # (f.stat().st_mtime, f) is a tuple
    # .stat() gets info on file. .st_mtime gives the time of the last modification
    time, file_path = max((f.stat().st_mtime, f) for f in my_dir.iterdir())
    print(f"Last modified: {file_path.name} on: {datetime.fromtimestamp(time)} ")


if __name__ == "__main__":
    main()
