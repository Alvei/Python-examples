""" Calculate pi using approximation.
    pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 + ...
    numerator stays constant at 4 while denominator increases by two
    operation alternate between additions and substraction.
    Inspired by David Kopec Chapter 1. """

def calculate_pi(n_terms: int) -> float:
    """ Approximate PI using Leibniz formula. """
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

if __name__ == "__main__":
    print(f"\npi = {calculate_pi(1000):.6f}")
