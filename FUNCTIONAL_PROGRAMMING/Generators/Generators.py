def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

"""The yield statement is used to define a generator,
replacing the return of a function to provide a result to its caller without destroying local variables."""