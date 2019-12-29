from typing import Sequence
import random


def recursive_linear_search(input_list: Sequence, low: int, high: int, key: int):

    if high < low:
        return "Not Found."
    if input_list[low] == key:
        return f"Found. The index is {low}."
    
    return recursive_linear_search(input_list, low + 1, high, key)


def iterative_linear_search(input_list, key):

    for i, element in enumerate(input_list):
        if element == key:
            return f"Found. The index is {i}."
    
    return "Not Found."


# Run
INPUT = [random.randint(1, 100) for _ in range(100)]
KEY=random.randint(1, 100)

r = recursive_linear_search(INPUT, 0, len(INPUT) - 1, KEY )
i = iterative_linear_search(INPUT, KEY)

print(r)
print(i)

