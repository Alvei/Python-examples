#
# Simple function to reverse a string
#######################################


def reverse(text):
    ''' Function that is reversing the text it receives '''
    new_text = ''
    text = str(text)   # Convert the argument into a string if not already
    my_list = len(text) - 1

    for letter in text:
        new_text = new_text + text[my_list]
        my_list -= 1

    return new_text
