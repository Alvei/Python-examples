"""
Rational_class.py
Rational(num, den):

.__add__(self, other):
    [ other is a Rational instance ->
     return the sum of self and other as a Rational instance ]
.__sub__(self, other):
    [ other is a Rational instance ->
     return the difference of self and other as a Rational instance ]
.__mul__(self, other):
    [ other is a Rational instance ->
     return the product of self and other as a Rational instance ]
.__div__(self, other):
    [ other is a Rational instance ->
     return the quotient of self and other as a Rational instance ]
.__str__(self):
    [ return a string representation of self ]
.__float__(self):
    [ return a float approximation of self ]
.mixed(self):
        [ return a string representation of self as a mixed fraction ]
"""


class Rational():
    """ Rational (num, den):
        num is a nonnegative integer and den is a positive integer
        Signature (int, int) -> Rational instance"""

    def __init__(self, num, den):
        if den == 0:
            raise ZeroDivisionError("Denominator of a rational may not be zero.")
        else:
            common = gcd(num, den)
            self.n, self.d = int(num / common), int(den / common)

    def __add__(self, other):
        return Rational(self.n * other.d + self.d * other.n, self.d * other.d)

    def __sub__(self, other):
        return Rational(self.n * other.d - self.d * other.n, self.d * other.d)

    def __mul__(self, other):
        return Rational(self.n * other.n, self.d * other.d)

    def __truediv__(self, other):
        return Rational(self.n * other.d, self.d * other.n)

    def __str__(self):
        return "{0:d} / {1:d}".format(self.n, self.d)

    def __float__(self):
        return float(self.n) / float(self.d)

    def mixed(self):
        """Renders self as a mixed fraction in string form."""

        # Built-in function divmod() returns 1st the quotient
        # that comes from floor division, then the remainder.
        # or said differently: whole = self.n / self.d, truncated
        #                            n2 = self.n % self.d """
        whole, remainder = divmod(self.n, self.d)

        # Three cases:  1) if self.d == 1 -> return str(self.n)
        #               2) if whole == zero -> return str(n2)+"/"+str(self.d)
        #               3) num is bigger than den such that ans = whole + new_num/den
        if self.d == 1:
            return str(self.n)
        if whole == 0:
            return "%s/%s" % (remainder, self.d)
        return "%s and %s/%s" % (whole, remainder, self.d)


def gcd(num, num2):
    '''Greatest common divisor function; Euclid's algorithm.
       Signature (int, int) -> int '''

    if num2 == 0:
        return num  # Base case

    return gcd(num2, num % num2)


def test_rationale():
    """ Test Harness"""
    rat1 = Rational(3, 4)
    rat2 = Rational(3, 4)

    print("Num 1 =", rat1)
    print("{} + {} = {}".format(rat1, rat2, rat1 + rat2))
    print("{} - {} = {}".format(rat2, rat1, rat2 - rat1))
    print("({}) * ({}) = {}".format(rat1, rat2, rat1 * rat2))
    print("({}) / ({}) = {}".format(rat1, rat2, rat1 / rat2))

    rat1_float = float(rat1)
    print(rat1_float)

    rat = Rational(4, 1)
    print("r = ({}) is {}".format(rat, rat.mixed()))
    rat = Rational(0, 2)
    print("r = ({}) is {}".format(rat, rat.mixed()))
    rat = Rational(5, 2)
    print("r = ({}) is {}".format(rat, rat.mixed()))


test_rationale()
# generalTests()