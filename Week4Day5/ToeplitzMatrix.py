# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

# Problem Link: https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
  def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
    return all(matrix[i][j] == matrix[i + 1][j + 1] for i in range(len(matrix) - 1) for j in range(len(matrix[0]) - 1))
