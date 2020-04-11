## Tic-Tac-Toe!
## by Cesare Tidler

import random
import time              

#these will be used to sanitize input later
marks = ["X","O"]
round_limit_check = [3,5,7]
turn_order_check = ["1","2"]
placement_check = [1,2,3,4,5,6,7,8,9]

#Set up variables
round_won = False
player1_win_count = 0
player2_win_count = 0

print("Welcome to Tic-Tac-Toe!")
time.sleep(2)

# Both players choose a symbol
player1_mark = input("\nPlayer One - type either an X or an O to choose your symbol: ").strip().upper()
while player1_mark not in marks:
    player1_mark = input("Please only enter an X or an O and press enter: ").strip().upper()
if player1_mark == "X":
    player2_mark = "O"
elif player1_mark == "O":
    player2_mark = "X"

# Players pick who they want to go first
time.sleep(.5)
go_first = input("\nWho should go first?  Type 1 for Player One or 2 for Player Two: ").strip()
while go_first not in turn_order_check:
    go_first = input("Please only enter a 1 or a 2 to choose who goes first: ").strip()

# Subtract 1 from go_first to make it easier for the player turn to loop around
time.sleep(.5)
go_first = int(go_first) - 1

# Players choose how many games they want to play
round_limit = int(input("\nDo you want to play best of 3, 5, or 7?  Type either 3, 5 or 7 to choose: "))
while round_limit not in round_limit_check:
    round_limit = int(input("Please only type 3, 5, or 7 to choose the potential games in a series: "))
if round_limit == 3:
    p1_wins_needed = 2
    p2_wins_needed = 2
elif round_limit == 5:
    p1_wins_needed = 3
    p2_wins_needed = 3
elif round_limit == 7:
    p1_wins_needed = 4
    p2_wins_needed = 4

# Draw the board
board = ["empty"," "," "," "," "," "," "," "," "," "]
def drawBoard ():
    print(board[7:10])
    print(board[4:7])
    print(board[1:4])

# Get input to make player's mark (X or O) on board (1-9) for whoever's turn it is
def makeMark ():
    print("\n")
    placement = int(input("Player " + str(turn_number + 1) + " - type a value between 1 and 9 to make a mark on the board: ").strip())
    while placement not in placement_check or board[placement] != " ":
        placement = int(input("Please only enter a 1 through 9 in an empty spot to make a mark on the board: ").strip())
    print("\n")
    if turn_number == 0:
        board[placement] = player1_mark
    else:
        board[placement] = player2_mark

# Explain the rules
time.sleep(1)
print("\nTo make a mark on the board, you type a number that is between 1 and 9.")
time.sleep(2.5)
print("\nEach spot on the board is represented by the number keys...here are the number keys for each spot on the board:\n")
time.sleep(2.5)
fake_board = ["1","2","3","4","5","6","7","8","9"]
def drawFakeBoard ():
    print(fake_board[6:9])
    print(fake_board[3:6])
    print(fake_board[0:3])
drawFakeBoard()
time.sleep(1.5)
print("\nAlright, let's get into the game! We'll start by drawing an empty board:\n")
time.sleep(2.5)

# Figure out who's turn it is to start the game
turn_number = go_first

# The game loop
while p1_wins_needed > 0 or p2_wins_needed > 0:
    drawBoard()
    makeMark()
    # Columns win check
    if board[7] == board[4] and board[7] == board[1] and board[7] != " ":
        round_won = True
    elif board[8] == board[5] and board[8] == board[2] and board[8] != " ":
        round_won = True
    elif board[9] == board[6] and board[9] == board[3] and board[9] != " ":
        round_won = True
    # Rows win check
    elif board[7] == board[8] and board[7] == board[9] and board[7] != " ":
        round_won = True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != " ":
        round_won = True
    elif board[1] == board[2] and board[1] == board[3] and board[1] != " ":
        round_won = True
    # Diagonals win check
    elif board[7] == board[5] and board[7] == board[3] and board[7] != " ":
        round_won = True
    elif board[9] == board[5] and board[9] == board[1] and board[9] != " ":
        round_won = True
    # Check for a Tie
    elif board[1] in ("X","O") and board[2] in ("X","O") and board[3] in ("X","O") and board[4] in ("X","O") and board[5] in ("X","O") and board[6] in ("X","O") and board[7] in ("X","O") and board[8] in ("X","O") and board[9] in ("X","O") and round_won != True:
        time.sleep(1)
        print("We have a tie! Let's clear the board...")
        board = ["empty"," "," "," "," "," "," "," "," "," "]
    # Check to see if round was won and who won it. If player wins the series, the loop breaks.
    if round_won == True:
        drawBoard()
        board = ["empty"," "," "," "," "," "," "," "," "," "]
        # Resets the rounds_won so the game won't think someone won on the next loop
        round_won = False
        if turn_number == 0:
            player1_win_count = player1_win_count + 1
            p1_wins_needed = p1_wins_needed - 1
            time.sleep(1)
            if p1_wins_needed > 0 and p2_wins_needed > 0:
                print("\nPlayer 1 won that round...keep playing!\n")
                time.sleep(1)
            else:
                break
        else:
            player2_win_count = player2_win_count + 1
            p2_wins_needed = p2_wins_needed - 1
            time.sleep(1)
            if p1_wins_needed > 0 and p2_wins_needed > 0:
                print("\nPlayer 2 won that round...keep playing!\n")
                time.sleep(1)
            else:
                break
    # Rotate between 0 and 1 which is Player 1 and Player 2 respectively
    turn_number = (turn_number + 1) % 2

# Declare the series winner!
if round_limit == 3 and player1_win_count == 2:
    time.sleep(1)
    print("\nCONGRATULATIONS Player 1!  You are the supreme Tic-Tac-Toe champion!")
elif round_limit == 3 and player2_win_count == 2:
    time.sleep(1)
    print("\nCONGRATULATIONS Player 2!  You are the supreme Tic-Tac-Toe champion!")
elif round_limit == 5 and player1_win_count == 3:
    time.sleep(1)
    print("\nCONGRATULATIONS Player 1!  You are the supreme Tic-Tac-Toe champion!")
elif round_limit == 5 and player2_win_count == 3:
    time.sleep(1)
    print("\nCONGRATULATIONS Player 2!  You are the supreme Tic-Tac-Toe champion!")
elif round_limit == 7 and player1_win_count == 4:
    time.sleep(1)
    print("\nCONGRATULATIONS Player 1!  You are the supreme Tic-Tac-Toe champion!")
elif round_limit == 7 and player2_win_count == 4:
    time.sleep(1)
    print("\nCONGRATULATIONS Player 2!  You are the supreme Tic-Tac-Toe champion!")
