def add_five(x: int):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result) 

""" We could have achieved the same result more easily by using lambda syntax """

nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x + 5, nums))
print(result)

# To convert the result to a list, we used the list explicitly

