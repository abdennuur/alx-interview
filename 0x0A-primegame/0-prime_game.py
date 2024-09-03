#!/usr/bin/python3
"""The Prime game module.
"""


def isWinner(x, nums):
    """ Determines winner of prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for ix, is_prime in enumerate(primes, 1):
        if ix == 1 or not is_prime:
            continue
        for ji in range(ix + ix, n + 1, ix):
            primes[ji - 1] = False
    # filter the nbr of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
