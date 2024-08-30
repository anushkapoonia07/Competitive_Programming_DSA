# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Problem Link: https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        while n > 0:
            if n % 2 == 1: 
                result *= x
            x *= x
            n //= 2
        
        return result
