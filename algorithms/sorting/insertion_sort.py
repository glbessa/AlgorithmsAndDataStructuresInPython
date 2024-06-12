from typing import List, Callable

def insertion_sort(arr: List, key: Callable = lambda x: x, reverse: bool = False) -> None:
    n = len(arr)
    for i in range(0, n):
        j = i

        if not reverse:
            while j > 0 and key(arr[j - 1]) > key(arr[j]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
        else:
            while j > 0 and key(arr[j - 1]) < key(arr[j]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1