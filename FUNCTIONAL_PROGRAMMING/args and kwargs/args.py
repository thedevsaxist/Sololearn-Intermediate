"""Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function."""

def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)


# The parameter *args must come after the named parameter to a function.
# The name args is just a convention; you can choose to use another