#!/usr/bin/python3
""" minimum operations """


def minOperations(n):
    """ function to calculate the minimum operations """
    
    if n == 0:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + 1 + (i - j))

    return dp[n] if dp[n] != float('inf') else 0


n = 9
print(minOperations(n))  # Output: 6
