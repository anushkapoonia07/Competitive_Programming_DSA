# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

#Problem Link: https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1] * (rowIndex + 1)
        
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        
        return row
