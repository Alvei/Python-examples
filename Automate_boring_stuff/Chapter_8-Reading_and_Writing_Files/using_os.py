""" using_os.py
    Various examples of using the os module. """
import os


#######
# Basic
#######
print(f"Current working directory = {os.getcwd()}")

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
    print(os.path.join('C:\\user\\asweigart', filename))

abspath = os.path.abspath('.')
print(f"Absolute Path = {abspath}")
print(f"Is {mypath} an absolute Path = {os.path.isabs(mypath)}?")
print(f"Is {abspath} an absolute Path = {os.path.isabs(abspath)}?")