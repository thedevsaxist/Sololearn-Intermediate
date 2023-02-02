pairs = {
    1: 'apple',
    "orange": [2, 3, 4],
    True: False,
    12: "True",
}

print(pairs.get("orange"))  # the print() followed by the variable name.get() then the key, alternate value.
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))  # The second specified value is returned only if the first value is not recognised
print(pairs.get(False, "here"))
print(pairs.get(1, "oppo"))