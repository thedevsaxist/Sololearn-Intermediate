# Strongly private methods and attributes have a double underscore at the beginning of their names.
# This causes their names to be mangled, which means that they can't be accessed from outside the class.
# The purpose of this isn't to ensure that they are kept private, but to avoid bugs if there are subclasses
# that have methods or attributes with the same names.
# Name mangled methods can still be accessed externally, but by a different name. The method __privatemethod of class Spam
# could be accessed externally with _Spam__privatemethod.

class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)  # type: ignore

"""This will raise an error because the __egg attribute has a double underscore preceding it
which makes it private and unaccessible"""
print(s.__egg)

"""Basically, Python projects those members by internally changing the name to include the class name"""