# An ATM machine takes the amount to be withdrawn as input and calls the corresponding withdrawal method.
# In case the input is not a number, the machine should output "Please enter a number".

# Task
"""Use exception handling to take a number as input, call the withdraw() method with the input as its argument, 
and output "Please enter a number", in case the input is not a number."""

# Tip:
"""A ValueError is raised when you try to convert a non-integer to an integer using int()."""

# My Code:
def withdraw(amount):
    print(str(amount) + " withdraw")
x = input()
try:
    if int(x):
        withdraw(x)
except (ValueError, TypeError):
    print("Please enter a number")