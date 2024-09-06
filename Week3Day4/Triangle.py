# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Problem Link: https://leetcode.com/problems/triangle/description/

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for i in reversed(range(len(triangle) - 1)):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        
        return triangle[0][0]
