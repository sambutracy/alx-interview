#!/usr/bin/python3
"""
This module provides a function to generate Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.
    Returns an empty list if n <= 0.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # First element of each row is 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of each row is 1
        triangle.append(row)

    return triangle