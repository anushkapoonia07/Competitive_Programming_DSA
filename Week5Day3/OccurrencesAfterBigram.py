# Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

# Return an array of all the words third for each occurrence of "first second third".

# Problem Link: https://leetcode.com/problems/occurrences-after-bigram/description/

class Solution:
  def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
    words = text.split()  
    return [c for a, b, c in zip(words, words[1:], words[2:]) if a == first and b == second]
