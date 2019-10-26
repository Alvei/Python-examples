""" Etudes_returning_fucntions_and_derivatives.py
Different functions that return another function.
scale(): is simply a multiplicative function that takes one input.
         When you assign it to another object you need to provide n.
         Then when you use that new object you need to provide x.

derivative(): returns the approximation f'(x) = (f(x+h) - f(x))/h
              When you assign to object you need to provide the function and h.
              Then when you use the new object, you need to provide x.

kthDerivative(): is a generalization of derivative() to work for derivatives
                 of higher order. It is not bullet proof, did not check that
                 the order is higher than the order of the function provided.
                 It solves the problem in recursive problem.

For Python 3.5 """


def scale(num):
    """Function that returns a function!"""
    return lambda x: num * x


def raise_val(exp):
    """ polymorphic function """
    def inner(num):
        raised = num ** exp   # note that exp is part of the outer scope
        return raised

    return inner


def derivative(func, h):
    """Returns a new function that is the approximation of the derivative
       of a function, f, with respect to h. h should be a small increment"""
    return lambda x: (func(x + h) - func(x)) / h


def square(number):
    """Simple function that squares"""
    return number * number


def quartic(number):
    """ Simple function that puts to the power 4"""
    return number**4


def kth_derivative(func, h, k_deriv):
    """Returns a new function that is the approximation of the kth
       derivative of function, func, with respect to h. """

    if k_deriv == 1:
        return derivative(func, h)  # Base case
    return derivative(kth_derivative(func, h, k_deriv - 1), h)


def test_scale():
    """Test Harness"""
    my_func = scale(32)  # Assign the return function with n = 32

    # Assign the funtion and define the first outer argument - exp
    f_square = raise_val(2)
    f_cube = raise_val(3)

    # exp is different in the two functions since it was defined in the funciton assigment
    print('Polymorphic', f_square(10), f_cube(10), 'should be 100 and 1000')

    print('\nf(2) =', my_func(2), 'should be 64')
    print('f(3) =', my_func(3), 'should be 96')


def test_derivatives():
    """Test Harness"""
    test = derivative(square, 0.0001)
    test2 = derivative(lambda x: x**3, 0.0001)
    test3 = kth_derivative(quartic, 0.0001, 3)
    test4 = kth_derivative(quartic, 0.0001, 2)

    print('derivative of x**2, @ x = 10 => %5.4f should be 20' % (test(10)))
    print('derivative of x**2, @ x = 25 => %5.4f should be 50' % test(25))
    print('derivative of x**3, @ x = 10 => %5.4f should be 300' % test2(10))
    print('derivative of x**3, @ x = 25 => %5.4f should be 675' % test2(15))
    print('3rd derivative of x**4, @ x = 3  => %5.4f should be 72' % test3(3))
    print('3rd derivative of x**4, @ x = 10 => %5.4f should be 242' % test3(10))
    print('2nd derivative of x**4, @ x = 3  => %5.4f should be 108' % test4(3))
    print('2nd derivative of x**4, @ x = 10 => %5.24f should be 1200' % test4(10))


# Testing
# ========
test_scale()
test_derivatives()
