def binarysearch(self, arr, k):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return -1
