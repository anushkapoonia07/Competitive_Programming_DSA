# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Problem Link: https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2  
        return total_sum - sum(nums)   
