def rotate(self, arr):
    n = len(arr)
    k = 1 % n
    arr[:] = arr[n - k :] + arr[: n - k]
    return arr
