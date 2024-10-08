# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Problem Link: https://leetcode.com/problems/word-break/description/

class Solution:
  def wordBreak(self, s: str, wordDict: list[str]) -> bool:
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
      for j in range(i):
        if dp[j] and s[j:i] in wordSet:
          dp[i] = True
          break

    return dp[-1]
