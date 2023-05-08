def you_died(why):
    print(f"{why}. Bye now!")
    exit(0)

def blue_door_room():
    "The player finds a treasure chest, options to investigate the treasure chest or guard"
    treasure_chest = ["diamonds", "gold", "silver", "sword"]
    print("You see a room with a wooden treasure chest on the left and a sleeping guard on the right in front of the door.")

    action = input("What do you do? ").lower()

    #way to see if the text typed by the player is in the list
    if action in ["treasure", "chest", "left"]:
        print("oooh treasure!")
    else:
        print("The guard is more interesting, let's go that way!")


    

def red_door_room():
    print("Once you open the door, you see a great big dragon.")
    print("It stares at you through one narrowed eye")
    print("Do you flee for your life or stay?")

    next_move = input(" ")

    if "flee" in next_move:
        start_adventure()
    else:
        you_died("You froze in place and the dragon decided to eat you up. Welp, too bad.")
        
def start_adventure():
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = input("Do you pick the red door or the blue door? ")


    if door_picked == "red":
        print("You picked the red door")
        red_door_room()
    elif door_picked == "blue":
        print("You picked the blue door")
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You've failed already, byeeeee.")

def main():

    #Gets the players name, prints it out and starts the adventure

    player_name = input("What's your name?\n ")
    print(f"Your name is {player_name}.")

    #Call another function dclared above´

    start_adventure()

if __name__ == '__main__':
    main()


