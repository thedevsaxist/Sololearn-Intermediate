# To write files, you use the write method

file = open("name.txt", "w")
file.write("This has been written to a file")
file.close()

"""This will create a new file called 'name.txt' and write the content to it.
In case te file already exists, its entire content wil be replaced when you open it in write mode using 'w'."""