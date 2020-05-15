""" using_os.py
    Various examples of using the os module. """
import os

def size_folder(myfolder: str) -> int:
    """ Find the size of a folder. """
    total = 0
    for file in os.listdir(cwd):
        newfile = os.path.join(cwd, file)
        total += os.path.getsize(newfile)

    return total

#######
# Basic
#######
cwd = os.getcwd()
print(f"Current working directory = {cwd}")

# Changing directory. Need to use two backslash in windows
os.chdir('C:\\Users\\Hugo Sarrazin\\Documents')
print(f"Current working directory = {os.getcwd()}")

# Combine different elements to create a path
# In windows it will be backslash whereas it will be forwardslash for others
# To work in both environment you can use the .join() method.
mypath = os.path.join('usr', 'bin', 'spam')
print(f"\npath combo = {mypath}")

myfiles = ['account.txt', 'details.csv', 'invite.docx']

for filename in myfiles:
    # Works on windows because of double backslash
    print(os.path.join('C:\\user\\bsmith', filename))

#######
# Path
#######
abspath = os.path.abspath('.')
print(f"Absolute Path = {abspath}")
print(f"Is {mypath} an absolute Path = {os.path.isabs(mypath)}?")
print(f"Is {abspath} an absolute Path = {os.path.isabs(abspath)}?")

path1 = "C:\\windows"
path2 = "C:\\"
relpath = os.path.relpath(path1, path2)
print(f"Relative Path between {path1} and {path2} is => {relpath}")

print(f"Breaking the absolute path {abspath} into its components")
print(f"dirname = {os.path.dirname(abspath)} and base = {os.path.basename(abspath)}")

# To get a tuple
path_tuple = os.path.split(abspath)
print(path_tuple)

# To get all the elements, use os.path.sep which identifies the right separator for the OS
path_elements = abspath.split(os.path.sep)
print(path_elements)

###############################
# file size and folder content
###############################
filename = 'README.md'
thispath = os.path.join(cwd, filename)
print(f"Size of {filename}: {os.path.getsize(thispath)}")
print(f"files in cwd: {os.listdir(cwd)}")

# Loop through all the files in a directory
for file in os.listdir(cwd):
    newfile = os.path.join(cwd, file)
    print(f"{os.path.getsize(newfile)}\t{file}")

print(f"Total size of folder = {size_folder(cwd)}")

########################
# Checking path validity
########################
print(f"{os.path.exists(cwd)}")
print(f"{os.path.isfile(cwd)}")
print(f"{os.path.isdir(cwd)}")