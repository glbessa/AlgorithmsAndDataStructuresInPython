import math
from typing import Callable, List

def reverse(arr: List, start: int, end: int) -> None:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate(arr: List, start: int, end: int, amount: int) -> None:
    n = end - start + 1
    amount = amount % n
    if amount == 0:
        return
    
    reverse(arr, start, end - amount)
    reverse(arr, end - amount + 1, end)
    reverse(arr, start, end)

def floor_power_of_two(n: int) -> int:
    return 2 ** int(math.log2(n))

def merge(arr: List, left: int, mid: int, right: int):
    left_arr = arr[left:mid]
    right_arr = arr[mid:right]

    i = j = 0
    k = left
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

def insertion_sort(arr: List, start: int, end: int, key: Callable = lambda x: x, reverse: bool = False) -> None:
    for i in range(start + 1, end):
        j = i
        while j > start and key(arr[j - 1]) > key(arr[j]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def block_sort(arr: List, 
               block_size: int = 16, 
               key: Callable = lambda x: x, 
               reverse: bool = False):
    n = len(arr)
    pw2 = floor_power_of_two(n)
    scale = n / pw2
    denominator = pw2 / block_size
    numerator_step = n % denominator
    integer_step = int(n / denominator)

    for merge_index in range(0, n, block_size):
        start = merge_index
        end = merge_index + block_size
        print(arr[start:end])
        insertion_sort(arr, start, end, key, reverse)
        print(arr[start:end])

    while integer_step < n:
        integer_part = 0
        numerator = 0
        while integer_part < n:
            start = integer_part
            integer_part += integer_step
            numerator += numerator_step
            if numerator >= denominator:
                numerator -= denominator
                integer_part += 1
           
            mid = integer_part
           
            integer_part += integer_step
            numerator += numerator_step
            if numerator >= denominator:
                numerator -= denominator
                integer_part += 1
        
            end = integer_part
        
            print(start, mid, end)

            if arr[end - 1] < arr[start]:
                rotate(arr, start, end, end - start)
            elif arr[mid - 1] > arr[mid]:
                merge(arr, start, mid, end)

            print(arr)

        integer_step += integer_step
        numerator_step += numerator_step
        if numerator_step >= denominator:
            numerator_step -= denominator
            integer_step += 1

if __name__ == '__main__':
    arr = [5, 3, 2, 4, 1, 6]
    block_sort(arr, 3)
    print(arr)