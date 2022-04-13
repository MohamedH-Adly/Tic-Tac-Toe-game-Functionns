
import numpy as np
import random

def create_board():
    return np.zeros((3,3), dtype=int)

def place(board, player, position=()):
    if board[position]==0:
        board[position]=player
        return board
    else:
        print ("This position already equal to ", board[position])
        return board

def possibilities(board):
    avalposi=np.where(board==0)
    return list(zip(avalposi[0], avalposi[1]))

def random_place(board, player):
    posi=random.choice(possibilities(board))
    board[posi]=player
    return board

def row_win(board, player):
    for i in range(3):
        if (board[i,0]==player and board[i,1]==player and board[i,2]==player):
            return True
    return False

def colum_win(board, player):
    for i in range(3):
        if (board[0,i]==player and board[1, i]==player and board[2, i]==player):
            return True
    return False

def diag_win(board, player):
    if ((board[0,0]==player and board[1, 1]==player and board[2, 2]==player) or (board[0,2]==player and board[1, 1]==player and board[2, 0]==player)):
        return True
    return False

def evaluate(board):
    if (row_win(board, 1) or colum_win(board, 1) or diag_win(board, 1)):
        return 1
    elif(row_win(board, 2) or colum_win(board, 2) or diag_win(board, 2)):
        return 2
    elif(np.any(board==0)):
        return 0
    else:
        return -1

def play_game():
    board=create_board()
    for i in range(5):
        for j in range(1,3):
            random_place(board, j)
            event=evaluate(board)
            if event==0:
                continue
            else:
                return event

def play_strategic_game():
    board=create_board()
    for i in range(5):
        for j in range(1,3):
            if (i==0 and j==1):
                place(board, 1, (1,1))
            else:
                random_place(board, j)
            event=evaluate(board)
            if event==0:
                continue
            else:
                return event

