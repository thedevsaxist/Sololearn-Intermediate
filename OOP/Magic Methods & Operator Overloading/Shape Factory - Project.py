# We are improving our drawing application. 
# Our application needs to support adding and comparing two Shape objects.
# Add corresponding methods to enable addition + and comparison using the greater than > operator
# for the Shape class.


# Task:
"""The addition should return a new object with the sum of the widths and heights of the operands 
while the comparison should return the result of comparing the areas of the objects."""

# Explanation:
"""The given code creates two Shape objects from user input, outputs the area() of their addition and compares them."""

# Code:

class Shape:
    def __init__(self, w, h) -> None:
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __add__(self, otherShape):
        return Shape(self.width + otherShape.width, self.height + otherShape.height)

    def __gt__(self, other):
        return self.area() > other.area()

w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)