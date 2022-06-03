# Creating python simple game called rock-paper=-scissor

import random

while True:
    print("Welcome to the game")
    print("Enter 'q' to leave the game")
    user = input("choose one from 'R for Rock, P for Paper, S for Scissor': ")
    if user == 'q':
        break
    user = user.upper()
    
    choices = ['R', 'P', 'S']

    cpu = random.choice(choices)
    if user == "R" and cpu == "R":
        print("Player (Rock) : CPU (Rock)")
        print("Its a draw")
        print("####################")
        continue
    elif user == "R" and cpu == "P":
        print("Player (Rock) : CPU (Paper)")
        print("You lose the computer wins!!!!")
        print("####################")
        break
    elif user == "R" and cpu == "S":
        print("Player (Rock) : CPU (Scissor)")
        print("***************")
        print("**** You win ****")
        break
    elif user == "P" and cpu == "R":
        print("Player (Paper) : CPU (Rock)")
        print("************")
        print("**** You win ****")
        break
    elif user == "P" and cpu == "P":
        print("Player (Paper) : CPU (Paper)")
        print("Its a draw")
        print("####################")
        continue
    elif user == "P" and cpu == "S":
        print("Player (Paper) : CPU (Scissor)")
        print("You lose the computer wins!!!")
        print("####################")
        break
    elif user == "S" and cpu == "R":
        print("Player (Scissor) : CPU (Rock)")
        print("You lose the computer wins!!!")
        print("####################")
        break
    elif user == "S" and cpu == "S":
        print("Player (Scissor) : CPU (Scissor)")
        print("Its a draw")
        print("####################")
        continue
    elif user == "S" and cpu == "P":
        print("Player (Scissor) : CPU (Paper)")
        print("***************")
        print("**** You win ****")
        break
    else:
        print("Invalid Input")
