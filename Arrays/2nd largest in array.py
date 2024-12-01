def print2largest(self, arr):
    n = len(arr)
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(0, n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    return second_largest if second_largest != float("-inf") else -1
