"""You are working at a car dealership and store the car data in a dictionary.
Your program needs to take the key as input and output the corresponding value."""

# this is the dictionary we are working with
car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

# this is a search() we defined to iterate through the dictionary
z = input()
def search(z):
    if z in car:
        return car[z]

print(search(z))

"""
likewise, this line of code does the same thing
z = input()
print(car.get(z))
"""

"""
likewise, this line of code does the same thing
key = input()
if key in variable:
    print(variable[key])
"""