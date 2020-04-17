# Hidden Message
# by Cesare Tidler

"""
Encryption Key:
    A = Z
    B = Y
    C = X
    D = W
    E = V
    F = U
    G = T
    H = S
    I = R
    J = Q
    K = P
    L = O
"""

# Get user message
message = str(input("Enter your message to encrypt here: "))


# Replace the characters with encrypted characters    
string_to_build = '' # create an empty string that we'll build with characters from the message
for letter in message: # loops over each character in the message    

    # encryption key
    if letter == "A":
        letter = "Z"
    elif letter == "a":
        letter = "z"
    elif letter == "B":
        letter = "Y"
    elif letter == "b":
        letter = "y"
    elif letter == "C":
        letter = "X"
    elif letter == "c":
        letter = "x"
    elif letter == "D":
        letter = "W"
    elif letter == "d":
        letter = "w"
    elif letter == "E":
        letter = "V"
    elif letter == "e":
        letter = "v"
    elif letter == "F":
        letter = "U"
    elif letter == "f":
        letter = "u"
    elif letter == "G":
        letter = "T"
    elif letter == "g":
        letter = "t"
    elif letter == "H":
        letter = "S"
    elif letter == "h":
        letter = "s"
    elif letter == "I":
        letter = "R"
    elif letter == "i":
        letter = "r"
    elif letter == "J":
        letter = "Q"
    elif letter == "j":
        letter = "q"
    elif letter == "K":
        letter = "P"
    elif letter == "k":
        letter = "p"
    elif letter == "L":
        letter = "O"
    elif letter == "l":
        letter = "o"
    elif letter == "Z":
        letter = "A"
    elif letter == "z":
        letter = "a"
    elif letter == "Y":
        letter = "B"
    elif letter == "y":
        letter = "b"
    elif letter == "X":
        letter = "C"
    elif letter == "x":
        letter = "c"
    elif letter == "W":
        letter = "D"
    elif letter == "w":
        letter = "d"
    elif letter == "V":
        letter = "E"
    elif letter == "v":
        letter = "e"
    elif letter == "U":
        letter = "F"
    elif letter == "u":
        letter = "f"
    elif letter == "T":
        letter = "G"
    elif letter == "t":
        letter = "g"
    elif letter == "S":
        letter = "H"
    elif letter == "s":
        letter = "h"
    elif letter == "R":
        letter = "I"
    elif letter == "r":
        letter = "i"
    elif letter == "Q":
        letter = "J"
    elif letter == "q":
        letter = "j"
    elif letter == "P":
        letter = "K"
    elif letter == "p":
        letter = "k"
    elif letter == "O":
        letter = "L"
    elif letter == "o":
        letter = "l"

    string_to_build = string_to_build + letter # replaces the characters, else just adds the character to the string


# Reverse the string
reversed_string = ''.join(reversed(string_to_build)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed_string) #print the reversed string
