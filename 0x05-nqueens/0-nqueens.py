#!/usr/bin/python3
"""This module solves the N queens problem
"""
import sys


if (len(sys.argv) != 2):
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)
if (N < 4):
    print("N must be at least 4")
    exit(1)

# create board (list of lists to hold queens)
board = [[0 for i in range(N)] for i in range(N)]

# result list of lists
res = []

# the locations that will constraint the position of a placed Queen
col = []
rightdiag = []
leftdiag = []


def backtrack(row):
    """ This recursive function places a Queen starting at row 0
    then checks for constraints found in lists (col, rightdiag, leftdiag)
    if found it skips to the next columns ``continue``.
    """
    if row >= N:  # basecase for recursion function
        sol = []
        for i in range(len(board)):
            pos = []
            for column in range(len(board[i])):
                if board[i][column] == 1:
                    pos += [[i, column]]
            sol += pos
        res.append(sol)  # adding one solution to the result list.
        return

    for c in range(N):  # check if poisition is restricted by lists.
        if c in col or (row + c) in rightdiag or (row - c) in leftdiag:
            continue

        col.append(c)  # code program runs while testing a position.
        rightdiag.append(row + c)
        leftdiag.append(row - c)
        board[row][c] = 1  # places a queen at position.

        backtrack(row + 1)  # recursive call

        col.remove(c)  # code program runs while backtracking.
        rightdiag.remove(row + c)
        leftdiag.remove(row - c)
        board[row][c] = 0
    return


backtrack(0)
for solution in res:
    print(solution)
