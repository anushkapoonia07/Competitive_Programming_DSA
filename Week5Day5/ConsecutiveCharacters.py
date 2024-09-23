# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.

# Problem Link: https://leetcode.com/problems/consecutive-characters/description/

class Solution:
  def maxPower(self, s: str) -> int:
    max_power = 1
    current_power = 1

    for i in range(1, len(s)):
      if s[i] == s[i - 1]:
        current_power += 1
      else:
        current_power = 1
      max_power = max(max_power, current_power)

    return max_power
