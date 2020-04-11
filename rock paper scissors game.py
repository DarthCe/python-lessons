#Rock Paper Scissors game

import random
import time

print("Welcome to Rock Paper Scissors!")
time.sleep(2)
print("\nRules:\n   Game is best 2 out of 3\n   Type R for Rock, P for Paper, and S for Scissors")
time.sleep(2)

turns_left = 3
user_score = 0
computer_score = 0

while turns_left > 0 and user_score < 2 and computer_score < 2:
        
    comp_answer = random.randint(1,3)
    ## 1=R, 2=P, 3=S
    user_answer = input("\nPick [R]ock, [P]aper, or [S]cissors: ")

    ##user wins scenarios
    if user_answer == "R" and comp_answer == 3:
        print("\nComputer picks Scissors...Rock smashes scissors, YOU WIN!")
        user_score = user_score + 1
        turns_left = turns_left + 1
    elif user_answer == "P" and comp_answer == 1:
        print("\nComputer picks Rock...Paper covers Rock, YOU WIN!")
        user_score = user_score + 1
        turns_left = turns_left + 1
    elif user_answer == "S" and comp_answer == 2:
        print("\nComputer picks Paper...Scissors cuts Paper, YOU WIN!")
        user_score = user_score + 1
        turns_left = turns_left + 1
    ##user loses scenarios
    elif user_answer == "R" and comp_answer == 2:
        print("\nComputer picks Paper...Paper covers Rock, you lose :(")
        computer_score = computer_score + 1
        turns_left = turns_left + 1
    elif user_answer == "P" and comp_answer == 3:
        print("\nComputer picks Scissors...Scissors cuts Paper, you lose :(")
        computer_score = computer_score + 1
        turns_left = turns_left + 1
    elif user_answer == "S" and comp_answer == 1:
        print("\nComputer picks Rock...Rock smashes Scissors, you lose :(")
        computer_score = computer_score + 1
        turns_left = turns_left + 1
    ##tie scenarios
    elif user_answer == "R" and comp_answer == 1:
        print("\nComputer picks Rock, you tie...go again!")
    elif user_answer == "P" and comp_answer == 2:
        print("\nComputer picks Paper, you tie...go again!")
    elif user_answer == "S" and comp_answer == 3:
        print("\nComputer picks Scissors, you tie...go again!")
    ##bad user input
    else:
        print("\nPlease only type either R , P , or S to play!")

if user_score == 2:
    print("\nCONGRATULATIONS! You win :)")

if computer_score == 2:
    print("\nThe computer beat you :( , run the program again and give it another go!")

    

