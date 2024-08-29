#!/usr/bin/python3
"""
nqueens.py: N queens problem gets solved using a backtracking algorithm.
It places N non-attacking queens on an N×N chessboard.
Prints all solutions.
"""

import sys


def isSafe(board, row, col):
    """
    isSafe: checks if a queen can be placed on board[row][col]
    without being attacked by any other queen.

    Args:
        board (list): The current board configuration.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for c in range(col):
        if board[c] == row or abs(c - col) == abs(board[c] - row):
            return False
    return True


def solveNQueens(N):
    """
    solveNQueens: Solves the N queens problem using backtracking.

    Args:
        N (int): The size of the chessboard (N×N).
    """
    def solveNQueensUtil(board, col):
        """
        solveNQueensUtil: Utility function to solve N queens problem.

        Args:
            board (list): The current board configuration.
            col (int): The current column being processed.
        """
        if col == N:
            print([[c, board[c]] for c in range(N)])
            return
        for row in range(N):
            if isSafe(board, row, col):
                board[col] = row
                solveNQueensUtil(board, col + 1)
                board[col] = -1  # Backtrack

    board = [-1 for _ in range(N)]
    solveNQueensUtil(board, 0)


def main():
    """
    Main function to parse input arguments and solve the N Queens problem.

    Exits with status 1 if input is invalid.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Start the backtracking algorithm
    solveNQueens(N)


if __name__ == "__main__":
    main()
