# To read only a certain amount of a file, you can provide the number of byte to read as the argument to the read function.

file = open("filename.txt")
print(file.read(5))  # This will read the firs five characters of the file
print(file.read(7))  # then this will read the next seven
print(file.read())
file.close()

"""Calling the read() method without an argument will return te rest of te file content"""