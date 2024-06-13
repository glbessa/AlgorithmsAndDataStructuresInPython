from typing import List, Callable

def selection_sort(arr: List, key: Callable = lambda x: x, reverse: bool = False) -> None:
    n = len(arr)
    for i in range(n):
        trg_idx = i
        for j in range(i + 1, n):
            if not reverse:
                if key(arr[j]) < key(arr[trg_idx]):
                    trg_idx = j
            else:
                if key(arr[j]) > key(arr[trg_idx]):
                    trg_idx = j
            
        arr[i], arr[trg_idx] = arr[trg_idx], arr[i]
    
if __name__ == "__main__":
    arr = [1,3,2,4,6,7,8,5]
    selection_sort(arr)
    print(arr)
