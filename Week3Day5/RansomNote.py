# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# problem link: https://leetcode.com/problems/ransom-note/description/

class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    for char in ransomNote:
      if ransomNote.count(char) > magazine.count(char):
        return False
    return True
