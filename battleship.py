#!/usr/bin/env python
 
from random import randint
 
playerboard = []
shipsboard = []
 
for x in range(5):
    playerboard.append(["O"] * 5)
 
for x in range(5):
    shipsboard.append(["O"] * 5)
 
def print_board(board):
    for row in board:
        print " ".join(row)
 
print "Let's play Battleship!"
 
howmanyships = 3
shipssunk = 0
 
def random_row(board):
    return randint(0, len(board) - 1)
 
def random_col(board):
    return randint(0, len(board[0]) - 1)
 
for shipnum in range(howmanyships):
    looksgoodtome = False
 
    while (looksgoodtome != True):   
        ship_row = random_row(shipsboard)
        ship_col = random_col(shipsboard)
        if (shipsboard[ship_row][ship_col] != 'Y'):
            looksgoodtome = True
            
    shipsboard[ship_row][ship_col] = 'Y'  
    print "Ship " + str(shipnum) + "pos: " + str(ship_row) + str(ship_col)
 
for turn in range(4):
    print "Turn", turn + 1
    print_board(playerboard)
 
   
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
 
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print "Oops, that's not even in the ocean."
	continue
 
    if (shipsboard[guess_row][guess_col] == "Y"):
	if (playerboard[guess_row][guess_col] == 'Y'):
		print "You have already sank that ship"
		continue
        print "You sank " + str(shipssunk+1) + " battleship!"
	playerboard[guess_row][guess_col] = 'Y'
	shipssunk += 1
	if (shipssunk == howmanyships):
		print "You won the game"
		break
        continue 
    else:
        if(playerboard[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            playerboard[guess_row][guess_col] = "X"
            if turn == 3:
                print "Game Over"