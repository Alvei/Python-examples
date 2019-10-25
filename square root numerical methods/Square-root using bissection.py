""" Find root of simple polynomial y**power = x using bissection. """

from typing import Optional  # Needed for None

def find_root(x: float, power: int, epsilon: float) -> Optional[float]:
    """ Find root of simple polynomial y**power = x using bissection.
        Returns float y such that y**power is within epsilon of x.
        If such a float does not exist, it returns None. """

    # Check for input validity. Avoiding imaginary numbers
    if x < 0 and power % 2 == 0:
        return None

    num_guesses = 0
    low, high = min(-1.0, x), max(1.0, x)
    ans = (high + low) / 2.0

    while abs(ans**power - x) >= epsilon:
        num_guesses += 1
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    # print('num_guesses =', num_guesses)
    return ans


def main():
    """ Test harness """
    epsilon = 0.0001

    # Test for < 1 and negative numbers
    for test in (0.25, -0.25, 2, -2, 8, -8):

        for power in range(1, 4):
            print(f"Testing => (x, power) = ({test},{power})")
            result = find_root(test, power, epsilon)

            if result is None:
                print('    No Roots')
            else:
                print(f"\tAns = {result:.4f} => {result**power:.4f} ~= {test}")


if __name__ == "__main__":
    main()
