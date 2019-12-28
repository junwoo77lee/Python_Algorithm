# Uses python3
import sys
import random
import time

# Objective: To implement an algorithm for the fractional knapsack problem.
# Input: The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
#        The next 𝑛 lines define the values and weights of the items.
#        The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the value and the weight of 𝑖-th item, respectively.
# Constraints: 1 ≤ 𝑛 ≤ 10^3, 0 ≤ 𝑊 ≤ 2·10^6; 0 ≤ 𝑣𝑖 ≤ 2·10^6, 0< 𝑤𝑖 ≤ 2·10^6 for all 1 ≤ 𝑖 ≤ 𝑛.
#              All the numbers are integers.
# Output: The maximal value of fractions of items that fit into the knapsack. (four digits after the decimal point)


def get_optimal_value(capacity, weights, values):
    value = 0.
    
    sorted_items = sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True)
    remaining = capacity
    for w, v in sorted_items:
        if remaining == 0:
            return value
        
        amount = min(w, remaining)
        value += amount * (v / w)
        remaining -= amount
    
    return value
        

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))


    ##############
    # Stress test
    ##############
    # while True:
    #     n = random.randint(1, 10**3)
    #     capacity = random.randint(0, 2*10**6)
    #     values = [ random.randint(0, 2*10**6) for _ in range(n) ]
    #     weights = [ random.randint(1, 2*10**6) for _ in range(n) ]

    #     t0 = time.time()
    #     opt_value = get_optimal_value(capacity, weights, values)
    #     t1 = time.time()
    #     tdiff = t1 - t0

    #     if tdiff < 5:
    #         print(f"n: {n}, capacity: {capacity}")
    #         print(f"Optimum value: {opt_value}")
    #         print(f"It took {tdiff} seconds.")
    #     else:
    #         print(f"n: {n}, capacity: {capacity}")
    #         print(f"Optimum value: {opt_value}")
    #         print(f"It took more than 5 seconds.")
    #         break



