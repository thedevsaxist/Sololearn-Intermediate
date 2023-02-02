# The given code defines a function, isPrime(x), which returns True if x is prime.
# You need to create a generator function primeGenerator, that will take two numbers as arguments, 
# and use the isPrime() function to output the prime numbers in the given range (between the two arguments).

"""
Sample Input
10
20

Sample Output
[11, 13, 17, 19]
"""
# The given code takes the two arguments as input and passes them to the generator function, 
# outputting the result as a list

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


def primeGenerator(a, b):
    for all in range(a, b):
        if isPrime(all):
            yield all

f = int(input("Start: "))
t = int(input("End: "))

print(list(primeGenerator(f, t)))