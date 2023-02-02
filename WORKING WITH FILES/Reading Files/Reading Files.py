# The contents of a file that has been opened in text mode can be read using the read method.

file = open("Note.txt")
cont = file.read()
print(cont)
file.close()

"""This wil print all the content of the file"""