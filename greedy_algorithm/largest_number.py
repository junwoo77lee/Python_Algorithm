#Uses python3

import sys
import random
import time

# Objective: Compose the largest number out of a set of integers.
# Input: The first line of the input contains an integer 𝑛.
#        The second line contains integers 𝑎1,𝑎2,...,𝑎𝑛.
# Constraints: 1 ≤ 𝑛 ≤ 100; 1 ≤ 𝑎𝑖 ≤ 10^3 for all 1 ≤ 𝑖 ≤ 𝑛.
# Output: The largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.

def largest_number(a):
    
    ans = ''
    while a:
        max_num = 0

        for number in a:
            if is_greater_or_equal(number, max_num):
                max_num = number
        ans += str(max_num)
        a.remove(max_num)

    return ans
 

def is_greater_or_equal(num, max_num):
    # return a boolean value after checking which is greater
    return True if (str(num) + str(max_num)) >= (str(max_num) + str(num)) else False


    # The code below is an approach to do the similar (not 100%) thing.
    # Just leave it because it will remind me about the importance of thinking differently!

    # num_string = str(num)
    # max_num_string = str(max_num)

    # num_digits = len(num_string)
    # max_num_digits = len(max_num_string)

    # index = 0
    # while (index < num_digits and index < max_num_digits):
    #     if num_string[index] == max_num_string[index]:
    #         index += 1
    #     elif num_string[index] > max_num_string[index]:
    #         return True
    #     elif num_string[index] < max_num_string[index]:
    #         return False
    
    # if num_digits < max_num_digits:
    #     diff = max_num_digits - num_digits
    #     temp = index
    #     while temp <= diff:
    #         if num_string[index - 1] == max_num_string[temp]:
    #             temp += 1
    #         elif num_string[index - 1] > max_num_string[temp]:
    #             return True
    #         else:
    #             return False
    #     return True

    # elif num_digits > max_num_digits:
    #     diff = num_digits - max_num_digits
    #     temp = index
    #     while temp <= diff:
    #         if max_num_string[index - 1] == num_string[temp]:
    #             temp += 1
    #         elif max_num_string[index - 1] > num_string[temp]:
    #             return False
    #         else:
    #             return True
    #     return False


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))


    ##############
    # Stress test
    ##############
    # while True:
    #     n = random.randint(1, 100)
    #     data = [random.randint(1, 1000) for _ in range(n)]
    #     print(f"n: {n}")
    #     print(f"data: {data}")

    #     t0 = time.time()
    #     ans = largest_number(data)
    #     t1 = time.time()
    #     tdiff = t1 - t0

    #     if tdiff < 5:
    #         print(f"ans: {ans}")
    #         print(f"It took {tdiff} seconds.")
    #     else:
    #         print(f"ans: {ans}")
    #         print("It took more than 5 seconds.")
    #         break

