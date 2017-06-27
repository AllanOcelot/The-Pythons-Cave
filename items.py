"""
All of our items, meaning things the player can interact with, Will be stored here

"""

######### Weapon Code
class weapon():

    def __init__(self):
        self.image_source = ""

    def __str__(self):
        return self.name

class rock(weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A small pebble like stone, More likely to cause an enemy to laugh at you than tremble."
        self.damage = 1
        self.image_source = "rock.png"

class dagger(weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small piece of metal has been inserted into a wooden handle. It's better than nothing."
        self.damage = 3
        self.image_source = "dagger1.png"

class sword(weapon):
    def __init__(self):
        self.name = "Sword"
        self.description = "A small Sword, be careful with this thing!"
        self.damage = 5
        self.image_source = "sword1.png"

class bow(weapon):
    def __init__(self):
        self.name = "Bow"
        self.accuracy = 25.5
        self.description = "It's a very simple bow, not good for much!"
        self.damage = 4
        self.image_source = "bow1.png"



########## Gold (Coin, Money)
########## Coin is the currency our game will use. Each item will have a worth in Coin.
class coin():
    def __init__(self):
        self.name = "A Coin"
        self.description = "A small, golden coin."
        self.worth = 1
        self.durability = 100
        self.weight = 0.1
