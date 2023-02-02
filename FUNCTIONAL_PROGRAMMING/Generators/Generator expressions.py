"""Generator expressions are another way of creating generators. 
This way is similar to a list comprehension, except that it returns generators"""

gen = (x ** 2 for x in range(5))
print(next(gen))
print(next(gen))
print(list(gen))

