"""
    Newton-Raphson for polynomial
    Find x such that f(x) - k is within epsilon.
    Returns final guess and number of iteration
    for Python 3.5."""


def Newton_RaphsonSquareRoot(k, epsilon):
    """square root
    Find x such that x**2 - k is within epsilon.
    Newton Raphson => x(n+1) = x(n) - f[x(n)] / df[x(n)]
    Here f(x) = x**2 - k
    Returns final guess and number of iteration."""
    n = 0
    x0 = k / 2.0  # Generate the initial guess
    f_x = x0**2 - k

    while abs(f_x) >= epsilon:
        x0 = x0 - (f_x / (2 * x0))  # Newton-Raphson equation for f(x) = x**2-k
        n += 1
        f_x = x0**2 - k
    return x0, n

# Super Elegant general form if you know the function and its derivative
# --------------------------------------------------------------------


def newtonsMethod(f, df, x0, e):
    """ f is the function f(x) for which we are looking for roots
        df is the derivative of the function f(x)
        x0 is the guess
        e is the precisions
    """
    n = 0
    while abs(f(x0)) > e:
        x0 = x0 - f(x0) / df(x0)  # Newton-Raphson approximation
        n += 1

    #print('***Root is at: %4.4f with f(x) around %4.4e' % (x0, f(x0)) )
    return x0, n


''' root = newtonRaphson(f,df,a,b,tol=1.0e-9).
    Finds a root of f(x) = 0 by combining the Newton-Raphson
    method with bisection. The root must be bracketed in (a,b).
    Calls user-supplied functions f(x) and its derivative df(x).
'''


def newtonRaphson(f, df, a, b, tol=1.0e-9):
    import error
    from numpy import sign

    fa = f(a)
    if fa == 0.0:
        return a
    fb = f(b)
    if fb == 0.0:
        return b
    if sign(fa) == sign(fb):
        error.err('Root is not bracketed')

    x = 0.5 * (a + b)
    for i in range(30):
        fx = f(x)
        if fx == 0.0:
            return x
      # Tighten the brackets on the root
        if sign(fa) != sign(fx):
            b = x
        else:
            a = x
      # Try a Newton-Raphson step
        dfx = df(x)
      # If division by zero, push x out of bounds
        try:
            dx = -fx / dfx
        except ZeroDivisionError:
            dx = b - a
        x = x + dx
      # If the result is outside the brackets, use bisection
        if (b - x) * (x - a) < 0.0:
            dx = 0.5 * (b - a)
            x = a + dx
      # Check for convergence
        if abs(dx) < tol * max(abs(b), 1.0):
            return x
    print('Too many iterations in Newton-Raphson')

# Test Harness
#-------------


def test_Newton_RaphsonSquareRoot():
    roots = [4, 24, 64, 195]
    epsilon = 0.0001

    print('\nSqrt(x)\t is about \t# iterations')
    print('========================================')
    for k in roots:
        guess, n = Newton_RaphsonSquareRoot(k, epsilon)
        #print('Sqrt(%d) is about %4.4f found in %d iterations' % (k, guess, n ))
        print('%d\t%4.4f\t\t%d ' % (k, guess, n))

    print('\n')
    for k in roots:
        guess, n = newtonsMethod(lambda x: x**2 - k, lambda y: 2 * y, k / 2, epsilon)
        print('%d\t%4.4f\t\t%d ' % (k, guess, n))

#-------------
# Root is at:  0
# f(x) at root is:  0
# Root is at:  0.628668078167
# f(x) at root is:  -1.37853879978e-06
# Root is at:  1
# f(x) at root is:  0


def f(x):
    return 6 * x**5 - 5 * x**4 - 4 * x**3 + 3 * x**2


def df(x):
    return 30 * x**4 - 20 * x**3 - 12 * x**2 + 6 * x


def test_newtonsMethod():
    x0s = [0.25, .5, 2]  # Different guesses for the roots

    print('\nRoot of polynomial example:')
    for x0 in x0s:
        r, n = newtonsMethod(f, df, x0, 1e-5)
        print(' %4.4f' % r)


def test_newtonsMethod2():
    # Using short functions g(x) and g'(x)
    def g(x): return x**2 + 2 * x + 1

    def gp(x): return 2 * x + 2
    roots = newtonsMethod(g, gp, 20, 1e-5)
    print('\n X**2 + 2*X + 1 => (roots, n) = ', roots)

# Testing
#=============


test_Newton_RaphsonSquareRoot()
print('\n')
test_newtonsMethod()
test_newtonsMethod2()


def g(x): return x**2 - 2


def gp(x): return 2 * x


print('\n')
r = newtonRaphson(g, gp, 0.5, 12, tol=1.0e-9)
print('Root of f(x) = X**2 -2  => ', r)
