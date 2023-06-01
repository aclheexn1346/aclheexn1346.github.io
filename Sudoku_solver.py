#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:24:02 2023

@author: alexchen
"""

def find_empty_space(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None

def solve(board):
    empty_space = find_empty_space(board) # find the first empty space on the board
    if not empty_space: # if there are no empty spaces, then return True
        return True
    else:
        row,col = empty_space 
        for num in range(1,10):
            if is_valid_board(board, num, row, col):
                board[row][col] = num
                if solve(board):
                    return True
                board[row][col] = 0
        return False
            
def is_valid_board(board, num, row, col):
    for column in range(9):
        if board[row][column] == num:
            return False
    for row_num in range(9):
        if board[row_num][col] == num:
            return False
    # Checking the lil box for all 9 numbers
    lower_row = 3*(row//3)
    lower_col = 3*(col//3)
    for i in range(lower_row, lower_row + 3):
        for j in range(lower_col, lower_col + 3):
            if board[i][j] == num:
                return False
    return True


board = [
  [5, 0, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 3, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve(board)
