""" Convert a list of multiple integers into a single integer.
"""
from typing import List


def convert1(lst: List[int]) -> int:
    """ Iterate over each element and accumulate them in a string. """

    # iterating each element. print statement changed end from EOL to "" to avoid line return
    res = ''
    for index in lst:
        # print(index, end="")
        res = res + str(index)
    return int(res)

def convert2(lst: List[int]) -> int:
    """ First convert the list of integer into a list of strings
        (join() works with strings only). Then, join them using join().
        It takes a time complexity of O(n). """

    # Converting integer list to string list
    string = [str(i) for i in lst]

    # Join list items using join()
    res = int("".join(string))
    return(res)


def convert3(lst: List[int]) -> int:
    """ Converting integer list to string list and joining the list using join(). """

    res = int("".join(map(str, lst)))
    return res

def main():
    # creating a list of integer
    lst = [12, 15, 17]
    print(convert1(lst))
    print(convert2(lst))
    print(convert3(lst))

if __name__ == "__main__":
    main()
