# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Problem Link: https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import ListNode
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  
            curr.next = prev  
            prev = curr 
            curr = next_node
        
        return prev

        