# You can throw (or raise) exceptions when some conditions occur.
# This is done using the raise statement.

num = 102
if num > 100:
    raise ValueError


"""You need to specify the type of exception raised."""

'---------------------------------------------------------------------------------'

# Exceptions can be raised with arguments that give detail about them.
name = "123"
raise NameError("Invalid name!")

"""This makes it easier for other developers to understand why you raised the exception"""