import player

player = player.player()

 #Get the player's input and return it when we call this function
def get_player_command():
    return input('Action: ')

#Our main function to start the game
def play():
    print("Welcome To The Python's Cave!")
    command = get_player_command()
    if  (command == "North"):
        print("You head north down a deep dark forest")
    elif (command == "East"):
        print("You head east into the cold cold trees")
    elif (command == "South"):
        print("You turn back, heading south")
    elif (command == "West"):
        print("On second thought, let's not go West, Tis a silly place.")



    if( command == "Check Inventory"):
        print(player.inventory)
    play()



play()