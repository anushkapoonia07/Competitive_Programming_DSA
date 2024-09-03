# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Problem Link: https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(left: int, right: int, current: str):
            if left == 0 and right == 0:
                result.append(current)
                return
            if left > 0:
                dfs(left - 1, right, current + '(')
            if right > left:
                dfs(left, right - 1, current + ')')
        
        result = []
        dfs(n, n, '')
        return result
