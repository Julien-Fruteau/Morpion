# ***************    PYTHON FOR DATA SCIENCE    *************** #

# ***************          HOMEWORK 2           *************** #

# Tic-tac-toe (or noughts and crosses) is a simple strategy game
#  in which two players take turns placing a mark on a 3x3 board,
#  attempting to make a row, column, or diagonal of three with
#  their mark.
# In this homework, we will use the tools we've covered in the
#  past two weeks to create a tic-tac-toe simulator, and evaluate
#  basic winning strategies.

# EXERCISE 1
#
# Instructions:
# * For our tic-tac-toe board, we will use a numpy array with
#   dimension 3 by 3. Make a function create_board() that creates
#   such a board, with values of integers 0.
# * Call create_board(), and store this as board.

import numpy as np
import random

# let's make dim_board a GLOBAL constance since it will be used
# latter in this homework. LEGB allows us to do so.
dim_board = 3

def create_board():
    return(np.zeros((dim_board, dim_board), dtype=int))

# board = create_board()

# EXERCISE 2
#
# Instructions:
# * Players 1 and 2 will take turns changing values of this
#   array from a 0 to a 1 or 2, indicating the number of the
#   player who places there. Create a function place(board,
#   player, position) with player being the current player
#   (an integer 1 or 2), and position a tuple of length 2
#   specifying a desired location to place their marker.
#   Only allow the current player to place a piece on the board
#   (change the board position to their number)
#   if that position is empty (zero).
# * Use create_board() to store a board as board, and use place
#   to have Player 1 place a piece on spot (0, 0).

def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    else:
        print("Move not allowed at position ", position)

# place(board, 1, (0,0))

# EXERCISE 3
#
# Instructions:
# * Create a function possibilities(board) that returns a list of
#   all positions (tuples) on the board that are not occupied (0).
#   (Hint: numpy.where is a handy function that returns a
#   list of indexes that meet a condition.)
# * board is already defined from previous exercises.
#   Call possibilities(board) to see what it returns!

def possibilities(board):
    # Let's PACK the tuple of 2 arrays returned by np.where:
    (ind_row, ind_col) = np.where(board == 0)
    # defined the list to be returned w/ List Comprehension:
    list_free_pos = [(ind_row[i], ind_col[i]) for i in range(len(ind_row))]
    return(list_free_pos)

# possibilities(board)

# EXERCISE 4
#
# Instructions:
# * Write a function random_place(board, player) that places a marker
#   for the current player at random among all the
#   available positions (those currently set to 0).
# * Find possible placements with possibilities(board).
# * Select one possible placement at random using random.choice(selection).
# * board is already defined from previous exercises.
#   Call random_place(board, player) to place a random
#   marker for Player 2, and store this as board to update its value.

def random_place(board, player):
    selection = random.choice(possibilities(board))
    place(board, player, selection)
    return(board)

# MAIN FLOW
# board = create_board()
# board = random_place(board, 2)

# EXERCISE 5
#
# Instructions:
# * board is already defined from previous exercises.
#   Use random_place(board, player) to place three pieces on board
#   each for players 1 and 2.
# * Print board to see your result.
board = create_board()
for i in range(3):
    for player in [1, 2]:
        board = random_place(board, player)

print(board)

# EXERCISE 6
#
# Instructions:
# * Now that players may place their pieces, how will they know they've won?
#   Make a function row_win(board, player) that takes the player (integer),
#   and determines if any row consists of only their marker.
#   Have it return True if this condition is met, and False otherwise.
# * board is already defined from previous exercises.
#   Call row_win to check if Player 1 has a complete row.

# Row consists of a player marker <=>
# all val of array tup(np.where(board == player))[0] are equals,
# i,e: array([0,0,0]), or array([1,1,1]) or array(2,2,2) (COND)
# np.unique() return an array with the unique values of an arg array.
# => its lenght is then == 1 only for (COND) above.

def row_win(board, player):
    if len(np.unique(np.where(board == player)[0])) == 1:
        return(True)
    else:
        return(False)

# row_win(board, 1)

# EXERCISE 7
#
# Instructions:
# *
