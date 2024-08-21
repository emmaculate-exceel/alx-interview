#!/usr/bin/python3
"""making changes to file using python
"""


def makeChange(coins, total):
    """ coins and it's sum
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    coins = [1, 2, 3]
    total = 11
    print(makeChange(coins, total))
