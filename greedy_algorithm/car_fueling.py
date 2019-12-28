# python3
import sys
import random
import time

# Objective: Find the minimum number of refills needed for your trip
# Input: The first line contains an integer 𝑑.
#        The second line contains an integer 𝑚.
#        The third line specifies an integer 𝑛.
#        Finally, the last line contains integers stop1, stop2, . . . , stop𝑛.
# Constraints: 1 ≤ 𝑑 ≤ 10^5, 1 ≤ 𝑚 ≤ 400, 1 ≤ 𝑛 ≤ 300, 0 < stop1 < stop2 < ··· < stop𝑛 < 𝑑
# Output: The minimum number of refills, If it's not possible to reach the destination, output -1


def compute_min_refills_eff(distance, tank, stops):
    # Using the greedy algorithm: Go as much as you can

    stops = [0] + stops + [distance]
    num_refills = 0
    number_of_stops = len(stops) - 2
    current_refill = 0   # index

    while current_refill <= number_of_stops:
        last_refill = current_refill

        while (current_refill <= number_of_stops) and (stops[current_refill + 1] - stops[last_refill] <= tank):
            current_refill += 1
        
        if current_refill == last_refill:
            return -1
        if current_refill <= number_of_stops:
            num_refills += 1

    return num_refills


# def compute_min_refills_naive(distance, tank, stops):

#     stops = [0] + stops + [distance]
#     current_d = 0
#     number_of_stops = len(stops) - 2
#     index = 0
#     refills = 0
#     while current_d + tank < distance:
#         if (stops[index] - current_d > tank):
#             return -1

#         ruler = tank + current_d
#         while index <= number_of_stops:
#             if stops[index] <= ruler:
#                 index += 1
#             else:
#                 break
#         current_d = stops[index - 1]
#         refills += 1

#     return refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills_eff(d, m, stops))


    #############
    # Stress test
    #############
    # while True:
    #     d = random.randint(1, 10**5)
    #     m = random.randint(1, 400)
    #     n = random.randint(1, 300)

    #     stops = []
    #     for i, _ in enumerate(range(n)):
    #         if i > 0:
    #             stops.append(random.randint(stops[i - 1], d))
    #         else:
    #             stops.append(random.randint(0, d))
    #     stops = sorted(list(set(stops)))
    #     print(f"distance: {d}, tank: {m}, stops: {stops}")

    #     naive = compute_min_refills_naive(d, m, stops)
    #     eff = compute_min_refills_eff(d, m, stops)

    #     if naive != eff:
    #         # print(f"distance: {d}, tank: {m}, stops: {stops}")
    #         print(f"Wrong answer: Naive vs. Eff = {naive} vs. {eff}")
    #         break
    #     else:
    #         # print(f"distance: {d}, tank: {m}, stops: {stops}")
    #         print('OK')



        

