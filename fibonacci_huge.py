# Uses python3
import sys
import random
import time

# Problem description
# Input -> n is a single integer and m is a divisor for Fn; 1 ≤ n ≤ 10^14, 2 ≤ m ≤ 10^3
# Output -> Fn mod m

# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % m


# Efficient algorithm
def get_fibonacci_huge_fast(n, m):
    
    pisano_period = get_length(m)
    reduced_n = n % pisano_period
    reduced_fibo = get_fibonacci_list(reduced_n)[-1]

    return reduced_fibo % m


def get_length(m):
    fibo = get_fibonacci_list(5000) # use 5000 to calculate the pisano period for m=1000
    fibo_mod = [number % m for number in fibo]
    for i, p in enumerate(fibo_mod):
        if i > 3 and all([fibo_mod[i-2]==0, fibo_mod[i-1]==1, fibo_mod[i]==1]):
            pisano_period = i - 2
            break

    return pisano_period #print(fibo_mod) #len(fibo_cycles[1]) + 3


def get_fibonacci_list(n):
    l = []
    for i in range(n+1):
        if i <= 1:
            l.append(i)
        else:
            l.append(l[i-1] + l[i-2])
    return l


if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))
    print(get_fibonacci_huge_fast(n, m))

    #############
    # Stress test
    #############
    # while True:
    #     n, m  = tuple([random.randint(1, 10**14), random.randint(2, 10**3)])
    #     print(f"n: {n}, m: {m}")
    #     t0 = time.time()
    #     fast = get_fibonacci_huge_fast(n, m)
    #     t1 = time.time()
    #     tdiff = t1 - t0

    #     if tdiff <= 5:
    #         print(f"F{n} mod {m}: {fast}")
    #         print(f"It takes {tdiff} seconds.")
    #     else:
    #         print(f"F{n} mod {m}: {fast}")
    #         print(f"It takes more then 5 seconds.")
