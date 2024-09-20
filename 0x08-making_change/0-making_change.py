#!/usr/bin/python3
"""
This module provides a function to determine the minimum number of coins
needed to make a given total amount.
"""
import sys


def makeChange(coins, total):
    """
    Functions:
    makeChange(coins, total):
        Determines the minimum number of coins needed to make the given total.

    Usage:
    Run the script with the following command:
    python3 0-making_change.py <total> <coin1,coin2,...>

    Example:
        python3 0-making_change.py 11 1,2,5
    """
    if total <= 0:
        return 0

    # Create a DP array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make total 0

    # Populate the DP table
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, return -1 (means total can't be met)
    return dp[total] if dp[total] != float('inf') else -1


# Command-line interface
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 0-making_change.py <total> <coin1,coin2,...>")
        sys.exit(1)

    try:
        # Parse the arguments
        total = int(sys.argv[1])
        coins = list(map(int, sys.argv[2].split(',')))

        # Call the makeChange function
        result = makeChange(coins, total)
        print(result)

    except ValueError:
        print("Invalid input, integers for the total and coin denominations.")
        sys.exit(1)
