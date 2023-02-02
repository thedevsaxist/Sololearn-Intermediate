msg = "Hello World"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

"""The code above will write to the file and print the number of bytes written"""