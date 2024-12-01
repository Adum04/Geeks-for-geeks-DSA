def kthSmallest(self, arr, k):
    sorted_array = sorted(arr)
    return sorted_array[k - 1]
