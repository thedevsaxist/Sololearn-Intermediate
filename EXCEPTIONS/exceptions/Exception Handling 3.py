# An except statement without any exception specified will catch all errors.
# These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.

try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")


"""Exception handling is particularly useful when dealing with user input"""