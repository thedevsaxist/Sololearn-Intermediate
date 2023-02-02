# Take the number N as input and write the numbers 1 to N to the file "numbers.txt",
# each number on a separate line

"""
Sample Input:
4

Sample Output:
1
2
3
4
"""

# Code:

# The given code reads the content of the file and outputs it

n = int(input())
file = open("numbers.txt", "w+")
for num in range(1, n+1):
    file.write(f'{str(num)}\n')
    print(num)

f = open("numbers.txt", "r")
print(f.read())
f.close()