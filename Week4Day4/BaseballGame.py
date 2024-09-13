# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

# Problem Link: https://leetcode.com/problems/baseball-game/description/

class Solution:
  def calPoints(self, operations: list[str]) -> int:
    scores = []

    for operation in operations:
      if operation == '+':
        scores.append(scores[-1] + scores[-2])
      elif operation == 'D':
        scores.append(scores[-1] * 2)
      elif operation == 'C':
        scores.pop()
      else:
        scores.append(int(operation))

    return sum(scores)
