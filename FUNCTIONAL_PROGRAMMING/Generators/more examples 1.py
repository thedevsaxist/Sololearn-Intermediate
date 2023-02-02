def doubler_generator():
    number = 2
    while True:
        yield number
        number *= number
doubler = doubler_generator()
print(next(doubler))
print(next(doubler))
print(next(doubler))
print(type(doubler))
