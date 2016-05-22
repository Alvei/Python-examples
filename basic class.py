class Car(object):

    def __init__(self, typ, make, model, color, year, miles):
        self.typ = typ
        self.make = make
        self.model = model
        self.color = color.lower()
        self.year = year
        self.miles = miles

    def __str__(self):
        print('Vehicle Type: ' + str(self.typ))
        print('Make: ' + str(self.make))
        print('Model: ' + str(self.model))
        print('Year: ' + str(self.year))
        print('Miles: ' + str(self.miles))
        return ''  # I can avoid getting an error if I un-comment this line

bmw = Car('SUV', 'BMW', 'X5', 'silver', 2003, 12030)
print bmw




class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"
        self.color = "Color not defined"

    def __str__(self):
        print ('Shape with sides: ' + str(self.x) + ' and ' + str(self.y))
        return ''   # __str__ needs a return
               
    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def colorName(self, text):
        self.color = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale

class Square(Shape):
    def __init__(self,x):
        self.x = x
        self.y = x
    


smallSquare = Square(10)

print smallSquare


# The shape looks like this:
# _________
#|    |    |
#|    |    |
#|____|____|
 
class DoubleSquare(Square):
    def __init__(self,y):
        self.x = 2 * y
        self.y = y
    def perimeter(self):
        return 2 * self.x + 2 * self.y


dictionary = {}
 
# Then, create some instances of classes in the dictionary:
dictionary["DoubleSquare 1"] = DoubleSquare(5)
dictionary["long rectangle"] = Shape(600,45)
 
#You can now use them like a normal class:
print "long rectangle area", dictionary["long rectangle"].area()
 
dictionary["DoubleSquare 1"].authorName("The Gingerbread Man")
print dictionary["DoubleSquare 1"].author   

