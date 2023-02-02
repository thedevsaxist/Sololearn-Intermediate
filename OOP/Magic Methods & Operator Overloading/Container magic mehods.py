import random

class VagueList:
    def __init__(self, cont) -> None:
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont) * 2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])


"""We have overridden the len() function for the class VagueList to return a random number.
The indexing function also returns a random item in a range from the list, based on the expression."""