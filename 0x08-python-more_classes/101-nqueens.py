#!/usr/bin/python3

"""Defines a nqueens"""

import sys

def init_board(n):
    """Initialize an 'n'x'n' sized chessboard with 0's."""
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)
    return board

def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return [board_deepcopy(row) for row in board]
    return board

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solution.append([row, col])
                break
    return solution

def x_out(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no longer be played are X-ed out.
    
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
