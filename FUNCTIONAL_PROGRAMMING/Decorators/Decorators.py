def decor(func):
    def wrap():
        print("==============")
        func()
        print("==============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)  # The variable decorated is a decorated version of print_text
decorated()                    # -- it's print_text plus something

"""Now print_text corresponding to our decorated version"""
# print_text = decor(print_text)
# print_text()


"""We defined a function named decor that has a single parameter func.
inside the decor, we defined a nested function named wrap.
The wrap function will print a string, then call func(), and print another string.
The decor function returns the wrap function as its result."""