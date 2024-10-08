# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Problem Link: https://leetcode.com/problems/rotate-array/description/

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  
        nums[:] = nums[-k:] + nums[:-k]  
