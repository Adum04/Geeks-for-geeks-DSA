def leaders(self, n, arr):
    leader = []
    max_right = arr[n - 1]
    leader.append(max_right)
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_right:
            leader.append(arr[i])
            max_right = arr[i]
    return leader[::-1]
