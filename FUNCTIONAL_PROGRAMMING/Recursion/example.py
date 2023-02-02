def power(x: int, y: int):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)
        # this returns 2 * (2, 3 - 1)

print(power(2, 3))