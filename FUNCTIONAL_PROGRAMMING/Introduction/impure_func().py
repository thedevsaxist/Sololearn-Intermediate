some_list = ["this", "that", "they", "them"]

def impure(arg):
    some_list.append(arg)
# the function above is not pure because it changed the state of some_list.

print(impure("thy"))

