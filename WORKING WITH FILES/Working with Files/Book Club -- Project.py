# You are given a "books.txt" file, which includes book titles, each on a separate line.

# Task:
"""Create a program to output how many words each title contains, in the following format:
Line 1: 3 words
Line 2: 5 words"""


# Code:

with open("books.txt") as f:
    j = 1
    for line in f:
        print(f'Line {str(j)}: {str(len(line.split(" ")))} words')
        j += 1