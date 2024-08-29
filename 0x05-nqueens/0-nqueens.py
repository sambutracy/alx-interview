#!/usr/bin/python3
"""
This module solves the N Queens problem using a backtracking algorithm.

The N Queens problem is about placing N queens on an N×N chessboard
so that no two queens threaten each other.
"""

import sys

# Input validation
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

# Initialize the board and sets to track column and diagonal threats
board = [[0 for _ in range(N)] for _ in range(N)]
solutions = []
columns = set()
right_diagonals = set()
left_diagonals = set()


def solve_nqueens(row):
    """
    Recursively place queens on the board starting from the given row.

    This function uses backtracking to explore all possible placements
    of queens on the board while ensuring no two queens can attack each other.
    """
    if row == N:
        solution = [[r, c] for r in range(N)
                    for c in range(N) if board[r][c] == 1]
        solutions.append(solution)
        return

    for col in range(N):
        if col in columns or (row + col) in right_diagonals or \
               (row - col) in left_diagonals:
            continue

        # Place queen and update the tracking sets
        board[row][col] = 1
        columns.add(col)
        right_diagonals.add(row + col)
        left_diagonals.add(row - col)

        # Recurse to the next row
        solve_nqueens(row + 1)

        # Backtrack by removing the queen and updating the tracking sets
        board[row][col] = 0
        columns.remove(col)
        right_diagonals.remove(row + col)
        left_diagonals.remove(row - col)


# Start the backtracking process from the first row
solve_nqueens(0)

# Print all valid solutions
for solution in solutions:
    print(solution)
