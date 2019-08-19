"""
Etudes_in_sorting.py
Different implementations of sorting

Python 3.5
"""

import operator


def sel_sort(my_list):
    """Selection Sort()
       Assumes that L is a list of elements that can be compared using >.
       Sorts L in ascending order.
       Changes the original list L.
       Time O(len(L)^2) => quadratic
       inplace sorting has constant storage complexity"""
    assert isinstance(my_list, list)      # Check that the input is a list

    suffix_start = 0
    my_swap = 0
    # print(L)

    while suffix_start != len(my_list):

        # Look at each element in suffix
        for i in range(suffix_start + 1, len(my_list)):
            # print("(" + str(suffixStart) + ", " + str(i) + ")")

            if my_list[i] < my_list[suffix_start]:
                # Swap position of elements

                my_list[suffix_start], my_list[i] = my_list[i], my_list[suffix_start]
                # print(L)
                my_swap += 1
        suffix_start += 1
    print("No. of Swap = ", my_swap)


def sel_sort2(my_list):
    """Other implementation of selection sort.
       Easier to read and more elegant
       Signature (list) -> """
    for starting_index in range(len(my_list)):
        #print(" i = ", starting_index, my_list)
        min_element_index = index_of_min(my_list, starting_index)
        # Swap the element in the current iteration with the minElement
        swap(my_list, starting_index, min_element_index)


def index_of_min(a_list, start_index):
    """Returns the index of the min element at or after startIndex"""
    min_element_index = start_index
    for i in range(start_index, len(a_list)):
        if a_list[i] < a_list[min_element_index]:
            min_element_index = i
    return min_element_index


def swap(a_list, i, j):
    """Swaps the value of aList[i] and aList[j].
       No need to return since changing aList by refernce"""
    temp = a_list[i]
    a_list[i] = a_list[j]
    a_list[j] = temp


def merge(left, right, compare):
    """Assumes left and right are sorted lists and
       compare defines an ordering of the elements.
       Returns a new sorted (by compare) list containing the
       same elements"""
    assert isinstance(left, list) and isinstance(right, list)

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remainder of the longer list
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(my_list, compare=operator.lt):
    """Assumes L is a list, compare defines an odering on elements of L
       Returns a new sorted list containing the same elements
       time O(n*log(len(L))
       however because it makes copies it has space complexity of O(len(L)  """
    assert isinstance(my_list, list)

    if len(my_list) < 2:  # Base case
        return my_list[:]

    # Default is not base case
    mid = len(my_list) // 2
    left = merge_sort(my_list[:mid], compare)
    right = merge_sort(my_list[mid:], compare)
    return merge(left, right, compare)


def last_name_first_name(name1, name2):
    """Defines a operator for merge sort.
       The split method creates a list of strings
       Signature: (string, string) -> bolean value"""

    new_name1 = name1.split(' ')
    new_name2 = name2.split(' ')
    if new_name1[1] != new_name2[1]:  # Sort by last name
        return new_name1[1] < new_name2[1]

    # Default -> Last name the same, sort by first name
    return new_name1[0] < new_name2[0]


def first_name_last_name(name1, name2):
    """Defines a operator for merge sort.
       The split method creates a list of strings
       Signature: (string, string) -> bolean value"""
    new_name1 = name1.split(' ')
    new_name2 = name2.split(' ')
    if new_name1[0] != new_name2[1]:  # Sort by first name
        return new_name1[0] < new_name2[0]

    # Default -> First name the same, sort by first name
    return new_name1[1] < new_name2[1]

# Test harness
#------------


def test_sel_sort():
    ''' test_selSort'''
    my_list = list(range(8, 1, -1))  # Need to use List in front of range in Python 3.5
    my_list2 = list(range(8, 1, -1))
    print('\nOriginal list:\t', my_list, "\n\t\t", my_list2)
    sel_sort(my_list)
    sel_sort2(my_list2)
    print('New list:\t', my_list, "\n\t\t", my_list2)


def test_merge_sort1():
    ''' Merge pre-sorted lists L1 and L2
        Sort a list LS'''
    my_list1 = [1, 5, 12, 18, 19, 20]
    my_list2 = [2, 3, 4, 17]
    print('\nL1 => ', my_list1, ' and L2 => ', my_list2, ' => Merging pre-sorted lists')

    my_list3 = merge(my_list1, my_list2, compare=operator.lt)
    print('LR=> ', my_list3)

    my_list4 = list(range(11, 2, -2))
    print('\nLS => ', my_list4, '= => Sorting')

    list_merge_sort = merge_sort(my_list4, compare=operator.lt)
    print('list_merge_sort =>', list_merge_sort)


def test_merge_sort2():
    """Experiment with sorted() function and .sort() method"""
    my_list = [3, 5, 2]
    my_list2 = {'a': 12, 'c': 5, 'b': 'dog'}
    print('\nList =>', my_list, 'and Dictionary =>', my_list2)
    print('Use Sorted function that does not change the orginal list')
    print('Sorted() results =>, ', sorted(my_list), 'Original list is still =>', my_list)

    my_list.sort()
    print('L.sort() results does change L =>', my_list)
    print('Sort dictionary => ', sorted(my_list2))


def test_merge_sort3():
    '''Sort list of names by lastname and then first name'''
    my_list = ['Chris Terman', 'Tom Brady', 'Eric Grimson', 'Gisele Budchen']
    new_list = merge_sort(my_list, last_name_first_name)
    new_list2 = merge_sort(my_list, first_name_last_name)
    print('\nStart list=>\t\t', my_list)
    print('Sorted by last names=>\t', new_list)
    print('Sorted by 1st names=>\t', new_list2)


# Start Testing
# =============
test_sel_sort()
# test_merge_sort1()
# test_merge_sort2()
# test_merge_sort3()
