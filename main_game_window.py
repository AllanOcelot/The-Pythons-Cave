"""
    This is our main game window.
    It houses all of the displays for our game and handles the keyboard events.
"""


#Import PyGame
import pygame, sys , os
import example_map
import player
import pygame.font
from pygame.locals import *

#Import everything we need from Pygame
from pygame.locals import *

# Init Pygame
pygame.init()


#Get the Width and height of the display
infoObject = pygame.display.Info()


player = player.player("Allan, the developer ", 100, 0, 0, 0)

class main():


    def set_state(self , state):
        self.state = state


    def draw_splash_screen(self , canvas , width , height):
        pygame.draw.rect(canvas, (0, 255, 0) , (0,0, width , height))


    def draw_player_avatar(self , canvas , screen_width , screen_height):
        #The player will have an avatar in the bottom left corner of the screen
        #The idea is that this will animate while the user moves / speaks / interacts etc
        pygame.draw.rect(canvas, (144, 133, 66) , ( 20 , screen_height - 149 , 129 , 129 ) )



    def draw_mini_map(self , canvas):
        pygame.draw.rect(canvas,  (75,75,75) , (20 , 20 , 120 , 120))



    def draw_textarea(self, canvas , screen_width , screen_height):
        #This is our screen area in the bottom left section
        #I'll have to have a big long string of 'Recent Text'
        #And trim the begging of the text off

        textarea_height = 550
        textarea_width  = 240


        #First we draw the black background for the text to be display on
        pygame.draw.rect(canvas, (0,0,0), (0, screen_height - 550 / 2.5 ,textarea_height ,textarea_width))

        stringToPrint = "You look around the dungeon. Things are not looking good."
        fontobject = pygame.font.Font(None, 16)
        canvas.blit(fontobject.render(stringToPrint, 1, (255, 255, 255)),( 20, screen_height - 20))







    def draw_main_menu(self , drawingSurface , width , height):


        #This code is a lie, it actually draws the 'inventory'


        """
            For each item in inventory
            get it's image location (as a string)
            load it and display it relative to the inventory icon

        """

        #Declare what we are drawing to
        canvas = drawingSurface

        #Draw the background color
        #pygame.draw.rect(canvas, (46, 1, 17), (0,0, width , height))


        #We want the tool bar to be 20 pixels from the bottom of the screen
        inventory_top_position = height - 120

        #And we want it to be 20 pixels from the left side
        inventory_left_position = 150

        #Load the icon bar
        toolbar_texture = pygame.image.load(os.path.join("Assets/items", "item-bar-container.png")).convert_alpha()


        canvas.blit(toolbar_texture, ( inventory_left_position , inventory_top_position ))


        #What current index of the inventory are we on
        currentInventoryIndex = 0

        for item in player.inventory:
            #We only want to display four items
            if(currentInventoryIndex < 4):

                inventoryImageLeft = 0

                if(currentInventoryIndex == 0):
                    inventoryImageLeft = inventory_left_position + 20
                if(currentInventoryIndex == 1):
                    inventoryImageLeft = inventory_left_position + 96
                if(currentInventoryIndex == 2):
                    inventoryImageLeft = inventory_left_position + 172
                if(currentInventoryIndex == 3):
                    inventoryImageLeft = inventory_left_position + 248


                #Load the current item's texture
                item_texture = pygame.image.load(os.path.join("Assets/items", item.image_source )).convert_alpha()
                #But scale it up, to 64 * 64 pixels
                item_texture = pygame.transform.scale(item_texture, (64, 64))

                canvas.blit(item_texture, ( inventoryImageLeft , inventory_top_position + 20  )  )
                currentInventoryIndex = currentInventoryIndex + 1









    def repaint(self):
        if (self.state == "Splash"):
            self.draw_splash_screen(self.canvas, self.width, self.height)

        if (self.state == "MainMenu"):
            #self.draw_main_menu(self.canvas, self.width, self.height)
            #self.draw_player_avatar(self.canvas , self.width , self.height)
            self.draw_mini_map(self.canvas)
            self.draw_textarea(self.canvas, self.width , self.height)
            pygame.display.flip()





    def __init__(self , title, state , width, height):
        self.title = title
        self.width = width
        self.height = height
        self.state = "Splash"

        # create our screen
        self.canvas = pygame.display.set_mode((width, height), HWSURFACE |  DOUBLEBUF | RESIZABLE)

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


            #We want to constantly repaint the screen
            self.repaint()
            pygame.display.update()
