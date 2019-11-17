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
        num is a nonnegative integer and den is a positive integer"""

    def __init__(self, num: int, den: int) -> None:
        if den == 0:
            raise ZeroDivisionError("Denominator of a rational may not be zero.")

        common = gcd(num, den)
        self._num, self._den = int(num / common), int(den / common)

    @property
    def num(self):
        """ Getter. """
        return self._num

    @property
    def den(self):
        """ Getter. """
        return self._den

    def __add__(self, other):
        return Rational(self._num * other._den + self._den * other._num, self._den * other._den)

    def __sub__(self, other):
        return Rational(self._num * other._den - self._den * other._num, self._den * other._den)

    def __mul__(self, other):
        return Rational(self._num * other._num, self._den * other._den)

    def __truediv__(self, other):
        return Rational(self._num * other._den, self._den * other._num)

    def __str__(self) -> str:
        return f"{self._num:d} / {self._den:d}"

    def __float__(self) -> float:
        return float(self._num) / float(self._den)

    def mixed(self):
        """Renders self as a mixed fraction in string form."""

        # Built-in function divmod() returns 1st the quotient
        # that comes from floor division, then the remainder.
        # or said differently: whole = self.n / self.d, truncated
        #                            n2 = self.n % self.d """
        whole, remainder = divmod(self._num, self._den)

        # Three cases:  1) if self.d == 1 -> return str(self.n)
        #               2) if whole == zero -> return str(n2)+"/"+str(self.d)
        #               3) num is bigger than den such that ans = whole + new_num/den
        if self._den == 1:
            return str(self._num)
        if whole == 0:
            return f"{remainder}/{self._den}"
        return f"{whole} and {remainder}/{self._den}"


def gcd(num: int, num2: int) -> int:
    '''Greatest common divisor function; Euclid's algorithm.'''
    if num2 == 0:
        return num  # Base case
    return gcd(num2, num % num2)


def main():
    """ Test Harness"""
    rat1 = Rational(3, 4)
    rat2 = Rational(3, 4)

    print("Test harness")
    print(f"Num 1 = {rat1} \nNum 2 = {rat2}")
    rat1_float = float(rat1)
    print(f"Num 1 in float = {rat1_float}")

    print(f"Adding them => \t\t({rat1}) + ({rat2}) = {rat1 + rat2}")
    print(f"Substrating them =>\t({rat2}) - ({rat1}) = {rat2 - rat1}")
    print(f"Multiplying them =>\t({rat1}) * ({rat2}) = {rat1 * rat2}")
    print(f"Dividing them =>\t({rat1}) / ({rat2}) = {rat1 / rat2}")

    rat = Rational(4, 1)
    print(f"r = ({rat}) is {rat.mixed()}")
    rat = Rational(0, 2)
    print(f"r = ({rat}) is {rat.mixed()}")
    rat = Rational(5, 2)
    print(f"r = ({rat}) is {rat.mixed()}")


if __name__ == "__main__":
    main()
