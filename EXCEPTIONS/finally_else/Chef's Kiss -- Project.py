# You are making a digital menu to order food.
# The menu is stored as a list of items.

# Task:
"""Your program needs to take the index of the item as input and output the item name.
Incase the index os not valid, you should output 'Item not found'.
In case the item name is valid and the item name is output successfully, you should output 'Thanks for your order'"""

"""
Sample Input:
2

Sample Output:
Cheeseburger
Thanks for your order
"""

# Tip:
"""Handle the cases when the input is out of range, as well as when it is not a number"""

# Code:

menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

try:
    menu_index = int(input("Order's Up!\n"))
    print(menu[menu_index])
    print("Thanks for your order")
except:
    print("Item not found")