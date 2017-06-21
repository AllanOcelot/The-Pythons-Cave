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


#Let's instigate all of our variables here

#Name
playerName = "Allan the fearless warrior"

#Players Position X  = Horizontal position of player
playerX = 0

#Players Postion Y = Vertical position of player
playerY = 0

#Player Position Z = Z (Layer , think, up, down,) positon of player. Used when going upstairs, downstairs in buildings etc.
playerZ = 0







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






""" Build the player class """
class player():
    name = getPlayerName()
    posX = getPlayerX()
    posY = getPlayerY()
    posZ = getPlayerZ()


