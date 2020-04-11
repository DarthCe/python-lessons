#Dice Rolling Simulator

#https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

import random
import time

min = 1
max = 6

print("Welcome to the Dice Rolling Simulator! \n")
time.sleep(1.5)
print("Do you want to roll the dice? [y/n]")
decision = input()

while decision == "y" or decision == "Y" or decision == " y" or decision ==  " Y":
    print("\nRolling the dice...")
    time.sleep(1)
    print("You rolled: " + str(random.randint(min,max)) + " and " + str(random.randint(min,max)))
    print("\nRoll again? [y/n]")
    decision = input()
    if decision == "y" or decision == "Y" or decision == " y" or decision ==  " Y":
        continue
    else:
        print("\nSee you next time!")
    

