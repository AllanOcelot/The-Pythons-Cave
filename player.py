"""
   Welcome to the player class file.
   In this file we will create the 'Player' class.
   Really, it's just an object, since a class implies we will reuse the code time and time again for other 'players'.
   But this game just has one player.

   I'm waffling again.

   The player will be accessed by our game everywhere, or globally.
   To make sure that we don't set values where we don't want them
   we will use 'Getters' and 'Setters'

"""

import items


#Let's instigate all of our variables here

#Name
playerName = "Allan the fearless warrior"

#Players Position X  = Horizontal position of player
playerX = 0

#Players Postion Y = Vertical position of player
playerY = 0

#Player Position Z = Z (Layer , think, up, down,) position of player. Used when going upstairs, downstairs in buildings etc.
playerZ = 0

#Create the player's inventory
inventory = {"One large sword" , "An empty coin purse", "Despair!"}

#Player health , max health is 100, but we will limit this in our 'Setter' function
health = 100
alive = True





#GETTERS AND SETTERS
def setPlayerName(newName):
    playerName = newName
def getPlayerName():
    return playerName



def setPlayerX(newX):
    playerX = newX
def getPlayerX():
    return playerX

def setPlayerY(newY):
    playerY = newY
def getPlayerY():
    return playerY

def setPlayerZ(newZ):
    playerZ = newZ
def getPlayerZ():
    return playerZ


def setPlayerHealth(healthInput):
    if(healthInput > 100):
        health = 100
    else:
        health = healthInput

    if(healthInput == 0):
        health = 0
        alive = False

def getPlayerHealth():
    return health

####################
###
####################



""" Build the player class """
class player():
    def __init__(self, name, health, playerPosX, playerPosY , playerPosZ ):
        self.name = name
        self.health = health
        self.posX = playerPosX
        self.posY = playerPosY
        self.posZ = playerPosZ
        self.inventory = {items.rock(), items.dagger()}


    def getPlayerInventory(self):
        index = 0

        #The String we return
        results = ""

        if(len(self.inventory) < 2):
            results += "You don't seem to be carrying too much, only..."
        if(len(self.inventory) > 2):
            results += "You are carrying a few things in your pockets... \n"


        for item in self.inventory:
            results += str(index) + " " + str(item) + "  \n"
            index = index + 1

        return results
