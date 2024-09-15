"""https://leetcode.com/problems/remove-nth-node-from-end-of-list"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n):
            # first and last both point to the same node
            if fast.next is None:
                fast = head
                break
            fast = fast.next
        if slow == fast:
            head = head.next
            return head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
