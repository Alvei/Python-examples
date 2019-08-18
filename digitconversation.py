"""digitconversation.py
Set of functions to manipulate list or convert them.
Python 3.5 """


def int_to_str(number):
    """Returns a decimal string representation of number
       Signature: (int) -> string"""
    assert number >= 0   # Works only wiht positive number

    digits = '0123456789'
    if number == 0:          # base case
        return '0'

    result = ''
    while number > 0:
        result = digits[number % 10] + result
        number = number // 10       # Remove the last digit
    return result


def add_digits(number):
    """Returns the sum of the digit in number.
       Signature: (int) -> int """
    assert number >= 0   # Works only wiht positive n

    string_rep = int_to_str(number)     # Convert the integer into a string (a list)

    total = 0
    for char in string_rep:
        total += int(char)
    return total


def is_subset(my_list1, my_list2):
    """Returns True if each element in my_list1 is also in my_list2.
       Signature: (list, list) -> boolean """
    assert isinstance(my_list1, list) and isinstance(my_list2, list)  # Check that inputs are lists

    for elem1 in my_list1:
        matched = False
        for elem2 in my_list2:
            if elem1 == elem2:
                matched = True
                break       # if e1 was found in L2 got to the next e1
        if not matched:     # if e1 was not found in L2 stop function
            return False
    return True


def intersection(my_list1, my_list2):
    """Returns a list that is the intersection of my_list1 and my_list2.
       Signature: (list, list) -> list """
    assert isinstance(my_list1, list) and isinstance(my_list2, list)  # Check that inputs are lists

    # Build a list containing common elements
    tmp = []
    for elem1 in my_list1:
        for elem2 in my_list2:
            if elem1 == elem2:
                tmp.append(elem1)

    # Build a list without duplicates
    result = []
    for elem in tmp:
        if elem not in result:
            result.append(elem)
    return result


def get_binary_rep(number, num_digits):
    """number is the number to convert into binary
       numDigit is the number of digits in the binary display.
       Assumes n and numDigits are non-negative ints
       Returns a numDigits str that is a binary representation of n"""
    assert number >= 0   # Works only with positive n

    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    if len(result) > num_digits:
        raise ValueError('not enough digits')

    # Pad the front of the display with zeroes
    for _ in range(num_digits - len(result)):
        result = '0' + result
    return result


def gen_power_set(my_list):
    """Returns a list of lists that contains all the possible
       combinations of the elements of my_list.
       Signature: (list) -> list """
    assert isinstance(my_list, list)      # Check that the input is a list

    powerset = []
    for count1 in range(0, 2 ** len(my_list)):
        bin_str = get_binary_rep(count1, len(my_list))
        # print(count1,binStr)

        subset = []
        for index, _ in enumerate(my_list):
            if bin_str[index] == '1':
                subset.append(my_list[index])
                # print(binStr)
                # print 'index = ' + str(index) + '=> ' + str(my_list[index])
        powerset.append(subset)
    return powerset


def search(my_list, elem):
    """Brute force search of a list
       Assumes my_list and e are the same type.
       Signature: (list, int) -> bool"""
    assert isinstance(my_list, list)      # Check that the input is a list

    for index, _ in enumerate(my_list):
        if my_list[index] == elem:
            return True
    return False

# Test Harness


TEST_STRING = int_to_str(456)
print('\nString number', TEST_STRING, 'where s is a ', type(TEST_STRING))

print('\nThe sum of the digits of 456 is:', add_digits(456))

print('\n[3,4] is a subset of [1,2,3,45]?:', is_subset([3, 4], [1, 2, 3, 4, 5]))
print('\nIntersection of [3,4] and [1,2,3,45]?:', intersection([3, 4], [1, 2, 3, 4, 5]), '\n')

for i in range(16):
    print('binary representation of', i, 'is:\t', get_binary_rep(i, 8))

print('\nPower combo of [1,2,4] are:', gen_power_set([1, 2, 4]))

print('\nIs 3 part of [1,2,3,4,5]:', search([1, 2, 3, 4, 5], 3))
