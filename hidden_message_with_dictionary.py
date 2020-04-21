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

message = str(input("Enter your message to encrypt here: ")) # get user message
string = '' # set up empty string

# Create a dictionary
letter_mapping = {'A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O',
                  'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o',
                  'Z':'A','Y':'B','X':'C','W':'D','V':'E','U':'F','T':'G','S':'H','R':'I','Q':'J','P':'K','O':'L',
                  'z':'a','y':'b','x':'c','w':'d','v':'e','u':'f','t':'g','s':'h','r':'i','q':'j','p':'k','o':'l'}


# Replace the characters with encrypted characters   
for letter in message:  

    if letter in letter_mapping: # check if letter is in dictionary
        letter = letter_mapping[letter] # change the letter to its key pair to encrypt it
    else: # if letter isn't in dictionary
        letter = letter
        
    string = string + letter # builds string by using an empty string + letter
    

# Reverse the string
reversed_string = ''.join(reversed(string)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed_string) #print the reversed string
