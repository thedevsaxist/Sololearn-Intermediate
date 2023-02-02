def silly_generator():
    yield "Python"
    yield "Rocks"
    yield "So do you!"

gen = silly_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(type(gen))
print(next(gen))  # this final call raises an error because it exhausts the limits of the generator

"""The yield keyword can be used more than once in a generator.
But, if you call it more times than it was used in the generator, it will raise a 'StopIteration' error"""