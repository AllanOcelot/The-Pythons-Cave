"""
 We will create and use all of our world tiles here.
 It's important to note that one tile is 32X32 (So we can draw them as graphics at a later date)
 You can have multiple "tiles" in a "Room" (collection of tiles)
 You can have multiple "Rooms" in a "Map" (collection of Rooms together).
"""






### Declare the different types of tiles here
class tile_type():
    def __init__(self):
        self.name = "Example tile Type"
        self.texture = "none"
        self.sound = "none"
        self.description = "An example tile you should not be seeing this"
        self.passable = True

class tile_soil(tile_type):
    def __init__(self):
        self.name = "Soil"
        self.description = "A flat piece of earth."
        self.passable = True


#Build the tile type, we will pass this into a map maker/viewer at a later date to build the world
class tile():
    def __init__(self):
        self.posX = 0; #Horizontal
        self.posY = 0; #Vertical
        self.posZ = 0; #Layer
        self.type = 0; #Link to a type - containing a description and graphic , sound etc

