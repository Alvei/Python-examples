"""
    Simple examples of applying functions to a list.
    It mutates the input parameter my_list
    for Python 3.5."""


def apply_to_each(my_list, func):
    """ Mutates my_list by replacing each element , e of my_list by f(e)
        Signature: (list, function) -> None"""
    for index in range(len(my_list)):
        my_list[index] = func(my_list[index])


# simple function
def func2(x):
    return x * x - 1


def main():
    """ Main code """
    L = [1, -2, 3, 3.33]
    print('L =', L)

    print('\nApply Abs()')
    apply_to_each(L, abs)
    print('L =', L)

    print('\nApply int()')
    apply_to_each(L, int)
    print('L =', L)

    print('\nApply f()')
    apply_to_each(L, func2)
    print('L =', L)


if __name__ == '__main__':
    main()
