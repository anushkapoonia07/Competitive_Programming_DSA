# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# Problem Link: https://leetcode.com/problems/h-index/description/

class Solution:
  def hIndex(self, citations: list[int]) -> int:
    citations.sort(reverse=True)
    h = 0
    for i, citation in enumerate(citations):
      if citation >= i + 1:
        h = i + 1
      else:
        break
    return h
