# Given a string as input, 
# you need to output how many times each letter appears in the string.
# You decide to store the data in a dictionary,
# with the letters as the keys, and the corresponding counts as the values.
# Create a program to take a string as input and output a dictionary, 
# which represents the letter count.

"""
Sample Input
hello

Sample Output
{'h':1, 'e':1, 'l':2, 'o':1}
"""

# You need to output the dictionary object.
# Note, that the letters are in the order of appearance in the string.

text = input("Enter String here: ")
after = list(text)
empty = []

for each_letter in text:
    new = text.count(each_letter)
    empty.append(new)
    
print(dict(zip(after, empty)))


"""This is using the lambda function"""
# text = input("Enter String here: ")
# after = list(text)

# result = list(map(lambda x: text.count(x), after))
# print(dict(zip(after, result)))