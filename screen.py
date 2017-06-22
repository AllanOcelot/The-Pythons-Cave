"""
We create the class screen, we will use Pygame to display our information on the screen's etc
We will reuse this code to create title screens, maps etc
"""


#Import PyGame
import pygame, sys
import example_map

#Import everything we need from Pygame
from pygame.locals import *

# Init Pygame
pygame.init()

#We would normally load in a map
currentLevel = example_map.map()


class screen():


    def drawMap(self , surfaceToDrawTo):
        print(currentLevel.title)

        #We are going to fine out how 'wide' the map is
        mapWidth = len(currentLevel.mapArray) / 2

        print("The map should be " +  str(mapWidth) + " wide")

        indexX = 0;
        indexY = 0;

        #We will loop over our map here - and paint a block getting the details from the array such as type, texture etc
        for item in currentLevel.mapArray:
            pygame.draw.rect(surfaceToDrawTo, (0, 255, 0), (indexX * 32, indexY * 32, 32, 32))
            indexX = indexX + 1
            if indexX == mapWidth:
                indexX = 0
                indexY = indexY + 1



    def __init__(self , title, width, height):
        self.title = title

        # create our screen
        self.canvas = pygame.display.set_mode((width, height))

        #Set our title
        pygame.display.set_caption(self.title)



        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()



            self.drawMap(self.canvas)
            pygame.display.update();
