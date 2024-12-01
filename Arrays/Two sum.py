def twoSum(self, arr, target):
    n = len(arr)
    dic = {}
    for i in range(0, n):
        rem = target - arr[i]
        if rem in dic:
            return True
        dic[arr[i]] = i
    return False
