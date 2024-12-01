import math


class Solution:
    def lcmAndGcd(self, A, B):
        x = math.gcd(A, B)
        return [abs(A * B) // x, x]
