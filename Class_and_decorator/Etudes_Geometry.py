""" Etudes_geometry.py
Simple collection of geometric Classes. """

from math import pi, sqrt, atan
from typing import List, overload
import sys
#dirname = os.path.dirname(__file__)
#filename = os.path.join(dirname, 'relative/path/to/file/you/want')
#sys.path.insert(1, '~/documents/github/python-examples/Error_Handling')
#import error


class Pt():
    """Simple object to describe a point."""

    def __init__(self, loc_x: float, loc_y: float) -> None:
        self.x, self.y = loc_x, loc_y

    def move(self, delta_x: float, delta_y: float) -> None:
        """Move a point by distance dx and dy."""
        self.x += delta_x
        self.y += delta_y

    def __add__(self, pt2) -> Pt:
        new_x = self.x + pt2.x
        new_y = self.y + pt2.y
        return Pt(new_x, new_y)

    def __str__(self) -> str:
        # two ways to achieve same formating
        # return '({self.x}, {self.y})'.format(self=self)
        return '({0:.2f}, {1:.2f})'.format(self.x, self.y)


class Circle():
    """Simple object to describe a circle by reusing the point class.
       If no center is specified assume at origin"""

    def __init__(self, radius: float, point=Pt(0, 0)) -> None:
        self.radius, self.center = radius, point

    def area(self) -> float:
        """Calculate the areas of the circle."""
        return pi * self.radius ** 2

    def __add__(self, another_circle):
        return Circle(self.radius + another_circle.radius)

    def __gt__(self, another_circle) -> bool:
        return self.radius > another_circle.radius

    def __lt__(self, another_circle) -> bool:
        return self.radius < another_circle.radius

    def __str__(self) -> str:
        # two ways to achieve same formating
        # return 'Origin {self.center} and r = {self.r}'.format(self=self)
        return 'Origin({0:.2f}, {1:.2f}) and r = {2:.2f}'.format(self.center.x,
                                                                 self.center.y, self.radius)


class Line():
    """Simple object to describe a line using Pt class."""

    def __init__(self, pt1, pt2) -> None:
        self.point1, self.point2 = pt1, pt2

        x_dist = self.point2.x - self.point1.x
        y_dist = self.point2.y - self.point1.y
        self.mag = sqrt(x_dist**2 + y_dist**2)
        self.theta = atan(y_dist / x_dist) * 180 / pi

    def __add__(self, another_line):
        if self.point1 == another_line.point1:
            new_line = Line(self.point2, another_line.point2)
        elif self.point2 == another_line.point2:
            new_line = Line(self.point2, another_line.point2)
        else:
            new_line = None
        return new_line

    def __gt__(self, another_line) -> bool:
        return self.mag > another_line.mag

    def __lt__(self, another_line) -> bool:
        return self.mag < another_line.mag

    def __str__(self) -> str:

        return 'Line: {0} to {1} with Mag {2:.2f} at angle {3:.2f}'.format(self.point1,
                                                                           self.point2, self.mag, self.theta)


