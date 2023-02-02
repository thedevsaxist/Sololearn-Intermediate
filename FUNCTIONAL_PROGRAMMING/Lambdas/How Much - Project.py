# You are given code that should calculate the corresponding percentage of a price.
# Somebody wrote a lambda function to accomplish that, however the lambda is wrong.
# Fix the code to output the given percentage of the price.

"""
Sample Input
50
10

Sample Output
5.0
"""
# The first input is the price, while the second input is the percentage we need to calculate: 10% of 50 is 5.0

"""This is using a named function"""
# price = int(input("Enter price here: "))
# per = int(input("Enter percentage here: "))
# def percentage(price, per):
#     return per/100 * price
# print(percentage(price, per))

"""Lambda function"""
price = int(input("Enter price here: "))
per = int(input("Enter percentage here: "))
print((lambda x, y: y/100 * x) (price, per))