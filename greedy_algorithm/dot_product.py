#Uses python3

import sys
import random
import time

# Objective: Given two sequences 𝑎1,𝑎2,...,𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad)
#            and 𝑏1,𝑏2,...,𝑏𝑛 (𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot),
#            we need to partition them into 𝑛 pairs (𝑎𝑖,𝑏𝑗) such that the sum of their products is maximized.
# Inputs: The first line contains an integer 𝑛,
#         the second one contains a sequence of integers 𝑎1,𝑎2,...,𝑎𝑛,
#         the third one contains a sequence of integers 𝑏1,𝑏2,...,𝑏𝑛
# Constraints: 1 ≤ 𝑛 ≤ 10^3; −10^5 ≤ 𝑎𝑖, 𝑏𝑖 ≤ 10^5 for all 1 ≤ 𝑖 ≤ 𝑛
# Output: The maximum total revenue


def max_dot_product(a, b):

    a, b = sorted(a, reverse=True), sorted(b, reverse=True)

    maximum_revenue = sum(profit * num_click for profit, num_click in zip(a, b))
   
    return maximum_revenue


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

    #############
    # Stress test
    #############
    # while True:

    #     n = random.randint(1, 10**3)
    #     a = [random.randint(-10**5, 10**5) for _ in range(n)]
    #     b = [random.randint(-10**5, 10**5) for _ in range(n)]
    #     print(f"n: {n}")
    #     print(f"a: {a}")
    #     print(f"b: {b}")
        
    #     t0 = time.time()
    #     ans = max_dot_product(a, b)
    #     t1 = time.time()
    #     tdiff = t1 - t0


    #     if tdiff < 5:
    #         print(f"The maximum profit: {ans}")
    #         print(f"It takes {tdiff} seconds.")
    #     else:
    #         print(f"The maximum profit: {ans}")
    #         print(f"It takes more than 5 seconds.")
    #         break
