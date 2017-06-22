"""
All of our items, meaning things the player can interact with, Will be stored here

"""

######### Weapon Code
class weapon():
    def __str__(self):
        return self.name

class rock(weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A small pebble like stone, More likely to cause an enemy to laugh at you than tremble."
        self.damage = 1


class dagger(weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small piece of metal has been inserted into a wooden handle. It's better than nothing."
        self.damage = 3



########## Gold (Coin, Money)
########## Coin is the currency our game will use. Each item will have a worth in Coin.
class coin():
    def __init(self):
        self.name = "A Coin"
        self.description = "A small, golden coin."
        self.worth = 1
        self.durability = 100
        self.weight = 0.1
