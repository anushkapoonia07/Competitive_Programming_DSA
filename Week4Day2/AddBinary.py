# Given two binary strings a and b, return their sum as a binary string.

# Problem Link: https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        a, b = a[::-1], b[::-1]
        max_len = max(len(a), len(b))
        for i in range(max_len):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0
            total = digit_a + digit_b + carry
            carry = total // 2
            result.append(str(total % 2))
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])
