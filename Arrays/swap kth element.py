def swapKth(self, k, arr):
    n = len(arr)
    arr[k - 1], arr[n - k] = arr[n - k], arr[k - 1]
    return arr