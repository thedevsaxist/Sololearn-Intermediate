"""An example of recursion is the factorial function, 
which finds the product of all positive integers below a specified number.
For example, 5!(5 factorial) is 5*4*3*2*1 (120).
To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, and so on.
Generally, n! = n * (n-1)!. Furthermore, 1! = 1. This is known as the base case, as it can be calculated 
without performing any more factorials."""


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))

# The base case acts as the exit condition of the recursion. 
# Not adding a base case results in infinite function calls, crashing the program.