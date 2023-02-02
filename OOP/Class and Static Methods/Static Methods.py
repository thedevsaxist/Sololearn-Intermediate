# Static methods are marked with a staticmethod decorator.

class Pizza:
    def __init__(self, toppings) -> None:
        self.toppings = toppings

    @staticmethod
    def validate_toppings(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_toppings(i) for i in ingredients):
    """The all() returns if al the items of an iterable fit a condition"""
    pizza = Pizza(ingredients)

# Static methods behave like plain functions, 
# except from the fact that you can call them from an instance of a class