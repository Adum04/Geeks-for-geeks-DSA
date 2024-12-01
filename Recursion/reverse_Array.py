def reverseArray(self, arr):
    n = len(arr)
    low = 0
    high = n - 1
    mid = low + high // 2
    while low < mid + 1:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    return arr
