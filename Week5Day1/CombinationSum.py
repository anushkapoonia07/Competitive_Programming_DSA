# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Problem Link: https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        
        def dfs(s: int, target: int, path: list[int]) -> None:
            if target == 0:
                ans.append(path[:])
                return
            if target < 0:
                return

            for i in range(s, len(candidates)):
                path.append(candidates[i])
                dfs(i, target - candidates[i], path)
                path.pop()

        candidates.sort()
        dfs(0, target, [])
        return ans
