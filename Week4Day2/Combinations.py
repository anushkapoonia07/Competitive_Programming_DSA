# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# Problem Link: https://leetcode.com/problems/combinations/description/

from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return list(combinations(range(1, n + 1), k))
