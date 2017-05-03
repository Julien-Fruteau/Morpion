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
# let's make dim_board a GLOBAL var since it will be used
# for latter exercise. LEGB allows us to do so.
dim_board = 3
def create_board():
    return np.zeros((dim_board, dim_board), dtype=int)

board = create_board()

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
        print("Move not allowd at position ", position)
        print("Current Board Status:\n", board)

place(board, 1, (0,0))

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
    # np.where(board) would return a 2d-TUPLE ARRAY
    # with INDICES where VALUE != 0
    # Since we want INDICES where VALUE == 0, we create a 'board negative'.
    mask = create_board()
    board_negative = np.where(board, mask, 1)
    # Now we can extract indices values != 0
    board_empty_space = np.where(board_negative) # return a tuple w/ 2 arrays
    # To build a list of Tuples, get the two arrays and build a list

    # Let's PACK the tuple:
    (ind_row, ind_col) = board_empty_space
    list_of_pos_free = [(ind_row[i], ind_col[i]) \
                            for i in range(len(ind_row))]

    # for i in range(len(ind_row)):
    #     possibilities_list.append((ind_row[i], ind_col[i]))
    return list_of_pos_free

    # Added a comment for test git

possibilities(board)

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
