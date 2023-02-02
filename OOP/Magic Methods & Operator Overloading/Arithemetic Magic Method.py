class SpecialString:
    def __init__(self, cont) -> None:
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello World!")
print(spam / hello)


"""In the operation above, we defined the division operator for ou class Special"""