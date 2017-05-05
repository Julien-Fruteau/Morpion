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

# board = create_board()
# for i in range(3):
#     for player in [1, 2]:
#         board = random_place(board, player)
#
# print(board)

# EXERCISE 6
#
# Instructions:
# * Now that players may place their pieces, how will they know they've won?
#   Make a function row_win(board, player) that takes the player (integer),
#   and determines if any row consists of only their marker.
#   Have it return True if this condition is met, and False otherwise.
# * board is already defined from previous exercises.
#   Call row_win to check if Player 1 has a complete row.

def row_win(board, player):
    for i in range(dim_board):
        if np.all(board[i] == player):
            return(True)
    return(False)
    # if len(np.unique(np.where(board == player)[0])) == 1:
    #     return(True)
    # else:
    #     return(False)

# row_win(board, 1)

# EXERCISE 7
#
# Instructions:
# * Create a similar function col_win(board, player) that takes
#   the player (integer), and determines if any column consists of only
#   their marker. Have it return True if this condition is met,
#   and False otherwise.
# * board is already defined from previous exercises. Call col_win to check
#   if Player 1 has a complete column.

def col_win(board, player):
    for i in range(dim_board):
        if np.all(np.transpose(board)[i] == player):
            return(True)
    return(False)
    # !!! Don't work for board with less than 3 rounds !!!
    # if len(np.unique(np.where(board == player)[1])) == 1:
    #     return(True)
    # else:
    #     return(False)

# col_win(board, 1)

# EXERCISE 8
#
# Instructions:
# * Finally, create a function diag_win(board, player) that tests if either
#   diagonal of the board consists of only their marker.
#   Have it return True if this condition is met, and False otherwise.
# * board is already defined from previous exercises.
#   Call diag_win to check if Player 1 has a complete diagonal.

def diag_win(board, player):
    diag1 = np.diag(board)
    diag2 = np.diag(np.fliplr(np.transpose(board)))
    return((np.all(diag1 == player) or np.all(diag2 == player)))
    # !!Works only for dim_board = 3!!

# diag_win(board, 1)

# EXERCISE 9
#
# Instructions:
# * Create a function evaluate(board) that uses row_win, col_win,
#   and diag_win functions for both players. If one of them has won,
#   return that player's number. If the board is full but no one has won,
#   return -1. Otherwise, return 0.
# * board is already defined from previous exercises. Call evaluate to see
#   if either player has won the game yet.

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.
        # if so, store `player` as `winner`.
        if (row_win(board, player) or \
            col_win(board, player) or \
            diag_win(board, player)):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# evaluate(board)

# EXERCISE 10
#
# Instructions:
# * create_board(), random_place(board, player), and evaluate(board)
#   have been created from previous exercises. Create a function play_game()
#   that creates a board, calls alternates between two players
#   (beginning with Player 1), and evaluates the board for a winner after
#   every placement. Play the game until one player wins (returning 1 or 2
#   to reflect the winning player), or the game is a draw (returning -1).
# * Call play_game once.

def play_game():
    # init game
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    # return(winner, board)
    return(winner)

play_game()

# def test_draw():
#  !!!! UNCOMMENT return(winner, board) from def play_game() !!!!
#     my_win = (0,0)
#     iteration = 0
#     while my_win[0] != -1 and iteration < 100:
#         my_win = play_game()
#         iteration += 1
#     print(my_win[1], iteration)
# test_draw()
