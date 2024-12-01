def sumOfDivisors(self, N):
    if N < 0:
        return 0
    result = 0
    for i in range(1, N + 1):
        result += i * (N // i)
    return result
