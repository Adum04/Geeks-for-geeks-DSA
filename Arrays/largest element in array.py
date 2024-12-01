def largest(self, n: int, arr: List[int]) -> int:
    n = arr[0]
    for i in arr:
        if i > n:
            n = i

    return n
