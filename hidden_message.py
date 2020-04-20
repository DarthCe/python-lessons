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

# Set up the in and out values for the maketrans function
in_values = 'ABCDEFGHIJKLabcdefghijklZYXWVUTSRQPOzyxwvutsrqpo'
out_values = 'ZYXWVUTSRQPOzyxwvutsrqpoABCDEFGHIJKLabcdefghijkl'


# Get user message
message = str(input("Enter your message to encrypt here: "))


# Replace the characters with encrypted characters    
mapping = str.maketrans(in_values,out_values) # creates the mapping which gets passed into the translate function
string_to_build = message.translate(mapping) # creates the string using the translate function


# Reverse the string
reversed_string = ''.join(reversed(string_to_build)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed_string) #print the reversed string
