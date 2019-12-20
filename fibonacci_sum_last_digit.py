# Uses python3
import sys
import time
import random


# Problem description
# Input: n is a single integer; 1 ≤ n ≤ 10**14
# Output: the last digit of F0 + F1 + ... + Fn

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current
#     return sum % 10


# Efficient algorithm
def fibonacci_sum_fast(n):
    periodic_last_digits = get_fibonacci_last_digits()
    # cycles = n // len(fibo_numbers)  # the last digit of sum(fibo_numbers) is always zero
    modulo = n % len(periodic_last_digits) + 1

    return sum(periodic_last_digits[:modulo]) % 10


def get_fibonacci_last_digits(n=59): # period is 60
    periodic_list = []
    for i in range(n+1):
        if i <= 1:
            periodic_list.append(i)
        else:
            periodic_list.append((periodic_list[i-2] + periodic_list[i-1]) % 10)
    return periodic_list


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_fast(n))

    # To find period across the last digit of all the fibonacci numbers
    # for _ in range(n):
    #     fast = fibonacci_sum_fast(_)
    #     print(f"The last digit of F{_}: {fast}")

    #############
    # Stress test
    #############
    # while True:
    #     n = random.randint(0, 10**14)
    #     t0 = time.time()
    #     fast = fibonacci_sum_fast(n)
    #     t1 = time.time()
    #     tdiff = t1 - t0

    #     if tdiff < 5:
    #         print(f"n: {n}, the last digit of sum of Fnumbers: {fast}")
    #         print(f"It takes {tdiff} seconds.")
    #     else:
    #         print(f"n: {n}, the last digit of sum of Fnumbers: {fast}")
    #         print("It takes more than 5 seconds.")
