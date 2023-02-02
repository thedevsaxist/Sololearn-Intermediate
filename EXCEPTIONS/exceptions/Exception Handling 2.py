# A try statement can have multiple different except blocks to handle different exceptions.
# Multiple exceptions can aso be put into a single except block using the parentheses, to have the except block handle all of them.

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")


# you can handle as many exceptions in the except statement as you need.