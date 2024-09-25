# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

# Problem Link: https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            end = nums[i]
    
            if start == end:
                ans.append(str(start))
            else:
                ans.append(f"{start}->{end}")
            
            i += 1
        
        return ans
