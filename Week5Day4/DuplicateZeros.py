# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

# Problem Link: https://leetcode.com/problems/duplicate-zeros/description/

from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        
        while i < n:
            if arr[i] == 0:
                arr.insert(i + 1, 0)  
                arr.pop() 
                i += 1  
            i += 1