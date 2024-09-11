# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Problem Link: https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        
        def dfs(index: int, path: list[int]) -> None:
            ans.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return ans
