#!/usr/bin/python3
"""
Module for 0x0C. N Queens.
Specializations - Interview Preparation ― Algorithms
"""
from sys import argv, exit


def solveNQueens(n):
    """Program that solves the N queens problem"""
    res = []
    queens = [-1] * n

    def dfs(index):
        """Recursively resolves the N queens problem"""
        if index == len(queens):  # n queens have been placed correctly
            res.append(queens[:])
            return
        for i in range(len(queens)):
            queens[index] = i
            if valid(index):
                dfs(index + 1)

    def valid(n):
        """Check whether nth queen can be placed"""
        for i in range(n):
            if abs(queens[i] - queens[n]) == n - i:  # same diagonal
                return False
            if queens[i] == queens[n]:
                return False
        return True

    def make_all_boards(solutions):
        """Build the list that will be returned"""
        actual_boards = []
        for queens_solution in solutions:
            board = []
            for row, col in enumerate(queens_solution):
                board.append([row, col])
            actual_boards.append(board)
        return actual_boards

    dfs(0)
    return make_all_boards(res)  # Ensure this return is correctly indented


if __name__ == "__main__":
    if len(argv) < 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)
    else:
        result = solveNQueens(n)
        for row in result:
            print(row)
