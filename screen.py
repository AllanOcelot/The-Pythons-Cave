"""
We create the class screen, we will use Pygame to display our information on the screen's etc
We will reuse this code to create title screens, maps etc
"""


#Import PyGame
import pygame, sys

#Import everything we need from Pygame
from pygame.locals import *

# Init Pygame
pygame.init()


class screen():
    def __init__(self , title, width, height):
        self.title = title

        #create our screen
        canvas = pygame.display.set_mode((width, height))

        #We will draw a square on screen
        pygame.draw.rect(canvas, (0,255,0) , (10,10,10,10))

        #Set our title
        pygame.display.set_caption(self.title)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update();
