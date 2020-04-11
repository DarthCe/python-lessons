#Guess the Number

import random
import time

ran_num = random.randint(0,100)
guess_tries = 0

print("I'm thinking of a number! Hmmm...\n")
time.sleep(2)
print("I've got it!\n")
time.sleep(1.5)
print("Think you can guess it?  I'll give you 7 tries...\n")
time.sleep(1.5)
print("Enter a number between 0 and 100: ")

while guess_tries < 7:
    guess = int(input())
    guess_tries +=1
    if guess < ran_num:
        print("Guess higher!")
    elif guess > ran_num:
        print("Guess lower!")
    elif guess == ran_num:
        break

if guess == ran_num:
    print("\nAh, you got me. Nice job!")
    time.sleep(3)
    print("\nCONGRATULATIONS, WE HAVE A WINNER!")
    time.sleep(2)
    print("\nYou guessed it only " + str(guess_tries) + " guesses!  Look at you go.")

if guess != ran_num:
    print("\nBetter luck next time!")

    
