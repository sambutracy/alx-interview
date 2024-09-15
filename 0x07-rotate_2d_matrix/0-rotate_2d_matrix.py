#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise.
    The matrix is modified in-place.
    
    Args:
        matrix (list of list of int): 2D matrix to be rotated.
    """
    n = len(matrix)  # Get the size of the matrix
    
    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row to get the rotated matrix
    for i in range(n):
        matrix[i].reverse()
