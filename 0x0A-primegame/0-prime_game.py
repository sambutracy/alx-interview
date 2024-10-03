#!/usr/bin/python3
"""
Maria and Ben Game: Prime Number Selection Game
"""

def isWinner(x, nums):
    """
    Determines the winner after x rounds of the game.

    Args:
    x : int : number of rounds
    nums : list : list of integers representing n in each round

    Returns:
    str : Name of the player with the most wins ("Maria" or "Ben").
          None if there's a tie.
    """

    # Sieve of Eratosthenes to compute primes up to the largest number in nums
    def sieve(n):
        # Create an array to mark prime numbers
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        # Mark multiples of each prime starting from 2
        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
        
        return is_prime

    # Precompute primes up to the largest number in nums
    max_n = max(nums)
    prime_flags = sieve(max_n)

    maria_wins = 0  # Count Maria's wins
    ben_wins = 0    # Count Ben's wins

    # Process each round
    for n in nums:
        # Initialize list of available primes in the current round
        primes_left = []
        for num in range(2, n + 1):
            if prime_flags[num]:
                primes_left.append(num)

        # Maria starts first
        turn = 0  # 0 for Maria, 1 for Ben

        # Play the game until no primes are left
        while primes_left:
            # Maria or Ben picks the smallest available prime
            chosen_prime = primes_left[0]

            # Remove the chosen prime and all of its multiples from primes_left
            primes_left = [prime for prime in primes_left if prime % chosen_prime != 0]

            # Switch turns between Maria (0) and Ben (1)
            turn = 1 - turn

        # If turn is 0 after the loop, Ben made the last move, so Maria lost
        if turn == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine overall winner based on win counts
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # It's a tie
