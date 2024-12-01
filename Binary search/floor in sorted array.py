def findFloor(self, A, N, X):
    low = 0
    high = N - 1
    lower = -1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] <= X:
            lower = mid
            low = mid + 1
        else:
            high = mid - 1
    return lower
