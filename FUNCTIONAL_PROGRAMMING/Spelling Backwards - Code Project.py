"""Given a string as input, use recursion to output each letter of the string in reverse order,
on a new line"""

"""
Sample Input
HELLO

Sample output
O
L
L
E
H
"""

# Complete the spell() function to produce the expected result

def spell(txt):
    for x in txt:
        print(x)

txt = input()[::-1]
spell(txt)