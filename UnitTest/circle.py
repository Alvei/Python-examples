from math import pi


def circle_area(radius):
    """ Super simple function to help develop a unit test.
        Signature: (int or float) -> float."""
    if radius < 0:
        raise ValueError ("Value Error, input currently a ", radius)
    if type(radius) not in [int, float]:
        raise TypeError ("Type Error, input currently a ", type(radius))
    return pi * radius **2

def main():
    """ Test harness """
    print("radius =", 1, ':', circle_area(1))
    print("radius =", 0, ':', circle_area(0))
    print("radius =", 2.1, ':', circle_area(2.1))

    print("radius =", -2, ':', circle_area(-2))


if __name__ == "__main__":
    main()