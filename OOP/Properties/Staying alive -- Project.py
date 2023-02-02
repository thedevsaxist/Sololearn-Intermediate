# We are improving our game and need to add an isAlive property, which returns True if the lives count is greater than 0.
# Complete the code by adding the isAlive property

# Hint:
"""The code uses a while loo[ to hit the Player, until its lives count becomes 0, 
using the isAlive property to make the condition"""

# Code:

class Player:
    def __init__(self,name, live) -> None:
        self.name = name
        self._lives = live

    def hit(self):
        self._lives -= 1

    @property
    def isAlive(self):
        if self._lives > 0:
            return True

p = Player("Cyberpunk77", int(input()))
i = 1
while True:
    p.hit()
    print("Hit # " + str(i))
    if not p.isAlive:
        print("Game Over")
        break