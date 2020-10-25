"""digitconversion.py
Set of functions to manipulate list or convert them.
Python 3.5 """


def int_to_str(number: int) -> str:
    """Returns a decimal string representation of number."""
    assert number >= 0

    digits = "0123456789"
    if number == 0:  # base case
        return "0"

    result = ""
    while number > 0:
        result = digits[number % 10] + result
        number = number // 10  # Remove the last digit
    return result


def add_digits(number: int) -> int:
    """ Returns the sum of the digit in number."""
    assert number >= 0  # Works only wiht positive n

    # Convert the integer into a string (a list)
    string_rep = int_to_str(number)

    total = 0
    for char in string_rep:
        total += int(char)
    return total


def is_subset(my_list1: list, my_list2: list) -> bool:
    """Returns True if each element in my_list1 is also in my_list2."""

    # Check that inputs are lists
    assert isinstance(my_list1, list) and isinstance(my_list2, list)

    for elem1 in my_list1:
        matched = False
        for elem2 in my_list2:
            if elem1 == elem2:
                matched = True
                break  # if e1 was found in L2 got to the next e1
        if not matched:  # if e1 was not found in L2 stop function
            return False
    return True


def intersection(my_list1: list, my_list2: list) -> list:
    """Returns a list that is the intersection of my_list1 and my_list2."""

    # Check that inputs are lists
    assert isinstance(my_list1, list) and isinstance(my_list2, list)

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


def get_binary_rep(number: int, num_digits: int) -> str:
    """number is the number to convert into binary
       num_digit is the number of digits in the binary display.
       Assumes n and numDigits are non-negative ints
       Returns a num_digits str that is a binary representation of n."""

    assert number >= 0  # Works only with positive n

    result = ""
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    if len(result) > num_digits:
        raise ValueError("not enough digits")

    # Pad the front of the display with zeroes
    for _ in range(num_digits - len(result)):
        result = "0" + result
    return result


def gen_power_set(my_list: list) -> list:
    """Returns a list of lists that contains all the possible
       combinations of the elements of my_list."""
    assert isinstance(my_list, list)  # Check that the input is a list

    powerset = []
    for count1 in range(0, 2 ** len(my_list)):
        bin_str = get_binary_rep(count1, len(my_list))
        # print(count1,binStr)

        subset = []
        for index, _ in enumerate(my_list):
            if bin_str[index] == "1":
                subset.append(my_list[index])
                # print(binStr)
                # print 'index = ' + str(index) + '=> ' + str(my_list[index])
        powerset.append(subset)
    return powerset


def search(my_list: list, elem: int) -> bool:
    """ Brute force search of a list
        Assumes my_list and elem are the same type."""

    assert isinstance(my_list, list)  # Check that the input is a list

    for index, _ in enumerate(my_list):
        if my_list[index] == elem:
            return True
    return False


def main():
    """Test Harness"""
    num = 456

    print(f"\nNumber {num} has been converted {type(int_to_str(num))}")
    print(f"\nThe sum of the digits of 456 is: {add_digits(num)}")

    list1 = [3, 4]
    list2 = [1, 2, 3, 4, 5]
    list3 = [1, 2, 4]
    print(f"\n{list1} is a subset of {list2}?: {is_subset(list1, list2)}")
    print(f"\nIntersection of {list1} and {list2}?: {intersection(list1, list2)}\n")

    for index in range(8):
        print(f"fbinary representation of {index} is:\t{get_binary_rep(index, 8)}")

    print(f"\nPower combo of {list3} are: {gen_power_set(list3)}")

    num = 2
    print(f"\nIs {num} part of {list2}?: {search(list2, num)}")


if __name__ == "__main__":
    main()
