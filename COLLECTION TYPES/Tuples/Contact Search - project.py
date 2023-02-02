# You are given a list of contacts, where each contact is represented by a tuple,
# with the name and age of the contact.

# Complete the program to get a string as input, search for the name in the list
# of contacts and output the age of the contact in the format presented below:

"""
Sample Input
  John

Sample Ouput
  John is 31
"""
# If the contact is not found, the program should output "Not found"

# Start
contacts = [
    #('name', age)
    ('James', 42),  # this is an example of "x"
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18) 
]

name = input()  
for x in contacts:  
    if name in x: 
        print(
            str(
                x[0] + " is " + str(x[1])
            )
        )
        break
    else:
        print("Not found")
# Stop



"""
Detailed explanation of the code above:

name = input()  >> This takes the name of the contact to be searched.
for x in contacts:  >> The loop name "x" here serves as the name of the tuple and a link between the "name" of the contact inputed and "contact"
                    >> The loop iterates through "contacts" to find "x".

    if name in x:  >> This iterates through "x" to find "name".
        print(
            str(

         name in the tuple       age in the tuple
                 ^                    ^
               x[0] + " is "  +  str(x[1])
            )
        )
        break >> this stops the loop
    else:
        print("Not found")
"""