import time

print("Welcome to the Vacations version of Mad Libs!\n")
time.sleep(2)
print("We'll begin by having you enter some words, and we'll tell you what type of word it should be.\n")
time.sleep(2)
print("When you see the prompt, type a word and press Enter\n")
time.sleep(2)
print("At the end, a Mad Lib will generate with your chosen words!\n")
time.sleep(2)
print("Let's get started!\n")
time.sleep(2)

adj1 = input("Type an ADJECTIVE: ")
adj2 = input("Type an ADJECTIVE: ")
noun = input("Type a NOUN: ")
noun2 = input("Type a NOUN: ")
plnoun = input("Type a PLURAL NOUN: ")
game = input("Type a GAME: ")
plnoun2 = input("Type a PLURAL NOUN: ")
verbing = input("Type a VERB ENDING IN 'ING': ")
verbing2 = input("Type a VERB ENDING IN 'ING': ")
plnoun3 = input("Type a PLURAL NOUN: ")
verbing3 = input("Type a VERB ENDING IN 'ING': ")
noun3 = input("Type a NOUN: ")
plant = input("Type a PLANT: ")
body = input("Type a PART OF THE BODY: ")
place = input("Type a PLACE: ")
verbing4 = input("Type a VERB ENDING IN 'ING': ")
adj3 = input("Type an ADJECTIVE: ")
num = input("Type a NUMBER: ")
plnoun4 = input("Type a PLURAL NOUN: ")
time.sleep(3)
print("You're done! Generating Vacation Mad Libs:\n")

print("A vacation is when you take a trip to some "+adj1+" place")
print("with your "+adj2+" family. Usually you go to some place")
print("that is near a/an "+noun+" or up on a/an "+noun2+".")
print("A good vacation place is one where you can ride "+plnoun+"")
print("or play "+game+" or go hunting for "+plnoun2+". I like")
print("to spend my time "+verbing+" or "+verbing2+". When parents go")
print("on a vacation, they spend their time eating three "+plnoun3+"")
print("a day, and fathers play golf, and mothers sit around "+verbing3+".")
print("Last summer, my little brother fell in a/an "+noun3+"")
print("and got poison "+plant+" all over his "+body+".")
print("My family is going to go to (the) "+place+", and I will practice "+verbing4+".")
print("Parents need vacations more than kids because parents are always very")
print(""+adj3+" and because they have to work "+num+" hours every day all year")
print("making enough "+plnoun4+" to pay for the vacation.")