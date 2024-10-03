#!/usr/bin/python3
""" Module for Prime Game """


def sieve(n):
    """Sieve of Eratosthenes to find all primes less than or equal to n"""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    """Determine who is the winner of the most rounds"""
    if x < 1 or not nums:
        return None

    # Find the maximum value in nums to calculate primes up to that number
    max_n = max(nums)

    # Get a list of prime numbers up to max_n
    primes = sieve(max_n)

    # Precompute the number of prime selections possible for each n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # For each round, determine the winner
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
