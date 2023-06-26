# Create a Python class called Rectangle that represents a rectangle. The class should have the following properties:

# width: the width of the rectangle (a float or integer)
# height: the height of the rectangle (a float or integer)

# The class should also have the following methods:

# area(): calculates the area of the rectangle and returns it as a float.
# perimeter(): calculates the perimeter of the rectangle and returns it as a float.
# scale(n): scales the rectangle by a factor of n. The width and height of the rectangle should be multiplied by n.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        prei = 2*(self.height + self.width)
        return prei

    def scale(self, n):
        self.height *= n
        self.width *= n


shape = Rectangle(300, 20)
print(shape.area())
print(shape.perimeter())
