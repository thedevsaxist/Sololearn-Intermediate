"""
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