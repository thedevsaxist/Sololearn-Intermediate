# Weakly private methods and attributes have a single underscore at the beginning.
# This signals that they are private, and shouldn't be used by external code.
# However, it is mostly only a convention, and does not stop external code from accessing them.

class Queue:
    def __init__(self, contents) -> None:
        self._hiddenList = list(contents)

    def push(self, value):
        self._hiddenList.insert(0, value)

    def pop(self):
        return self._hiddenList.pop(-1)

    def __repr__(self) -> str:
        return "Queue({})".format(self._hiddenList)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenList)

"""In the code above, the attribute _hiddenList is marked as private, but it can still be accessed in the outside code.
The __repr__ magic method is used for string representation of the instance"""