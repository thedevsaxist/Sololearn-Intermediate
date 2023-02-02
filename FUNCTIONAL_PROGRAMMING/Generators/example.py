# Finite generators can be converted into lists by passing them as arguments to the list function.

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))


