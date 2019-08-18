""" find_extreme_divistors.py
@author: Hugo Sarrazin for Python 3.5
"""

def find_extreme_divisors(num1, num2):
    """ Returns a tuple containing the smallest common divisor > 1
    and the largest commmon divisior of num1 and num2
    Signature: (int, int) -> tuple
    """

    assert num1 > 0 and num2 > 0

    #divisors = () # The empty tuple
    min_val, max_val = None, None

    for i in range(2, min(num1, num2) + 1):
        # Check to see if it can divide both n1 and n2
        if num1%i == 0 and num2%i == 0:
            if min_val is None or i < min_val:
                min_val = i
            if max_val is None or i > max_val:
                max_val = i
        #print( 'i = ', i, ' Min = ', min_val, ' Max = ', max_val )
    return (min_val, max_val)

def test_find_extreme_divisors():
    """ Test harness """
    min_div, max_div = find_extreme_divisors(100, 200)
    print('[min, max] = [', min_div, ',', max_div, ']')

test_find_extreme_divisors()
