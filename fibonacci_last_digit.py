# Uses python3
import sys
import random
import time

# Problem description
# input n: a single integer; 0 ≤ n ≤ 10^7
# output: the last digit of a Fibonacci number Fn


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % 10


# Efficient algorithm on speed and memory
def get_fibonacci_last_digit_fast1(n):
    l = []
    for i in range(n+1):
        if i <= 1:
            l.append(i)
        else:
            l[0], l[1] = l[1] % 10, (l[0] + l[1]) % 10

    return l[1] % 10


def get_fibonacci_last_digit_fast2(n):
    periodic_list = get_fibonacci_last_digits()
    pisano_period = len(periodic_list)
    modulo = n % pisano_period
    return periodic_list[modulo]


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
    print(get_fibonacci_last_digit_fast2(n))


    ##############
    # Stress test
    ##############
    # start, end = 0, 10_000_000
    
    # while True:
    #     n = random.randint(start, end)
    #     print(n)
    #     fast1 = get_fibonacci_last_digit_fast1(n)
    #     fast2 = get_fibonacci_last_digit_fast2(n)
    #     if fast1 != fast2:
    #         print("Wrong answer")
    #         break
    #     else:
    #         print("OK")

    ##############
    # Stress test2: speed test with new algorithm (_fast2)
    ##############
    # start, end = 0, 10_000_000
    
    # while True:
    #     n = random.randint(start, end)
    #     print(n)
    #     t0 = time.time()
    #     fast2 = get_fibonacci_last_digit_fast1(n)
    #     t1 = time.time()
    #     tdiff = t1 - t0

    #     if tdiff < 5:
    #         print(f"It takes {tdiff} seconds.")
    #     else:
    #         print("It takes more than 5 seconds.")
