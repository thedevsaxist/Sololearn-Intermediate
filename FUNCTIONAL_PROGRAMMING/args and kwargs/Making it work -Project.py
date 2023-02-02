"""The given code defines a function called my_min(), which takes two arguments and returns the smaller one
You need to improve the function, so that it can take any number of variables, so that the function call works"""

def my_min(*args):
    return min(args)
    
print(my_min(8, 13, 4, 42, 120, 7))
