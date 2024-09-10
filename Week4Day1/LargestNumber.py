# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

# Problem Link: https://leetcode.com/problems/largest-number/description/

from functools import cmp_to_key

def compare(x: str, y: str) -> int:
    return (y + x > x + y) - (y + x < x + y)

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        return ''.join(sorted(map(str, nums), key=cmp_to_key(compare))).lstrip('0') or '0'
