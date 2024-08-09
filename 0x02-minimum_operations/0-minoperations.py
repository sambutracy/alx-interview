#!/usr/bin/python3
"""This module defines the minOperations function
"""


def minOperations(n):
    """This function returns the fewest number of operations required
       to create n * 'H' characters. The only allowed operations are:
       Copy All and Paste.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed, or 0 if `n`
             is impossible to achieve.

    Example:
        For n = 9:
        H => Copy All => Paste => HH => Paste => HHH => Copy All =>
        Paste => HHHHHH => Paste => HHHHHHHHH
        Number of operations: 6
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
