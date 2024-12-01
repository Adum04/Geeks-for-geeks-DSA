def frequencyCount(self, arr, N, P):
    length = len(arr)
    hash_map = [0] * N
    for i in range(0, N):
        if 1 <= arr[i] <= N:
            hash_map[arr[i] - 1] += 1
    for i in range(N):
        arr[i] = hash_map[i]

    return hash_map
