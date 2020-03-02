"""
    Simple examples of applying functions to a list.
    It mutates the input parameter my_list
"""


def apply_to_each(my_list: list, func: any) -> None:
    """ Mutates my_list by replacing each element , e of my_list by f(e).
        Signature: (list, function) -> None"""
    for index in range(len(my_list)):
        my_list[index] = func(my_list[index])


# simple function
def func2(x: float) -> float:
    return x * x - 1


def main():
    """ Main code """
    L = [1, -2, 3, 3.33]
    print('L =', L)

    apply_to_each(L, abs)
    print(f"Apply Abs()\t=> L = {L}")

    apply_to_each(L, int)
    print(f"Apply int()\t=> L = {L}")

    apply_to_each(L, func2)
    print(f"Apply f()\t=> L = {L}")

if __name__ == '__main__':
    main()
