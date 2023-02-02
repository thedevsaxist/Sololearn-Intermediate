"""The keyword argument returns a dictionary in which the keys are the argument names, 
and the values are the argument values"""

def my_func(x, y = 7, *args, **kwargs):
    print(kwargs)
    print(args)
    print(x)
    print(y)

my_func(2, 3, 4, 5, 6, a = 7, b = 8)


# a and b ae the names of the arguments that we passed to the function call
# The arguments returned by **kwargs are not included in *args.