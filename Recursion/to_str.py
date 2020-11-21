""" Convert a string a number in any base. """


def to_str(num: int, base: int):
    """ """
    convert_string = "0123456789ABCDEF"

    if num < base:
        return convert_string[num]  # Base case, return a string

    return to_str(int(num / base), base) + convert_string[num % base]


def main():
    """ Test Harness. """
    tests = [(10, 2, "1010"), (8, 2, "1000"), (32, 16, "20"), (15, 16, "F")]
    for num, base, ans in tests:
        print(f"{to_str(num, base)} ? {ans}")


if __name__ == "__main__":
    main()
