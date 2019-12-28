# Uses python3
import random

# Find the minimum number of coins needed to change the input value (an integer)
# into coins with denominations 1, 5, and 10.

# Input: m is an integer; 1 ≤ m ≤ 10^3
# Output: The minimum number of coins with denominations 1, 5, and 10 that changes m


def get_change(m):
    # return the minimum number of coins (1, 5, and 10) that changes m
    # Using the greedy algorithm:
    # 0. While m is True (> 0)
    # 1. Check if m // 10 > 0. If yes, count it as for 10 and subtract the amount from the current m.
    # 2. Then, check if m // 5 > 0. If yes, count it for 5 and subtract the amount from the current m.
    # 3. Then, check if m // 1 > 0. If yes, count it for 1 and subtract the amount from the current m.

    coins = {}
    while m:
        if m // 10 > 0:
            coins[10] = m // 10
            m -= (m // 10) * 10
        elif m // 5 > 0:
            coins[5] = m // 5
            m -= (m // 5) * 5
        elif m // 1 > 0:
            coins[1] = m // 1
            m -= m // 1

    return sum(coins.values())


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
