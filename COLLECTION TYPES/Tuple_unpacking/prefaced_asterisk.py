a, b, *c, d = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a)
print(b)
print(c)
print(d)
# for context sake and for further explanation
print(type(c))
print(type(d))
# c will be assigned the values 3 to 8. It is not assigned 3 to 9 because there is another variable after it.
# c is a list not a tuple