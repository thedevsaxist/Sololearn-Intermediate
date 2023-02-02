# An alternative way of doing this is by using the with statement

with open("filename.txt") as f:
    print(f.read())

# the file is automatically closed after the with statement, even if exceptions occur within it