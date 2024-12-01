def factorialNumbers(self, n):
    ans = []
    i = 1
    fact = 1
    while fact <= n:
        ans.append(fact)
        i += 1
        fact *= i

    return ans
