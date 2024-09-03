#!/usr/bin/python3
"""
prime game for alx-interview
"""


def isWinner(x, nums):
    """
    function to check for the winner
    """

    if x <= 0 or not nums:
        return None

    max_n = max(nums)

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = 0
        for prime in primes:
            if prime > n:
                break
            if sieve[prime]:
                prime_count += 1

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
