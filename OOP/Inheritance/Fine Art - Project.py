"""You are making a drawing application, which has a Shape base class.
The given code defines a Rectangle class, creates a Rectangle object and calls its area() and perimeter() methods"""

"""Do the following to complete the program:
1. Inherit the Rectangle class from Shape
2. Define the perimeter() method in the Rectangle class, printing the perimeter of the rectangle
"""

# The perimeter is equal to 2*(width + height)

class Shape:
    def __init__(self, w, h) -> None:
        self.width = w
        self.height = h

    def area(self):
        print(self.width*self.height)

class Rectangle(Shape):
    def perimeter(self):
        print(2 * (self.width + self.height))
        


w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()