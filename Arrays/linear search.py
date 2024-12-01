def searchInSorted(self, arr, N, K):
    n = len(arr)
    for i in range(0, N):
        if arr[i] == K:
            return 1

    return -1
