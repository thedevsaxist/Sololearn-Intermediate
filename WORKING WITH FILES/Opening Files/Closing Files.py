# Once a file has been opened and used, you should close it.
# This is done with the close method of the file object

file = open("filename.txt", "w")
# do stuff to the file
file.close()