"""
Basic statistical functions
Created on Mon Dec 29 06:56:45 2014
for Python 3.5"""
import math
import pylab


def my_combination(item_n, group_r):
    ''' Function that implements the basic combination.
        item_n is the total number of items
        group_r is the size of group taken each time
        Needs math module
        Signature: (int, int) -> int'''

    assert isinstance(item_n, int) and isinstance(group_r, int)  # Input should be integers
    assert (item_n - group_r) > 0                        # myCombination() input test

    return math.factorial(item_n) / (math.factorial(group_r) * math.factorial(item_n - group_r))


def my_binomial_prob(prob, k, num_trial):
    ''' Function that calculates a single Binomial Proabability.
        Needs function myCombination and the math module
        Input:
        k is number of successes
        n-k is the number of failures
        Signature: (int, int, int) -> float
    '''
    assert (num_trial - k) > 0   # my_combination() input test
    failure_q = 1 - prob         # probability of failure
    ans = my_combination(num_trial, k) * prob**k * failure_q**(num_trial - k)
    return ans


def main():
    """ Main code """

    prob = 0.1
    k = 1         # number of success
    num = 5       # number of trials
    ans = []

    # Build a list of probabilities if you try n times
    for index in range(2, num + 1):
        ans.append(my_binomial_prob(prob, k, index))

    print(ans)

    # if you want to know the probability of having at least 1 successful trial
    # calculate the probabily of having none and substract from it

    trial_max = 10
    trials = range(1, trial_max + 1)  # Number of trials

    y10 = []
    y20 = []
    for trial in trials:
        y10.append(1 - my_binomial_prob(.1, 0, trial))
        y20.append(1 - my_binomial_prob(.2, 0, trial))

    print(ans)

    pylab.plot(trials, y10, trials, y20)
    pylab.grid()
    pylab.xlabel("Number of trials")
    pylab.ylabel("Cummulative probability")


if __name__ == '__main__':
    main()
