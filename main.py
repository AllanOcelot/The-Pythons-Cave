import player

import main_game_window


"""
    Main.PY runs our game.
    We use a global Game State to call different states.
    E.g - 
    Run Program, Launch Splash Screen, Launch Main Menu,  Main Menu -> New | Load | Options 
"""



#What is the game state, when launch it will always be Splash
#Availale states.
#Splash Screen. Main Menu. Character Creation. New Game. Load Game. Option. Exit.
gameState = "Splash"


#When our game loads, start the main game window
gameWindow = main_game_window.main("Title here", "Splash", 1000 , 800)

if(gameState == "Splash"):
   print("Game should fire a new Game window type. Passing the argument 'Splash' to it.  ")
if(gameState == "MainMenu"):
   print("Game should close the splashScreen and change it to the MainMenu")



# Set up the player
#player = player.player("Allan, the developer ", 100, 0, 0, 0)

    #Get the player's input and return it when we call this function
def get_player_command():
    return input('Action: ')

#Our main function to start the game
def play():
    command = get_player_command()
    if  (command == "North"):
        print("You head north down a deep dark forest")
    elif (command == "East"):
        print("You head east into the cold cold trees")
    elif (command == "South"):
        print("You turn back, heading south")
    elif (command == "West"):
        print("On second thought, let's not go West, Tis a silly place.")



    #Player Commands
    if( command == "Check Inventory"):
        print(player.getPlayerInventory())


    if( command == "Main Menu"):
        gameWindow.set_state("MainMenu")

    play()


print("Welcome To The Python's Cave!")
play()