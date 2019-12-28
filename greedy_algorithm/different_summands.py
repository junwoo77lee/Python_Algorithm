# Uses python3
import sys
import random
import time

# Objective: To represent a given positive integer 𝑛 as a sum of as many pairwise distinct positive integers as possible.
#            That is, to find the maximum 𝑘 such that 𝑛 can be written as 𝑎1+𝑎2+···+𝑎𝑘 where 𝑎1,...,𝑎𝑘 are positive integers
#            and 𝑎𝑖 ≠ 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.
# Input: n is a single integer
# Constraints: 1 ≤ n ≤ 10^9
# Output: The maximum number 𝑘 such that 𝑛 can be represented as a sum of 𝑘 pairwise distinct positive integers.
#         And 𝑘 pairwise distinct positive integers that sum up to 𝑛


def optimal_summands_naive(n):
    summands = []
    
    number = 1
    while sum(summands) != n:
        if (number not in summands)\
          and (n - (sum(summands) + number) not in summands)\
          and (n - (sum(summands) + number) != number):
            summands.append(number)
        else:
            last_number = n - sum(summands)
            summands.append(last_number)
            break

        number += 1

    return summands


# Efficient algorithm
def optimal_summands_fast(n):
    summands = []
    
    number = 1
    total = 0
    while (total != n)\
           and (n - (total + number) not in range(1, number + 1))\
            and (n - (total + number) != number):
        total += number
        number += 1

    summands += range(1, number)
    last_number = n - sum(summands)

    if not last_number == 0:
        summands.append(last_number)

    return summands


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    summands = optimal_summands_fast(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

    
