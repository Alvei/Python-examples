""" Different ways to get value from dict in increasing pythonic ways
"""

my_dict: dict = {'ID124': "bob", "ID345": "Majo", "ID445": "superman" }

def return_name1(key):
    """ Not very robust, if wrong key is used, crashes with Key Error"""
    return my_dict[key]

def return_name2(key):
    """ Does not crash but not very inefficient. Need to check for  key-value pair being present"""
    if key in my_dict:
        return my_dict[key]
    return "Key not found"

def return_name3(key):
    """ Does not crash and more efficient."""
    try:
        return my_dict[key]
    except KeyError:
        return "Key not found"

def return_name4(key):
    """ Does not crash and leverages dict.get() built-in capabilities including default when not found."""
    return my_dict.get(key, "Key not found")

print("Test 1:", return_name1("ID124"))
print("Test 2:", return_name2("ID124"))
print("Test 2:", return_name2("ID125"))
print("Test 3:", return_name3("ID124"))
print("Test 3:", return_name3("ID125"))
print("Test 4:", return_name4("ID124"))
print("Test 4:", return_name4("ID125"))