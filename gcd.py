# Uses python3
import sys
import random
import time

# Problem description
# Input -> a, b are non-begative integers and both are not equal to zero.
# 1 ≤ a, b ≤ 2*10^9
# output -> the greatest common divisor of a and b


# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd


# Efficient algorithm: Euclidean algorithm
def gcd_fast(a, b):
    if b == 0:
        return a
    else:
        return gcd_fast(b, a % b)


if __name__ == "__main__":
    a, b = tuple(map(int, input().split()))
    print(gcd_fast(a, b))

    #############
    # Stress test
    #############
    # start, end = (1, 2_000_000_000)
    #
    # while True:
    #     a, b = [random.randint(start, end) for _ in range(2)]
    #     # naive = gcd_naive(a,b)
    #     t0 = time.time()
    #     fast = gcd_fast(a,b)
    #     t1 = time.time()
    #     diff = t1 - t0
    
    #     if diff <= 5:
    #         print(f"a: {a}, b: {b}") 
    #         print(f"gcd(a,b): {fast}")
    #         print(f"It takes {diff} seconds.")
    #     else:
    #         print(f"a: {a}, b: {b}") 
    #         print(f"gcd(a,b): {fast}")
    #         print("It takes a long time than 5 seconds.")
    #         break
        

    
