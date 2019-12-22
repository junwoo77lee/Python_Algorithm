# The smallest number of group for grouping childeren based on their age
# one group should not have age difference over than 1 year among children
import random

# Generate a random age set
ages = [round(random.uniform(3, 10), 1) for _ in range(1000)]
# print(ages)


def greedy_grouping_age(children, ydiff):
    
    children = sorted(children) # O(nlogn)
    # print(children)
    n = len(children)
    segments = []
    i = 0
    while i < n:
        l, r = children[i], children[i] + ydiff
        segments.append((l, r))

        i += 1
        while i < n and children[i] <= r:
            i += 1

    return len(segments), segments


if __name__ == '__main__':
    print(greedy_grouping_age(ages, 1))



