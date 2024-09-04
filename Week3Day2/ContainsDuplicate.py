# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Problem Link: https://leetcode.com/problems/contains-duplicate/description/

class Solution:
  def containsDuplicate(self, nums: list[int]) -> bool:
    return len(nums) != len(set(nums))