class Rectangle():
    """Simple object to describe a rectangle using Pt and line class.
       Point p1 is bottom left. From there you go counter clock wise.
       If not p1 specified, assume at origine
       Rectangle is assumed to be horizontal"""

    def __init__(self, width: float, height: float, p1=Pt(0, 0)) -> None:
        self.point1 = p1
        self.point2 = p1 + Pt(width, 0)
        self.point3 = self.point2 + Pt(0, height)
        self.point4 = p1 + Pt(height, 0)
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the Area."""
        return self.width * self.height

    def move(self, delta_x: float, delta_y: float):
        """Move by distance delta_x and delta_y."""
        distance = Pt(delta_x, delta_y)
        self.point1 = self.point1 + distance
        self.point2 = self.point2 + distance
        self.point3 = self.point3 + distance
        self.point4 = self.point4 + distance

    def __str__(self) -> str:
        return 'Bottom Left Corner: {0}, W = {1}, H = {2}, A = {3:.2f}'.format(
            self.point1, self.width, self.height, self.area())


class Triangle():
    """Simple object to describe a Triangle using Pt and line class.

       To define a unique triangle we need either
       1) The lengths of the three sides (SSS)
       2) The lengths of two sides and the measure of the angle between the sides (SAS)
       3) The measure of two angles and the length of the side between the angles (ASA)
       4) The measure of two angles and the length of a side not between the angles (AAS)

       Current implementation works for SSS.
       Assumes the left most corner is p1 = A
       Ignore pylint R0902 Too many instance attributes (default is no more than 7)
       """

    def __init__(self, seg1: float, seg2: float, seg3: float, p1=Pt(0, 0)) -> None:
        self.seg1 = seg1  # Assumed to be segment AB
        self.seg2 = seg2  # Assumed to be segment AC
        self.seg3 = seg3  # Assume to be segment BC

        # Find location of all 3 points. There are two solutions given square root. Pick positive
        self.pt_a = p1
        self.pt_b = p1 + Pt(0, seg1)                 # Make Seg1 vertical starting with A
        var_cy = (seg1**2 + seg2**2 - seg3**2) / (2.0 * seg1)
        var_cx = sqrt(seg2**2 - var_cy)
        # Equation was derived with A(0,0) need to move by actual location
        self.pt_c = Pt(var_cx + self.pt_a.x, var_cy + self.pt_a.y)
        # print(self.A,self.B,self.C)

        self.width = seg1
        self.height = 2.0 * self.area() / self.width

    def area(self) -> float:
        """Calculate the Area but 1st check triangle ineguality."""
        test1 = self.seg1 + self.seg2 <= self.seg3
        test2 = self.seg1 + self.seg3 <= self.seg2
        test3 = self.seg2 + self.seg3 <= self.seg1

        if (test1 or test2 or test3):  # if sum of any 2 sides is bigger than 3rd
            print('****Error - Triangle inequality failed. Not a triangle')
            #error.err('****Error - Triangle inequality failed. Not a triangle')
        else:
            perimeter = self.seg1 + self.seg2 + self.seg3
            s_var = perimeter / 2.0     # Semi perimeter
            area = sqrt(s_var * (s_var - self.seg1) * (s_var - self.seg2) * (s_var - self.seg3))
        return area

    def move(self, delta_x, delta_y) -> None:
        """Move by distance deltat_x and delta_y."""
        distance = Pt(delta_x, delta_y)
        self.pt_a = self.pt_a + distance
        self.pt_b = self.pt_b + distance
        self.pt_c = self.pt_c + distance

    def __str__(self) -> str:
        return '(S1, S2, S3) = ({0},{1},{2}) with Area = {3:.3f}'.format(self.seg1,
                                                                         self.seg2, self.seg3, self.area())


def test_points():
    """Test harness."""
    print("\nTesting points:")
    point_x = Pt(2.5, 5)
    point_x.move(2, 2)
    print(point_x, "\t=? (4.5,7)")
    point_y = point_x + point_x
    print(point_y, "\t=? (9,14)")


def test_lines():
    """Test harness."""
    print("\nTesting Lines:")
    point_x = Pt(0, 0)
    point_y = Pt(3, 4)
    point_z = Pt(5, 5)
    print("\nTesting lines:")
    line1 = Line(point_x, point_y)
    print(line1, " =? (0,0) and (3,4) with mag = 5.0")
    line2 = Line(point_x, point_z)
    print(line2, " =? (0,0) and (5,5) with mag = 7.0")
    line3 = line1 + line2
    print(line3, " =?  (3,4) and (5,5) and with mag = 2.2")
    print("Is line1 < line2?", (line1 < line2))


def test_circle():
    """Test harness."""
    print("\nTesting circles:")

    point_y = Pt(3, 4)
    circle1 = Circle(3)
    circle2 = Circle(1, point_y)
    print(f"c1 = {circle1} of area = {circle1.area():.3f}")
    print(f"c2 = {circle2} of area = {circle2.area():.3f}")
    print("Is c1 < c2?", (circle1 < circle2))


def test_rectangles():
    """Test harness."""
    print("\nTesting rectangles:")
    point_x = Pt(1, 0)
    rect = Rectangle(5.1, 10, point_x)
    print('Rectangle: ', rect)
    rect.move(2.2, 3)
    print('Moved rectangle: ', rect)
    rect2 = Rectangle(10.12, 12)
    print('Rectangle at origin: ', rect2)


def test_triangles():
    """Test harness."""
    print("\nTesting triangles:")
    tri = Triangle(3, 4, 5)
    print(f"Triangle: {tri}")
    print(f"Width {tri.width:.3f} and height {tri.height:.3f}")
    print(f"Corners => ({tri.pt_a}{tri.pt_b}{tri.pt_c})")

    tri2 = Triangle(7, 7, 7)
    print(f"\nTriangle: {tri2}")
    print(f"Width {tri2.width:.3f} and height {tri2.height:.3f}")
    print(f"Corners => ({tri2.pt_a}{tri2.pt_b}{tri2.pt_c})")

    point_x = Pt(1, 3)
    tri3 = Triangle(3, 4, 5, point_x)
    print(f"\nTriangle: {tri3}")
    print(f"Width {tri3.width:.3f} and height {tri3.height:.3f}")
    print(f"Corners => ({tri3.pt_a}{tri3.pt_b}{tri3.pt_c}")

    #t = Triangle(3, 2, 5)
    # print( 'Triangle: {}'.format(t) )  # This should fail
    tri.move(2, 3)
    print('\nMove original triangle by (2,3)')
    print(f"Triangle: {tri}")
    print(f"Width {tri.width:.3f} and height {tri.height:.3f}")
    print(f"Corners => ({tri.pt_a}{tri.pt_b}{tri.pt_c})")


test_points()
test_circle()
test_lines()
test_rectangles()
test_triangles()
