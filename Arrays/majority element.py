def majorityElement(self, arr):
    n = len(arr)
    dic = {}
    mid = n // 2
    for i in range(0, n):
        dic[arr[i]] = 0
    for i in arr:
        dic[i] += 1
    for k, v in dic.items():
        if v > mid:
            return k
    return -1
