"""multi_files_clip.py
    Saves, loads and deletes pieces of text to the clipboard.
    From Automate the Boring stuff. Chapter 8.
    Usage:
    py.exe mcb_ext.pyw save <keyword> - Saves clipboard to keyword
    py.exe mcb_ext.pyw <keyword> - Loads keyword contents to clipboard
    py.exe mcb_ext.pyw list - Loads all keywords to clipboard
    py.exe mcb_ext.pyw delete <keyword>- Deletes saved keyword and contents
    py.exe mcb_ext.pyw delete_all - Deletes all keywords from clipboard
"""

import shelve  # Module to save binary data to hard-drive
import sys
import pyperclip

# Open binary file
mcb_shelf = shelve.open('mcb')

# Save the clipboard contents to keyword
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # pyperclip.paste() takes the content of the clipboard
    # mcb_shelf stores in a dictionary. The key is sys.argv[2]
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    print(f"{sys.argv[2]} saved successfully.")

# Delete keyword and associated content
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]
    print(f"{sys.argv[2]} deleted")

elif len(sys.argv) == 2 and sys.argv[1].lower() != 'delete_all':
    # List stored keywords
    if sys.argv[1].lower() == 'list':
        # mcb_shelf.keys() returns a "list" of all the key words but
        # still need to use the list() function to convert into an actual list
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print(f'List of all keywords copied to clipboard.')
    # Load content associated with chosen keyword to the clipboard
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print(sys.argv[1] + ' loaded successfully')
    # Inform user that their input doesn't match a saved keyword
    else:
        print('That keyword doesn\'t exist - so nothing'
              'has been loaded to the clipboard')

# Clear all shelved entries
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete_all':
    mcb_shelf.clear()
    print('All keywords and associated contents have been deleted.')

mcb_shelf.close()
