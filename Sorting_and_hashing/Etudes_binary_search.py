"""
Etudes_binary_search.py
Different ways to do binary searches

Binary searches work on SORTED lists or arrays
Binary search runs in at worst logarithmic time, making O(log n)
comparisons, where n is the number of elements in the array,
the O is Big O notation, and log is the logarithm.

"""
# RECURSIVE IMPLEMENTATION
############################


def binary_search(elem: int, my_list: list) -> int:
    """return the index at which elem lies, or return False
       if elem is not found. List must be sorted. """
    assert isinstance(my_list, list)
    return binary_search_helper(elem, my_list, 0, len(my_list) - 1)


def binary_search_helper(elem: int, arr: list, start: int, end: int):
    """ Return the index at which elem lies, or return False if elem is not found.
        List must be sorted"""
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


def b_search_helper(my_list, elem, low, high):
    """binary search using recursion O(log(n))
       Assumes my_list and e are the same type. my_list is in ascending order.
       Returns boolean logical"""

    if high == low:
        return my_list[high] == elem

    mid = (high + low) // 2

    if my_list[mid] == elem:
        return True

    if my_list[mid] > elem:
        if low == mid:  # Nothing to search
            return False
        return b_search_helper(my_list, elem, low, mid - 1)

    # default
    return b_search_helper(my_list, elem, mid + 1, high)


def b_search(my_list: list, elem: int) -> bool:
    """Assumes my_list and elem are the same type. L is in ascending order.
       Returns boolean logical"""
    assert isinstance(my_list, list)

    # len(sequence) is being used inside a condition to determine
    # if a sequence is empty. Instead of comparing the length to 0,
    # rely on the fact that empty sequences are False
    if my_list:
        return b_search_helper(my_list, elem, 0, len(my_list) - 1)  # high has to fit list indexing
    return False

# WHILE IMPLEMENTATIONS
############################


def binary_search_while(elem: int, my_list: list):
    """ Return the index at which elem lies, or return False if elem is not found
        list must be sorted. """
    assert isinstance(my_list, list)

    left, right = 0, len(my_list) - 1

    while left < right:
        mid = (left + right) // 2

        if my_list[left] <= elem and elem <= my_list[mid]:  # elem to the left mid
            right = mid
        elif my_list[mid + 1] <= elem and elem <= my_list[right]:  # elem to the right of mid+1
            left = mid + 1
        elif my_list[left] > my_list[mid]:
            right = mid
        else:
            left = mid + 1

    if my_list[left] == elem:
        return left
    return False


def binary_sort(elem: int, my_list: list) -> int:
    """return the index at which elem lies, or return False/0 if
       elem is not found array must be sorted. """
    assert isinstance(my_list, list)

    start = 0
    end = len(my_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if elem == my_list[mid]:
            return mid
        elif elem < my_list[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False


if __name__ == "__main__":
    MY_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for count in range(0, len(MY_LIST) - 1, 2):
        x = binary_search(count, MY_LIST)
        y = binary_search_while(count, MY_LIST)
        z = binary_sort(count, MY_LIST)
        print(f"Recursion -> Element Index = {str(x)}")
        print(f"WhileLoop -> Element Index = {str(y)}")
        print(f"WhileLoop2-> Element Index = {str(z)}")
