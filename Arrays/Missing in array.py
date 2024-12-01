def missingNumber(self, n, arr):
    lst = {}
    for i in range(1, n + 1):
        lst[i] = 0
    for i in arr:
        lst[i] += 1
    for k, v in lst.items():
        if v == 0:
            return k
