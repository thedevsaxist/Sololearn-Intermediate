# This is a simple example of using a method, classmethod, and staticmethod

"""
Variables used in this example:
class: Human
objects: h1 and h2
"""

"""
Methods defined inside the class:
method: desc(self)
        --> A method to introduce himself by telling us what his name is.

static: say_hello()
        --> A method to say 'Hello'

classm: create_human(cls, name)
        --> A customized constructor to verify if name is a string before creating the object or instance
"""

# Code:
 
class Human:
    def __init__(self, name):
        self.name = name

    def desc(self):  # We need the parameter 'self' to access the specific attribute and methods of the object
        """The function inside the class has 'self' as its first parameter which represents the object itself"""
        print(f"My name is {self.name}")

    @staticmethod
    def say_hello():  # Here we only need to print 'Hello!' to the screen which does not need any attribute... just 'Hello!'.
        """staticmethod means it always has the same functionality because it does not depend on the object attributes"""
        print("Hello!")

    @classmethod
    def create_human(cls, name):
        """"The purpose of this specific implementation is to verify first if the name is valid 
        before creating that particular Human or object"""
        if type(name) == str:
            return cls(name)
        else:
            print("Invalid Name!")


# Create a Human object 'h1' and pass "John" as its argument or 'name'
# You can do it like this:
# h = Human("John")
# But for the sake of this example, we will use the classmethod to verify first if the name is a string
print("CODE: h1 = Human.create_human('John')")
h1 = Human.create_human("John")

# 3.1416 is not a string or an invalid name, fortunately the classmethod can handle this type of situation
print("\n\nCODE: h2 = Human.create_human(3.1416)")
h2 = Human.create_human(3.1416)

# Call the desc() method using the object 'h1'. By using the object to call the method, the 'self' is already passed
print("\n\nCODE: h1.desc()")
h1.desc()

# h1.desc() is similar to this code. We passed the h1 as the 'self' to the Human.desc() method.
print("\n\nCODE: Human.desc(h1)")
Human.desc(h1) # type: ignore

# Call the staticmethod say_hello() using the object 'h1'
print("\n\nCODE: h1.say_hello()")
h1.say_hello()

# Call the staticmethod say_hello using the Human class itself.
# We don't need the object argument because we only need to say hello and that does not require any object or attribute
print("\n\nCODE: Human.say_hello()")
Human.say_hello()


"""As you can see, cls represents the class itself. 
Hence, 'cls(name)' is the same with 'Human(name)' where name is John in this example.
Then it will call the __init__ method to create the instance and its attributes.
Finally, it will return that created instance to the variable 'h1'
"""