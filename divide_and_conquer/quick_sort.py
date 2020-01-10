from typing import Sequence
import random


def quick_sort(arr: Sequence, left: int, right: int) -> Sequence:
    if left >= right:
        return
    
    m = partition(arr, left, right)
    quick_sort(arr, left, m - 1)
    quick_sort(arr, m + 1, right)

    return arr


def random_quick_sort(arr: Sequence, left: int, right: int) -> Sequence:
    if left >= right:
        return
    # Randomize the position of the pivot
    k = random.randint(left, right)
    arr[left], arr[k] = arr[k], arr[left]

    m = partition(arr, left, right)
    quick_sort(arr, left, m - 1)
    quick_sort(arr, m + 1, right)

    return arr


def partition(arr: Sequence, left: int, right: int) -> int:
    '''Return the final position of the first element in the array'''
    # pivot = arr[left]
    # l = [number for number in arr[left + 1:right + 1] if number <= pivot]
    # r = [number for number in arr[left + 1:right + 1] if number > pivot]
    # arr = l + [pivot] + r
    # print(arr)
    # return len(l)

    pivot = arr[left]
    j = left

    for i in range(left + 1, right + 1):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    
    arr[left], arr[j] = arr[j], arr[left]
    return j


A = [0, 1, 4, 2, 3, 9, 8, 9, 4, 7, 6, 6]
random.shuffle(A)
print(random_quick_sort(A, 0, len(A) - 1))