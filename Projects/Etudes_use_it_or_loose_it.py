
"""
Etudes of use it or loose it.
The 1st is the classic version
While the second uses dynamic program to speed-up time

for Python 3.5
"""


def backpack(capacity, items):
    """ Given a backpack capcity and a list of item consisting of positive
        numbers, return a number indicating the largest sum  that can be made
        from a subset of items without exceeding the capacity."""
    assert capacity >= 0
    assert isinstance(items, list)

    # Base case
    if capacity == 0 or items == []:
        return 0
    elif items[0] > capacity:  # Item does not fit therefore reject it
        return backpack(capacity, items[1:])

    # loseIt is the case where you do not keep the item and keep going
    # useIt is the case where you put item in the backpack"""
    else:
        lose_it = backpack(capacity, items[1:])
        use_it = items[0] + backpack(capacity - items[0], items[1:])
        return max(lose_it, use_it)


def distance(first, second):
    """Returns the edit distance between first and second word."""

    if first == '':  # if first is empty, distance is  copying second
        return len(second)
    elif second == '':  # if second is empty, distance is copying first
        return len(first)
    elif first[0] == second[0]:  # first character of first & second are same
        return distance(first[1:], second[1:])
    else:
        # All operations on first
        # Substition: replacing the 1st letter of first by 1st letter of second
        # Insertion: insering the 1st character of second in front of first
        # Deletion: deleting the 1st character of first
        substitution = 1 + distance(first[1:], second[1:])
        insertion = 1 + distance(first, second[1:])
        deletion = 1 + distance(first[1:], second)
        return min(substitution, insertion, deletion)


# Test harness
MY_LIST = [5, 8, 10, 20, 45]
CAPACITIES = [42, 22, 80, 12]    # Different capacities
print('\n')
for cap in CAPACITIES:
    print('Backpack capacity is', cap, 'Sum of items is ', backpack(cap, MY_LIST))

print('\nDistance between spam and poems =>', distance('spam', 'poems'), " should be 4")
print('Distance between alien and sales =>', distance('alien', 'sales'), " should be 3")
print('Distance between sales and alien =>', distance('sales', 'alien'), " should be 3")
