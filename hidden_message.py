# Hidden Message
# by Cesare Tidler

"""
Encryption Key:
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 0
    K = Z
    L = Y
"""

# Get user message
message = str(input("Enter your message to encrypt here: "))


# Replace the characters with encrypted characters    
string_to_build = '' # create an empty string that we'll build with characters from the message
for letter in message: # loops over each character in the message    

    # encryption key
    if letter.upper() == "A":
        letter = "1"
    elif letter.upper() == "B":
        letter = "2"
    elif letter.upper() == "C":
        letter = "3"
    elif letter.upper() == "D":
        letter = "4"
    elif letter.upper() == "E":
        letter = "5"
    elif letter.upper() == "F":
        letter = "6"
    elif letter.upper() == "G":
        letter = "7"
    elif letter.upper() == "H":
        letter = "8"
    elif letter.upper() == "I":
        letter = "9"
    elif letter.upper() == "J":
        letter = "0"
    elif letter == "K":
        letter = "Z"
    elif letter == "k":
        letter = "z"
    elif letter == "L":
        letter = "Y"
    elif letter == "l":
        letter = "y"
    elif letter.upper() == "1":
        letter = "A"
    elif letter.upper() == "2":
        letter = "B"
    elif letter.upper() == "3":
        letter = "C"
    elif letter.upper() == "4":
        letter = "D"
    elif letter.upper() == "5":
        letter = "E"
    elif letter.upper() == "6":
        letter = "F"
    elif letter.upper() == "7":
        letter = "G"
    elif letter.upper() == "8":
        letter = "H"
    elif letter.upper() == "9":
        letter = "I"
    elif letter.upper() == "0":
        letter = "J"
    elif letter == "Z":
        letter = "K"
    elif letter == "Y":
        letter = "L"
    elif letter == "z":
        letter = "k"
    elif letter == "y":
        letter = "l"

    string_to_build = string_to_build + letter # replaces the characters, else just adds the character to the string


# Reverse the string
reversed_string = ''.join(reversed(string_to_build)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed_string) #print the reversed string
