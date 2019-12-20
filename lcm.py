# Uses python3
import sys
import random
import time

# Problem description
# Input -> a, b are two positive integers; 1 ≤ a,b ≤ 10^7
# Output -> LCM(a,b)

# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#     return a*b

def lcm_fast(a, b):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    return a * b // gcd(a,b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_fast(a, b))

    #############
    # Stress test
    #############
    # start, end = 1, 10**7
    # while True:
    #     a, b = [random.randint(start, end) for _ in range(2)]

    #     # naive = lcm_naive(a, b)
    #     t0 = time.time()
    #     fast = lcm_fast(a, b)
    #     t1 = time.time()
    #     diff = t1 - t0

    #     if diff <= 5:
    #         print(f"a: {a}, b: {b}")
    #         print(f"LCM(a,b): {fast}")
    #         print(f"It takes {diff} seconds.")
    #     else:
    #         print(f"a: {a}, b: {b}")
    #         print(f"LCM(a,b): {fast}")
    #         print(f"It takes more than 5 seconds.")
    #         break
