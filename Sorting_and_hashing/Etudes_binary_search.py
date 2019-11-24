""" Etudes_binary_search.py
    Different ways to do binary searches.
    Binary searches work on SORTED lists or arrays.
    Binary search runs in at worst logarithmic time, making O(log n)
    comparisons, where n is the number of elements in the array,
    the O is Big O notation, and log is the logarithm. """
from typing import Union, List

def binary_search(elem: int, my_list: List[int]) -> Union[int, bool]:
    """ Simple wrapper for binary search for list of integers.
        List must be sorted. """
    assert isinstance(my_list, list)
    assert isinstance(elem, int)

    return binary_search_helper(elem, my_list, 0, len(my_list) - 1)

def binary_search_helper(elem: int, arr: List[int],
                         start: int, end: int) -> Union[int, bool]:
    """ Does the actual binary search recursively. Input already validated.
        List must be sorted. """

    if start > end:
        return False

    mid = (start + end) // 2

    if arr[mid] == elem:
        return mid
    if arr[mid] > elem:
        # recurse to the left of mid
        return binary_search_helper(elem, arr, start, mid - 1)

    # default recurse to the right of mid
    return binary_search_helper(elem, arr, mid + 1, end)

def b_search(elem: int, my_list: list) -> bool:
    """ Binary search that only confirms that the answer is within the list.
        Assumes list in ascending order. """
    assert isinstance(my_list, list)
    assert isinstance(elem, int)

    # len(sequence) is being used inside a condition to determine
    # if a sequence is empty. Instead of comparing the length to 0,
    # rely on the fact that empty sequences are False
    if my_list:
        return b_search_helper(elem, my_list, 0, len(my_list) - 1)  # high has to fit list indexing
    return False

def b_search_helper(elem: int, my_list: List[int], low: int, high: int) -> bool:
    """ Does the work for b_search. Binary search using recursion O(log(n))
        Assumes list is in ascending order. """

    if high == low:
        return my_list[high] == elem

    mid = (low + high) // 2
    #print(f"[{low}, {high}] - mid: {mid} => elem: {elem}")
    if my_list[mid] == elem:
        return True

    if my_list[mid] > elem:     # elem is below the current mid-point
        if low == mid:          # Nothing to search
            return False
        return b_search_helper(elem, my_list, low, mid - 1)

    # default
    return b_search_helper(elem, my_list, mid + 1, high)

def binary_search_while(elem: int, my_list: List[int]) -> Union[int, bool]:
    """ Return the index at which elem lies, or return False if elem is not found
        list must be sorted. """
    assert isinstance(my_list, list)
    assert isinstance(elem, int)

    left, right = 0, len(my_list) - 1

    while left < right:
        mid = (left + right) // 2

        if my_list[left] <= elem and elem <= my_list[mid]:          # elem to the left mid
            right = mid
        elif my_list[mid + 1] <= elem and elem <= my_list[right]:   # elem to the right of mid+1
            left = mid + 1
        elif my_list[left] > my_list[mid]:
            right = mid
        else:
            left = mid + 1

    if my_list[left] == elem:
        return left
    return False

def binary_sort(elem: int, my_list: List[int]) -> Union[int, bool]:
    """ More elegant conditions inside the while loop.
        Return index at which elem lies, or return False/0.
        List must be sorted. """
    assert isinstance(my_list, list)
    assert isinstance(elem, int)

    start, end = 0, len(my_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if elem == my_list[mid]:
            return mid

        if elem < my_list[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False

"""print(binary_search(2, [4, 1, 5, 2, 3]))

print(b_search(1, MY_LIST))
print(b_search(5, MY_LIST))
print(b_search(10, MY_LIST))
"""
MY_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b_search(15, MY_LIST))