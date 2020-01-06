from typing import Sequence


def merge_sort(seq: Sequence) -> Sequence:

    if len(seq) == 1:
        return seq

    m = len(seq) // 2
    left = merge_sort(seq[:m])
    right = merge_sort(seq[m:])

    ans = merge(left, right)
    
    return ans


def merge(left: Sequence, right: Sequence) -> Sequence:
    print(f"{left=}, {right=}")

    d = []
    while left and right:
        b = left[0]
        c = right[0]

        if b <= c:
            d.append(left.pop(0))
        else:
            d.append(right.pop(0))
    d += left + right

    return d


print(merge_sort([7,2,5,3,7,13,1,6,9]))