def getFloorAndCeil(self, x: int, arr: list) -> list:
    arr.sort()
    n = len(arr)
    low = 0
    high = n - 1
    floor = -1
    ceil = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return x, x
        elif arr[mid] > x:
            ceil = arr[mid]
            high = mid - 1
        else:
            floor = arr[mid]
            low = mid + 1
    return floor, ceil
