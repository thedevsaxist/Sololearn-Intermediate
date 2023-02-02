# Class methods are marked with a classmethod decorator

class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        """New square is a class method and is called on the class, rather than an instance of the class.
        It returns a new objects of the class cls."""
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())


# Technically, the parameters self and cls are just conventions; they could be changed to anything else.
# However, they are universally followed, so it is wise to stick to using them.