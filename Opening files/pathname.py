""" Pathname.py
    Testing different capabilities of the module os.py
"""
import os


# Where are we in the directory hiearchy
cwd = os.getcwd()
print("Current working directory:", cwd )

# Change to a new folder
print("Changing directory....")
new_dir = "C:\\Users\Hugo Sarrazin"
os.chdir(new_dir)
print("Current working directory:", os.getcwd() )

abs_path = os.path.abspath(new_dir)
print("Absolute path", abs_path)

# Check to see if argument is an absolute path
print(os.path.isabs(cwd))

relative_path = os.path.relpath(abs_path, "C:\\")
print ("Relative path after C: is", relative_path)
print(os.path.isabs(relative_path))

# Get the directory and base names
os.chdir(cwd)
print("Dir name:", os.path.dirname(cwd))
print("Base name:", os.path.basename(cwd))
print("Dir and Base names:", os.path.split(cwd))

# Finding file sizes and Folder Contents
print("Size:", os.path.getsize, cwd)
print("List files:", os.listdir(cwd))
total_size = 0
for file in os.listdir(cwd):
    total_size += os.path.getsize(cwd)
print("Total size:", total_size)