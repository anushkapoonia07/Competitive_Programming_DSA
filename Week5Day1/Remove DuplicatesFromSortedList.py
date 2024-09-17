# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

#Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import ListNode
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        return head
