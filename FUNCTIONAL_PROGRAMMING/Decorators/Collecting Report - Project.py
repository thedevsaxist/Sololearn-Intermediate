# You are working on an invoice system.
# The system has an already defined invoice() function, 
# which takes the invoice number as argument and outputs it

# You need to add a decorator for the invoice() function, that will print the invoice in the following format:

"""
Sample Input
42

Sample Output
***
INVOICE #42
***
END OF PAGE
"""

# The given code takes the invoice number as input and passes it to the invoice() function.

def decor(func):
    def wrap(man):
        print("***")
        func(man)
        print("***")
        print("END OF PAGE")
    return wrap

@decor
def invoice(num):
    print("INVOICE #" + str(num))

invoice(input("Enter invoice number here: "))