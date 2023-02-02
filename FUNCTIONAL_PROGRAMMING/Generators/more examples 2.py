def silly_generator():
    yield "Python"
    yield "Rocks"
    yield "So do you!"

gen = silly_generator()
for items in gen:
    print(items)

""" Running the generator inside of a for loop will help when the generator is exhausted"""