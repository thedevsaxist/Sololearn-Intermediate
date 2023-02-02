# To retrieve each line in a file, you can use the readlines() method

file = open("filename.txt")
for line in file.readlines():
    print(line)
file.close()

'---------------------------------------------------------'

# if you do not need the list for each line, you can simply iterate over the file variable
file = open("filename.txt")
for line in file:
    print(line)
file.close()

"""In the output, the lines are separated by blank lines, 
as the print function automatically adds a new line at the end of its output"""