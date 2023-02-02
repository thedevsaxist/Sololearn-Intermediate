class Wolf:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark()

"""In the example above, Wolf is the superclass, Dog is the subclass"""