# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 
# Problem Link: https://leetcode.com/problems/valid-sudoku/description/

class Solution:
  def isValidSudoku(self, board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
      for j in range(9):
        num = board[i][j]
        if num == '.':
          continue

        box_index = (i // 3) * 3 + (j // 3)
        
        if num in rows[i] or num in cols[j] or num in boxes[box_index]:
          return False
        
        rows[i].add(num)
        cols[j].add(num)
        boxes[box_index].add(num)

    return True
