# You need to make a function called calc(), that will take the side length of a square as its argument
# and return the perimeter and area using a tuple.
# The perimeter is the sum of all sides, while the area is the square of the side length.

# The given code takes a number from the user input, passes it to the calc() function,
# and uses unpacking to get the returned values.

def calc(x):
    p = x*4
    a = x**2
    return p, a
    
    
side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))