"""Etudes_random_walk.py
Program inspired by Intro to Computation and Programming using Python
Location class is used to determine the position in cartesian grid.
Field class maintains a mapping of drunks and locations.
Drunk and UsualDrunk classes

for Python 3.5
"""
import random
import numpy as np
import pylab


def stdDev(X: list) -> list:
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    mean = float(sum(X)) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot / len(X))**.5  # Square root of mean differences


def CV(X):
    """Coefficient of variation"""
    mean = sum(X) / float(len(X))
    try:
        return stdDev(X) / mean
    except ZeroDivisionError:
        return float('nan')


class Location(object):
    """2D representation of location.
       move() changes the location.
       distFrom() caculates the distance between current point and another one."""

    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self): return self.x

    def getY(self): return self.y

    def distFrom(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**.05

    def __str__(self):
        return '< {},{}>'.format(self.x, self.y)


class Field(object):
    """addDrunk() adds drunks but they cannot occupy the same location.
       moveDrunk() changes the location of the drunk on the field."""

    def __init__(self):
        self.drunks = {}  # Initializes a dictionary of drunk numbers and locations

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field - does not exist')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]

        # Use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object):
    def __init__(self, name=None):
        """Assumes name is a str"""
        self.name = name

    def __str__(self):
        if self is not None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    """Child class of Drunk but restricts thes steps to x or y."""

    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class ColdDrunk(Drunk):
    """Child class of Drunk but restricts the steps to x or y."""

    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class EWDrunk(Drunk):
    """Child class of Drunk but restricts the steps to x or y."""

    def takeStep(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def walk(f, d, numSteps):
    """Assumes f is a Field, d is a Drunk in f, and numStep an int >= 0.
       Moves d numSteps times, and returns the difference between
       the final location and the location at the start of the walk."""
    start = f.getLoc(d)  # Store initial location
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))  # Return the distance travel


def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps an int >= 0, numTrials an int >0.
       dClass is a subclass of Drunk
       Simulates numTrials walks of numSteps steps each.
       Returns a list of the final distances for each trial."""

    # Initialization
    Homer = dClass()
    origin = Location(0.0, 0.0)
    distances = []

    for t in range(numTrials):
        f = Field()  # Create new field
        f.addDrunk(Homer, origin)  # Add Homer at the origin
        distances.append(walk(f, Homer, numSteps))  # Update listof distances
    return distances


def drunkTest(walkLengths, numTrials, dClass):
    """Assumes walkLengths a sequence of ints >= 0
       numTrials an int >0, dClass a subclass of Drunk
       For each number of steps in walkLengths, runs simWlaks with
       numTrials walks and prints results"""

    means = []
    print('\n', dClass.__name__, 'random walk')
    print('Steps\tMean\tCV\tMax\tMin')
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)

        mean = sum(distances) / len(distances)
        means.append(mean)
        print('{0:d}\t{1:.4f}\t{2:.4f}\t{3:.3f}\t{4:.3f}'.format(numSteps,
                                                                 mean, CV(distances), max(distances), min(distances)))

    """pylab.plot(walkLengths, means)
    pylab.xlabel('Number of steps')
    pylab.ylabel('Drunk distance from origin')
    pylab.title('Comparison of distance travelled')
    pylab.show()"""


class styleIterator(object):
    """Simple class to help iterate across different style for pylab"""

    def __init__(self, styles):
        self.index = 0
        self.styles = styles  # List of styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


def simDrunk(numTrials, dClass, walkLengths):
    """Runs the simulation a number of times (numTrials)
       returns a tupple of mean distance travels and covariance"""

    meanDistances = []
    CVDistances = []

    for numSteps in walkLengths:
        print('Starting siumulation of {} steps'.format(numSteps))
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials) / float(len(trials))
        meanDistances.append(mean)
        CVDistances.append(stdDev(trials) / mean)
    return (meanDistances, CVDistances)


def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('b-', 'r:', 'm-'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of ', dClass.__name__)
        means, CVS = simDrunk(numTrials, dClass, walkLengths)
        CVMean = sum(CVS) / float(len(CVS))
        pylab.plot(walkLengths, means, curStyle,
                   label=dClass.__name__ + '(CV =' + str(round(CVMean, 4)) + ')')

    pylab.title('Mean Distance from Origin (' + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc='best')
    pylab.semilogx()
    pylab.semilogy()


def getFinalLocs(numSteps, numTrials, dClass):
    """Function to run the similuation and keep track of final locations of Drunk"""
    locs = []
    d = dClass()
    origin = Location(0, 0)

    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, origin)
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
    return locs


def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('b+', 'r^', 'mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for l in locs:
            xVals.append(l.getX())
            yVals.append(l.getY())
        meanX = sum(xVals) / float(len(xVals))
        meanY = sum(yVals) / float(len(yVals))

        curStyle = styleChoice.nextStyle()
        print('Starting simulation of ', dClass.__name__)

        pylab.plot(xVals, yVals, curStyle, label=dClass.__name__ +
                   'Mean Loc. = <' + str(meanX) + ',' + str(meanY) + '>')

    pylab.title('Location at end of walks (' + str(numSteps) + ' steps)')
    pylab.xlabel('Number of Steps North/South')
    pylab.ylabel('Number of Steps East/West')
    pylab.legend(loc='lower left', numpoints=1)
    pylab.semilogx()
    pylab.semilogy()


# drunkTest([10, 25, 50, 100, 50, 1000, 5000, 10000], 100, UsualDrunk)
# drunkTest([0, 1], 1000, UsualDrunk)
# simAll([UsualDrunk, ColdDrunk, EWDrunk], [100,1000, 10000, 50000], 100)

plotLocs([UsualDrunk, ColdDrunk, EWDrunk], 100, 200)
