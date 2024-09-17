# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

#Problem Link: https://leetcode.com/problems/divide-two-integers/description/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        
        dvd = abs(dividend)
        dvs = abs(divisor)
        ans = 0
        
        while dvd >= dvs:
            k = 1
            while k * 2 * dvs <= dvd:
                k <<= 1
            dvd -= k * dvs
            ans += k
        
        return sign * ans
