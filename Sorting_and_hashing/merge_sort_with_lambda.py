""" merge_sort_with_lambda.py
Flexible merge Sort using lambda """
from typing import List


def merge_list(left: list, right: list, func) -> list:
    ''' Assumes left and right are sorted lists.
        func defines an ordering on the elements of the lists.
        righteturns a new sorted (by func) list containing the same elements
        as (left + right) would contain.'''

    # Check that the input are lists
    assert isinstance(left, list) and isinstance(right, list)

    result = []
    i, j = 0, 0   # Starting at the beginning of each list

    # Loop while for the length of the shortest list
    while i < len(left) and j < len(right):

        # print "left %i and right %i" %(i,j)
        if func(left[i], right[j]):    # Using Lambda, if x < y
            result.append(left[i])   # Save left most element of left list
            i += 1
        else:
            result.append(right[j])  # Save left most element of rigth list
            j += 1

    # Check to see if there are still elements not saved in left list
    while i < len(left):
        # print "left %i and right %i" %(i,j)
        result.append(left[i])
        i += 1

    # Check to see if there are still elements not saved in right list
    while j < len(right):
        # print "left %i and right %i" %(i,j)
        result.append(right[j])
        j += 1

    return result


def merge_sort(my_list: list, func=lambda x, y: x < y) -> list:
    ''' Returns a new sorted list containing the same elements as L.
        lt is a lambda function left is smaller than right (x<y).
        Input: my_list is assumed to be a list list'''

    assert isinstance(my_list, list)    # Check that the input is a list

    # print "new list = ", my_list
    if len(my_list) <= 1:
        return my_list[:]  # Send back a copy. This is the base case of recursion

    # Non-base case. start recursion after breaking the list in half
    mid = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid], func)  # provide a list from beginning to mid
    right = merge_sort(my_list[mid:], func)  # provide a list from mid to end

    # print "About to merge", left, " and", right
    return merge_list(left, right, func)


def lastNameFirstName(name_1: str, name_2: str) -> bool:
    """ Defining a lambda that can be used to sort names starting with Last names. """
    # Returns a list with each part of name
    name1 = name_1.split(" ")
    name2 = name_2.split(" ")

    if name1[1] != name2[1]:    # Then sort on last name
        return name1[1] < name2[1]
    # Then Sort on first name
    return name1[0] < name2[0]


def firstNameLastName(name_1: str, name_2: str) -> bool:
    """ Defining a lambda that can be used to sort names starting with first names. """
    # Returns a list with each part of name
    name1 = name_1.split(" ")
    name2 = name_2.split(" ")

    if name1[0] != name2[0]:        # Then sort on first name
        return name1[0] < name2[0]
    # then Sort on last name
    return name1[1] < name2[1]

def main():
    """ Main code """
    list1 = [25, 4, 5, 29, 17, 58, 0]

    new_list1 = merge_sort(list1)    # uses default lambda for int
    print(f"{list1} -> {new_list1}")

    list2 = [2.0, 55.121, 44.01, 44.001, 5]
    new_list2 = merge_sort(list2, float.__gt__)  # uses the built-in float greater than as lambda
    print(f"{list2} -> {new_list2}")

    list3 = ['John Guttag', 'Tom Brady', 'Chancellor Grimson', 'Gisele Brady', 'Big Julie']

    new_list3 = merge_sort(list3, lastNameFirstName)
    print(f"\nsorted by last name: {new_list3}")

    new_list3 = merge_sort(list3, firstNameLastName)
    print(f"\nsorted by first name: {new_list3}")


if __name__ == '__main__':
    main()
