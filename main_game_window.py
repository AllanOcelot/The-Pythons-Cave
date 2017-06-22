"""
    This is our main game window.
    It houses all of the displays for our game and handles the keyboard events.
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


#Get the Width and height of the display
infoObject = pygame.display.Info()


class main():


    def set_state(self , state):
        self.state = state


    def draw_splash_screen(self , drawingSurface , width , height):
        canvas = drawingSurface
        pygame.draw.rect(canvas, (0, 255, 0), (0,0, width , height))


    def draw_main_menu(self , drawingSurface , width , height):
        canvas = drawingSurface
        pygame.draw.rect(canvas, (0, 65, 0), (0,0, width , height))


    def repaint(self):
        if (self.state == "Splash"):
            self.draw_splash_screen(self.canvas, self.width, self.height)
        if (self.state == "MainMenu"):
            self.draw_main_menu(self.canvas, self.width, self.height)

    def __init__(self , title, state , width, height):
        self.title = title
        self.width = width
        self.height = height
        self.state = "Splash"

        # create our screen
        self.canvas = pygame.display.set_mode((width, height))

        #Set our title
        pygame.display.set_caption(self.title)



        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    print("mouse button up!")
                    self.set_state("MainMenu")


            self.repaint()
            pygame.display.update()
