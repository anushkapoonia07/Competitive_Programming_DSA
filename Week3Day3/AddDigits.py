# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Problem Link: https://leetcode.com/problems/add-digits/description/

class Solution:
  def addDigits(self, num: int) -> int:
    while num >= 10:
      num = sum(int(digit) for digit in str(num))
    return num
