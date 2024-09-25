# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Problem Link: https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
