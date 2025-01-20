#!/usr/bin/python3
"""Determine the winner between Maria and Ben based on prime num"""


def get_primes_up_to(n):
    """
    Generate a list of prime numbers up to and including n.
    Returns: List of prime num up to n.
    """
    primes = []
    sieve = [True] * (n + 1)

    for u in range(2, n + 1):
        if sieve[u]:
            primes.append(u)
            for i in range(u, n + 1, u):
                sieve[i] = False

    return primes


def isWinner(x, nums):
    """
    Determine the winner of the prime game after x rounds,
    with different upper limits per round.
    Returns: The name of the player with the most wins ('Maria' or 'Ben').
    If the winner cannot be determined, returns None.
    """
    if not x or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in range(x):
        primes = get_primes_up_to(nums[n])

        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
