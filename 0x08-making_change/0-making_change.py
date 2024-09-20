#!/usr/bin/python3

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
