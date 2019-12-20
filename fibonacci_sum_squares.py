# Uses python3
import sys
import random
import time

# Problem description
# Input: n is an integer; 0 ≤ n ≤ 10**14
# Output: The last digit of F0^2 + F1^2 + ... + Fn^2

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares_fast(n):

    periodic_squared_last_digits = get_fibonacci_squared_last_digits()
    pisano_period = len(periodic_squared_last_digits)
    modulo = n % pisano_period
    return sum(periodic_squared_last_digits[:modulo+1]) % 10


def get_fibonacci_squared_last_digits(n=29): # period is 60
    periodic_squared_list = []
    periodic_list = []
    for i in range(n+1):
        if i <= 1:
            periodic_list.append(i)
            periodic_squared_list.append(i**2)
        else:
            last_digit = (periodic_list[i-2] + periodic_list[i-1]) % 10
            periodic_list.append(last_digit)
            periodic_squared_list.append((last_digit**2) % 10)
    return periodic_squared_list


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_fast(n))

    ################################################################################################
    # Stress test1: check if correct answers on the fast algorithm in a comparison to the naive one.
    ################################################################################################
    # start, end = 0, 10000

    # while True:

    #     n = random.randint(start, end)
    #     print(n)
    #     naive = fibonacci_sum_squares_naive(n)
    #     fast = fibonacci_sum_squares_fast(n)

    #     if naive != fast:
    #         print(f"Wrong answer. Naive vs. Fast = {naive} vs. {fast}")
    #         break
    #     else:
    #         print(f"OK")
    

    ################################################################################################
    # Stress test2: speed test
    ################################################################################################
    # start, end = 0, 10**14

    # while True:

    #     n = random.randint(start, end)
    #     print(n)
    #     t0 = time.time()
    #     fast = fibonacci_sum_squares_fast(n)
    #     t1 = time.time()
    #     tdiff = t1 - t0

    #     if tdiff < 5:
    #         print(f"It takes {tdiff} seconds.")
    #     else:
    #         print("It takes more than 5 seconds.")
