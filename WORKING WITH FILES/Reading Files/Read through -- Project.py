# You need to make a program to read the given number of characters of a file.
# Take a number N as input and output the first N characters of the books.txt file

"""The given code opens the books.txt. Use the file object to read the content of the file"""

# Code:
N = int(input())
file = open('filename.txt')
print(file.read(N))
file.close()