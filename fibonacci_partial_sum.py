# Uses python3
import sys
import random
import time


# Problem description
# Input: n, m are integers; 0 ≤ m ≤ n ≤ 10**14
# Output: The last digits of Fm + Fm+1 + ... + Fn


# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0

#     current = 0
#     next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             sum += current

#         current, next = next, current + next

#     return sum % 10


# Efficient algorithm
def fibonacci_partial_sum_fast(from_, to):
    # period: 60 digits
    # 0-59, 60-119, 120-179, ...
    # where is the "from_" based on the period?
    #   -> start index of the first_part: from_ - (from_ // period) * period
    # where is the "to" based on the period?
    #   -> start index of the second_part: to - (to // period) * period
    periodic_last_digits = get_fibonacci_last_digits()
    period = len(periodic_last_digits)

    start_index = from_ - (from_ // period) * period
    end_index = to - (to // period) * period

    if (from_ // period) == 0 and (to // period) == 0:
        sum_range = periodic_last_digits[start_index:end_index+1]
    else:
        first_edge = periodic_last_digits[start_index:]
        second_edge = periodic_last_digits[:end_index + 1] # to be included
        # print(f"Start index: {start_index}, First: {first_edge}")
        # print(f"End index: {end_index}, Second: {second_edge}")
        sum_range = first_edge + second_edge

    return sum(sum_range) % 10


def get_fibonacci_last_digits(n=59): # period is 60
    periodic_list = []
    for i in range(n+1):
        if i <= 1:
            periodic_list.append(i)
        else:
            periodic_list.append((periodic_list[i-2] + periodic_list[i-1]) % 10)
    return periodic_list


if __name__ == '__main__':
    from_, to = tuple(map(int, input().split()))
    print(fibonacci_partial_sum_fast(from_, to))

    ##############################################################################
    # Stress test1: check if a correct answer comes out for the fast algorithm 
    ##############################################################################
    # start, end = 0, 100000
    # while True:

    #     m, n = random.randint(start, end), random.randint(start, end)
    #     while n < m:
    #         m, n = random.randint(start, end), random.randint(start, end)
        
    #     print(f"m: {m}, n: {n}")
    #     assert n >= m
    #     naive = fibonacci_partial_sum_naive(m, n)
    #     fast = fibonacci_partial_sum_fast(m, n)

    #     if naive != fast:
    #         print(f"Wrong answer. Naive vs. Fast = {naive} vs. {fast}")
    #         break
    #     else:
    #         print("OK")

    ##############################################################################
    # Stress test2: speed test 
    ##############################################################################
    # start, end = 0, 10**14
    # while True:

    #     m, n = random.randint(start, end), random.randint(start, end)
    #     while n < m:
    #         m, n = random.randint(start, end), random.randint(start, end)
        
    #     print(f"m: {m}, n: {n}")
    #     assert n >= m
    #     t0 = time.time()
    #     fast = fibonacci_partial_sum_fast(m, n)
    #     t1 = time.time()
    #     tdiff = t1 - t0

    #     if tdiff < 5:
    #         print(f"It takes {tdiff} seconds.")
    #     else:
    #         print("It takes more than 5 seconds.")
    #         break    
        