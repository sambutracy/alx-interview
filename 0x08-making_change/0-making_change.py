#!/usr/bin/python3
import sys
"""
This module provides a function to determine the minimum number of coins
needed to make a given total amount.
Functions:
    makeChange(coins, total):
        Determines the minimum number of coins needed to make the given total.
Usage:
    Run the script with the following command:
    python3 0-making_change.py <total> <coin1,coin2,...>
    Example:
        python3 0-making_change.py 11 1,2,5
"""


def makeChange(coins, total):
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
    if __name__ == "__main__":

        if len(sys.argv) != 3:
            print("Usage: {} <total> <coin1,coin2,...>".format(sys.argv[0]))
            sys.exit(1)

        total = int(sys.argv[1])
        coins = list(map(int, sys.argv[2].split(',')))

        result = makeChange(coins, total)
        print(result)