# Using the greedy algorithm to fill in a knapsack
# that has a limited capacity to have a maximum value.

# Possible steps for algorithm:
# 1. Find an item with the maximum value per unit
# 2. Fill the knapsack with the item as much as it allows
# 3. If there is still a room in the knapsack, find the next maximum item and fill the sack.
# 4. repeat step 3 until the sack is fully filled.

from typing import List, Tuple

# Naive algorithm
def filling_the_sack(items: List[Tuple[int, int]], capacity_of_sack) -> int:
    # In a tuple, the first element is the weight of item and the second is the price.
    sack = []
    total_value = 0
    for weight, price in sorted(items, key=lambda x: x[1] / x[0], reverse=True):
        if sum(sack) < capacity_of_sack:
            if sum(sack) + weight < capacity_of_sack:
                total_value += price
                sack.append(weight)
            else:
                total_value += price / (capacity_of_sack - sum(sack))
                sack.append(capacity_of_sack - sum(sack))
        else:
            break

    return total_value


# Similar, but improved by thinking in the opposite way
def filling_the_sack2(items: List[Tuple[int, int]], capacity_of_sack) -> int:
    # In a tuple, the first element is the weight of item and the second is the price.
    sack = []
    total_value = 0
    remaining_capacity = capacity_of_sack
    for weight, price in sorted(items, key=lambda x: x[1] / x[0], reverse=True):
        if remaining_capacity == 0:
            return total_value, sack

        amount = min(weight, remaining_capacity)
        total_value += amount * (price / weight)

        sack.append(amount)
        remaining_capacity -= amount
    
    return total_value, sack




