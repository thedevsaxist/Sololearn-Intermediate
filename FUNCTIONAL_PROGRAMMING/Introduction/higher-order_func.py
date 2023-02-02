"""
This is an example of a Higher-order function
"""

def apply_twice(func, arg):  # this is a function that takes another function as its argument.
    return func(func(arg))  # this makes it call the function twice.

def add_five(x):  # this is the function that the apply_twice() takes as its argument.
    return x + 5  # this is the body of this function which has an argument x and adds 5 to it.

print(apply_twice(add_five, 10))  # this calls the apply_twice() which has the add_five() and 10 as its arguments.

# The function apply_twice takes another function as its argument, and calls it twice inside its body.
