# Given an m x n matrix, return all elements of the matrix in spiral order.

# Problem Link: https://leetcode.com/problems/spiral-matrix/description/

class Solution:
  def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
    if not matrix:
      return []

    result = []
    while matrix:
      result += matrix.pop(0)
      
      if matrix and matrix[0]:
        for row in matrix:
          result.append(row.pop())
      
      if matrix:
        result += matrix.pop()[::-1]
      
      if matrix and matrix[0]:
        for row in matrix[::-1]:
          result.append(row.pop(0))
    
    return result
