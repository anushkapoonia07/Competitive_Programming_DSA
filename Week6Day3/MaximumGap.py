# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.

# Problem Link: https://leetcode.com/problems/maximum-gap/description/

class Solution:
  def maximumGap(self, nums: list[int]) -> int:
    if len(nums) < 2:
      return 0

    nums.sort()

    max_gap = 0

    for i in range(1, len(nums)):
      max_gap = max(max_gap, nums[i] - nums[i - 1])

    return max_gap
