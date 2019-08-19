"""
mortgage.py
Small project to work with different mortgage classes
Inspired from John V. Guttag book
Have one abstract class called Mortgage that encapsulates data and methods
The inheritated classes name the class variable elements appropriately and
define some class specific methods or rewrite the more "master"
method makePayment to meet the needs of the subclass

for Python 3.5"""
import pylab


def findPayment(loan, r, m):
    """Assumes: loan and r are floats, m an int
       Returns the monthly payment for a mortgage of size
       loan at monthly rate of r for m month"""
    return loan * ((r * (1 + r)**m) / ((1 + r)**m - 1))


class Mortgage(object):
    """Abstract class for building different kinds of morgates"""

    def __init__(self, loan, annRate, months):
        """Create a new mortgage"""
        self.loan = loan
        self.rate = annRate / 12.0
        self.months = months
        self.paid = [0.0]   # list of all the payments
        self.owed = [loan]  # list of owed amount decreasing over time
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None  # Description of mortgage

    def makePayment(self):
        """Make a mortgage payment and update key variables: paid & owed"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1] * self.rate
        self.owed.append(self.owed[-1] - reduction)

    def getTotalPaid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)

    def __str__(self):
        return self.legend

    def plotPayments(self, style):  # Style is the line style
        pylab.plot(self.paid[1:], style, label=self.legend)

    def plotBalance(self, style):
        pylab.plot(self.owed, style, label=self.legend)

    def plotTotPd(self, style):
        """Plot the cumulative total of the payments made."""
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, style, label=self.legend)

    def plotNet(self, style):
        """Plot an approximation of the total cost of the mortgage
           over time by plotting the cash expended minus the equity
           acquired by paying off part of the loan. It ignores PV()"""
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])

        # Equity acquired through payments is amount of original loan
        # paid to date, which is amount of loan minus the original loan
        equityAcquired = pylab.array([self.loan] * len(self.owed))
        equityAcquired = equityAcquired - pylab.array(self.owed)
        net = pylab.array(totPd) - equityAcquired
        pylab.plot(net, style, label=self.legend)


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = "Fixed " + str(r * 100) + '%'


class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan * (pts / 100.0)]
        self.legend = "Fixed " + str(r * 100) + '%, '\
            + str(pts) + ' points'


class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r / 12.0
        self.legend = str(teaserRate * 100)\
            + '% for ' + str(self.teaserMonths)\
            + ' months, then ' + str(r * 100) + '%'

    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.owed[-1], self.rate,
                                       self.months - self.teaserMonths)
        Mortgage.makePayment(self)


def pylabplotInitHugo():
    pylab.rcParams['lines.linewidth'] = 4  # Set line width
    pylab.rcParams['axes.titlesize'] = 20  # Set fontsize for titles
    pylab.rcParams['axes.labelsize'] = 20  # Set fontsize for labels
    pylab.rcParams['xtick.labelsize'] = 16  # Set size of numbers on x-axis
    pylab.rcParams['ytick.labelsize'] = 16  # Set size of numbers on y-axis
    pylab.rcParams['xtick.major.size'] = 7  # Set size of ticks on x-axis
    pylab.rcParams['ytick.major.size'] = 7  # Set size of ticks on y-axis
    pylab.rcParams['lines.markersize'] = 10  # Set size of markers


def plotMortgages(morts, amt):
    styles = ['b-', 'b-.', 'b:']  # define the style of the lines

    pylabplotInitHugo

    # Give names to figures
    payments = 0
    cost = 1
    balance = 2
    netCost = 3

    # Configure each figure
    pylab.figure(payments)
    pylab.title('Monthly payment of Different $ ' + str(amt) + ' Mortgage')
    pylab.xlabel('Months')
    pylab.ylabel('Monthly Payment')

    pylab.figure(cost)
    pylab.title('Cash Outlay Different $ ' + str(amt) + ' Mortgage')
    pylab.xlabel('Total Payments')
    pylab.ylabel('Monthly Payment')

    pylab.figure(balance)
    pylab.title('Balance Remaining of Different $ ' + str(amt) + ' Mortgage')
    pylab.xlabel('Months')
    pylab.ylabel('Remaining Loan Balance')

    pylab.figure(netCost)
    pylab.title('Net Cost of Different $ ' + str(amt) + ' Mortgage')
    pylab.xlabel('Months')
    pylab.ylabel('Payment - Equity')

    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
        pylab.figure(balance)
        morts[i].plotBalance(styles[i])
        pylab.figure(netCost)
        morts[i].plotNet(styles[i])

    pylab.figure(payments)
    pylab.legend(loc='upper center')
    pylab.figure(cost)
    pylab.legend(loc='upper center')
    pylab.figure(balance)
    pylab.legend(loc='best')

# Test harness


def compareMortgages(amt, years, fixedRate, pts, ptsRate,
                     varRate1, varRate2, varMonths):
    """ amt is a float representing the initial mortgage amount
        years is a float representing the duration of loan
    """
    totMonths = years * 12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    for m in morts:
        print(m)
        print('Total Payment = $', int(m.getTotalPaid()))

    plotMortgages(morts, amt)


compareMortgages(amt=200000, years=30, fixedRate=0.07, pts=3.25,
                 ptsRate=0.05, varRate1=0.045, varRate2=0.095,
                 varMonths=48)
