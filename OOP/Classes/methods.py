"""Classes can have other methods defined to add functionality to them."""

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

# Class attributes are shared by all instances of the class