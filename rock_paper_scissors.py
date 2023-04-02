from random import randint

#create a list of play options:
options = ["rock", "paper", "scissors"]

#assign a random play to the computer between the indexes of 0(rock) and 2(scissors)
computer = options[randint(0,2)]
#set player value to False
player = False
#Create a variable to store number of victories of either computer or player
computer_count = 0
player_count = 0
'''create a while loop that will continue to iterate until either the
computer or the player reach 3 victories. It starts with the player 
choosing what option to pick. The program will then check to see whether
the choice of the player is the same as the computer's or different. If 
it's the same, it will say it's a tie. If it's different, it will compare
each of the choices and give different outputs. After each victory, the
victory count will go up to whoever won that round and the program will
show the user how many victories each competitor has.'''
while player == False:
    player = input("Rock, Paper or Scissors?\n").lower()

    #if player ties
    if player == computer:
        print("It's a tie! \n")
        print(f"Computer Victories: {str(computer_count)} \t Player Victories: {str(player_count)}\n")
        
    #if player uses rock and wins/loses

    elif player == "rock":

        if computer == "paper":
            print("Guess the computer got the better of you this time! Try again!\n")
            computer_count += 1
            print(f"Computer Victories: {str(computer_count)} \t Player Victories: {str(player_count)}\n")
        
        else:
            print("You really blunt that edge off the computer, you win!\n")
            player_count += 1
            print(f"Computer Victories: {str(computer_count)} \t Player Victories: {str(player_count)}\n")
    
    #if player uses paper and wins / loses

    elif player == "paper":

        if computer == "scissors":
            print("Scissors cut your choice! The computer wins this time! Try again!\n")
            computer_count += 1
            print(f"Computer Victories: {str(computer_count)} \t Player Victories: {str(player_count)}")
       
        else:
            print("You wrapped that rock so well it might as well be a Christmas present, good job! You win!\n")
            player_count += 1
            print(f"Computer Victories: {str(computer_count)} \t Player Victories: {str(player_count)}\n")
    
    #if player uses scissors and wins /loses

    elif player == "scissors":

        if computer == "rock":
            print("The computer just keeps showing that it rocks! Computer Wins! Try again!\n")
            computer_count += 1
            print(f"Computer Victories: {str(computer_count)} \t Player Victories: {str(player_count)}\n")
        
        else:
            print("You cut, cut, cut that paper now, you cuut the paper awaayy! You win!\n")
            player_count +=1 
            print(f"Computer Victories: {str(computer_count)} \t Player Victories: {str(player_count)}\n")
    
    else:
        print("Ooops, seems like you didn't type any of the options, give it another go. \n")

    #reset the value of player to False so the loop can restart
    player = False
    #assign another random value to computer so it's not always the same through each iteration
    computer = options[randint(0,2)]
    #
    if computer_count == 3:
        print("A-ha! \n Computer Wins the Lot!")
        break
    if player_count == 3:
        print("You won it a-hall! Good job!")
        break
    
  
