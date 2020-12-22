# imports
import random

# states
X = 'X'
O = 'O'
EMPTY = ' '

# board
board = [EMPTY, EMPTY, EMPTY,
         EMPTY, EMPTY, EMPTY,
         EMPTY, EMPTY, EMPTY]

moves = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

# player

player = X


# display function
def display_board():
    print()
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
    print()


def row_winner():
    if board[0] == board[1] == board[2] == X:
        return X
    if board[0] == board[1] == board[2] == O:
        return O
    if board[3] == board[4] == board[5] == X:
        return X
    if board[3] == board[4] == board[5] == O:
        return O
    if board[6] == board[7] == board[8] == X:
        return X
    if board[6] == board[7] == board[8] == O:
        return O
    return None


def col_winner():
    if board[0] == board[3] == board[6] == X:
        return X
    if board[0] == board[3] == board[6] == O:
        return O
    if board[1] == board[4] == board[7] == X:
        return X
    if board[1] == board[4] == board[7] == O:
        return O
    if board[2] == board[5] == board[8] == X:
        return X
    if board[2] == board[5] == board[8] == O:
        return O
    return None


def diag_winner():
    if board[0] == board[4] == board[8] == X:
        return X
    if board[0] == board[4] == board[8] == O:
        return O
    if board[2] == board[4] == board[6] == X:
        return X
    if board[2] == board[4] == board[6] == O:
        return O
    return None


def tie():
    if len(moves) == 0:
        return True
    else:
        return False


def winner():
    row = row_winner()
    col = col_winner()
    diag = diag_winner()
    if row == X:
        return X
    if col == X:
        return X
    if diag == X:
        return X
    if row == O or col == O or diag == O:
        return O
    return None


def terminal():
    if winner():
        return True
    if tie():
        return True
    return False


display_board()
while not terminal():
    if player == X:
        choice = input("Play your move " + str(moves) + " :")
        choice = int(choice)
        board[choice] = X
        moves.remove(choice)
        display_board()
        player = O
    elif player == O:
        choice = random.sample(moves, 1)[0]
        board[choice] = O
        moves.remove(choice)
        display_board()
        player = X

win = winner()
if win == X or win == O:
    print("Winner:- " + win)
else:
    print("Draw")
