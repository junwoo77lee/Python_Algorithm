from typing import List, Sequence


def selection_sort(seq: Sequence) -> Sequence:
    # return a sorted sequence by using the selection sorting algorithm
    # find the minimum and assign it to the first element

    idx = 0
    while idx < len(seq):
        idxmin = 0
        for i, number in enumerate(seq[idx:]):
            if seq[idx + i] < seq[idx + idxmin]:
                idxmin = i
        seq[idx], seq[idx + idxmin] = seq[idx + idxmin], seq[idx]
        idx += 1
    
    return seq


print(selection_sort([2, 4, 8, 5, 2]))
print(selection_sort([8, 2, 8, 5, 2, 66, 23, 0]))
print(selection_sort([2, 5, 99, 4, 7, 8, 5, 1, 10]))

