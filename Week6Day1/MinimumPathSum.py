# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Problem Link: https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue  
                elif i == 0:
                    grid[i][j] += grid[i][j - 1] 
                elif j == 0:
                    grid[i][j] += grid[i - 1][j] 
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]) 
        
        return grid[m - 1][n - 1] 
