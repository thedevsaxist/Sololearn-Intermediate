# To handle exceptions, and to call code when an exception occurs,
# you can use a try/except statement.

# The try block contains code that might throw an exception. 
# If that exception occurs, the code in the try block stops being executed, and the code in the except block is run.
# If no error occurs, the code in the except block doesn't run.

try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

"""In the code above, the except statement defines the type of exception to handle (in our case, the ZeroDivisionError)"""