def count(self, arr, n, x):
    cnt = 0
    for i in range(n):
        if arr[i] == x:
            cnt += 1
    return cnt
