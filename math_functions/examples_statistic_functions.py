"""
Basic statistical functions
"""
import math

def my_combination(item_n: int, group_r: int) -> float:
    ''' Function that implements the basic combination.
        item_n is the total number of items
        group_r is the size of group taken each time
        Needs math module. '''

    assert isinstance(item_n, int) and isinstance(group_r, int)  # Input should be integers
    assert (item_n - group_r) > 0                        # myCombination() input test

    return math.factorial(item_n) / (math.factorial(group_r) * math.factorial(item_n - group_r))


def my_binomial_prob(prob: float, k: int, num_trial: int) -> float:
    ''' Function that calculates a single Binomial Proabability.
        Needs function myCombination and the math module
        Input:
        k is number of successes
        n-k is the number of failures   '''
    assert (num_trial - k) > 0   # my_combination() input test
    assert isinstance(num_trial, int) and isinstance(k, int)
    assert isinstance(prob, float)
    failure_q = 1 - prob         # probability of failure

    ans = my_combination(num_trial, k) * prob**k * failure_q**(num_trial - k)
    return ans


def main():
    """ Main code """

    prob = 0.1
    k = 1         # number of success
    num = 5       # number of trials

    # Build a list of probabilities if you try n times
    ans = [my_binomial_prob(prob, k, index) for index in range(2, num + 1)]

    print(f"\n{ans}")

if __name__ == '__main__':
    main()
