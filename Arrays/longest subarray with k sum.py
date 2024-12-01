def lenOfLongestSubarr(self, arr, k):
    count = 0
    sum = 0
    map = {}
    for i in range(len(arr)):
        sum += arr[i]
        if sum == k:
            count = i + 1
        if sum - k in map:
            count = max(count, i - map.get(sum - k))
        if sum not in map:
            map[sum] = i
    return count
