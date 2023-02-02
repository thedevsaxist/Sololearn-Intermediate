# You are given a file named "books.txt" with book titles, each on a separate line.
# To encode the book titles you need to take the first letters of each word in the title and combine them.
# For example, for the book title "Game of Thrones" the encoded version should be "GoT"

# Complete the program to read te book title from te file and Output the encoded versions,
# each on a new line

# Code:


with open("books.txt") as f:
    for line in f:
        text = line.split()
        q = [line[0] for line in text]
        print("".join(q))