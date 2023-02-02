# The given code takes 2 numbers as input and calls the static area() method of the Shape class,
# to output the area of the shape, which is equal to the height being multiplied by the width.
# To make the code work, you need to define the Shape class, and the static area() method, 
# which should return the multiplication o fits two arguments.

# Use the @staticmethod decorator to define a static method

# Code:
class Shape:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    @staticmethod
    def area(height, width):
        return height * width

w = int(input("Width = "))
h = int(input("Height = "))

print(Shape.area(h, w))