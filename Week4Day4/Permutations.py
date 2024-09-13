# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Problem Link: https://leetcode.com/problems/permutations/description/

class Solution:
  def permute(self, nums: list[int]) -> list[list[int]]:
    if len(nums) == 1:
      return [nums]
    
    ans = []
    for i, num in enumerate(nums):
      perms = self.permute(nums[:i] + nums[i+1:])
      for perm in perms:
        ans.append([num] + perm)
    
    return ans
