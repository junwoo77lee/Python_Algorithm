from typing import List
import random
import time


# The binary search outperforms the ternary search.
def recursive_binary_search(input_list: List, low: int, high: int, key: int) -> int:
    ''' Return an index that key is matched at '''
    # base case: if not found
    if high < low:
        return low - 1
    
    mid = low + (high - low) // 2

    if key == input_list[mid]:
        return mid
    elif key < input_list[mid]:
        return recursive_binary_search(input_list, low, mid - 1, key)
    else: # key > input_list[mid]
        return recursive_binary_search(input_list, mid + 1, high, key)


# The iterative binary search little bit outperforms the recursive version of binary search
def iterative_binary_search(input_list: List, low: int, high: int, key: int) -> int:

    while low <= high:

        mid = low + (high - low) // 2
        
        if key == input_list[mid]:
            return mid
        elif key < input_list[mid]:
            high = mid - 1
        else: # key > input_list[mid]
            low = mid + 1

    return low - 1


def recursive_ternary_search(input_list: List, low: int, high: int, key: int) -> int:
    ''' Return an index that key is matched at '''

    if high < low:
        return low - 1
    
    mid1 = low + (high - low) // 3
    mid2 = mid1 + (high - low) // 3

    if key == input_list[mid1]:
        return mid1
    elif key == input_list[mid2]:
        return mid2
    elif key < input_list[mid1]:
        return recursive_ternary_search(input_list, low, mid1 - 1, key)
    elif key > input_list[mid1]:
        return recursive_ternary_search(input_list, mid1 + 1, mid1 + (mid2 - mid1) // 2 + 1, key)
    elif key < input_list[mid2]:
        return recursive_ternary_search(input_list, mid1 + (mid2 - mid1) // 2 - 1, mid2 - 1, key)
    else: # key > input_list[mid2]:
        return recursive_ternary_search(input_list, mid2 + 1, high, key)


# Run
INPUT = sorted([random.randint(1, 10000) for _ in range(10000)])
KEY = random.randint(1, 10000)

t0 = time.time()
rbinary = recursive_binary_search(INPUT, 0, len(INPUT) - 1, KEY)
t1 = time.time()
tdiff_rbinary = t1 - t0

t0 = time.time()
ibinary = iterative_binary_search(INPUT, 0, len(INPUT) - 1, KEY)
t1 = time.time()
tdiff_ibinary = t1 - t0

# t0 = time.time()
# ternary = recursive_ternary_search(INPUT, 0, len(INPUT) - 1, KEY)
# t1 = time.time()
# tdiff_ternary = t1 - t0

print(f"Answer: rBinary vs. iBinary = {rbinary} vs. {ibinary}.")
print(f"Time: rBinary vs. iBinary = {tdiff_rbinary} vs. {tdiff_ibinary}.")
    


