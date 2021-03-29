import turtle


class Polygon:
    def __init__(
        self,
        sides: int,
        name: str,
        size: int = 100,
        color: str = "black",
        line_thickness: int = 3,
    ):
        """ Initialize. """
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides - 2) * 180
        self.angle = self.interior_angles / self.sides

    def draw(self):
        """ Draw the Polygone. """
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)


class Square(Polygon):
    def __init__(self, size: int = 100, color: str = "black", line_thickness: int = 3):
        super().__init__(4, "Square", size, color, line_thickness)

    def draw(self):
        """ Overide method and fill the square. """
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()


if __name__ == "__main__":
    square = Square(size=300, color="#abcdef")
    square.draw()
    turtle.done()  # Necessary to see the fill
